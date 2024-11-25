import pandas as pd
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv('data/phishing_dataset.csv')  # Replace with your dataset file
data['label'] = data['label'].map({'phishing': 1, 'legitimate': 0})  # Convert labels to binary

# Feature extraction from URLs
def extract_features(url):
    return {
        'length': len(url),
        'has_ip': int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url))),
        'num_special_chars': len(re.findall(r'[@#?&]', url))
    }

# Apply feature extraction
features = pd.DataFrame(data['url'].apply(extract_features).tolist())
X = features
y = data['label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")

# Save the model
import joblib
joblib.dump(model, 'phishing_model.pkl')
