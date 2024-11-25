import pandas as pd
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
data = pd.read_csv('data/phishing_dataset.csv')  # Ensure your dataset is in the data/ folder

# Extract features from URLs
def extract_features(url):
    return {
        'length': len(url),
        'has_ip': int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url))),
        'num_special_chars': len(re.findall(r'[@#?&]', url))
    }

# Apply feature extraction
features = pd.DataFrame(data['url'].apply(extract_features).tolist())
X = features
y = data['label']  # Ensure your dataset has a 'label' column (1 = phishing, 0 = legitimate)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'phishing_model.pkl')
print("Model saved as phishing_model.pkl")
