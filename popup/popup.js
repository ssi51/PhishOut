document.addEventListener('DOMContentLoaded', () => {
  const status = document.getElementById('status');
  const result = document.getElementById('result');
  const reportButton = document.getElementById('reportButton');

  // Example logic for checking a website
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const url = new URL(tabs[0].url);
    status.textContent = `Checking ${url.hostname}...`;

    // Simulate URL scanning
    setTimeout(() => {
      const isPhishing = Math.random() < 0.5; // Random for demo purposes
      result.textContent = isPhishing ? '⚠️ Dangerous Site Detected!' : '✔️ Safe to Browse';
      result.style.color = isPhishing ? 'red' : 'green';
    }, 2000);
  });

  // Report phishing functionality
  reportButton.addEventListener('click', () => {
    alert('This site has been reported as phishing. Thank you for contributing!');
    // Future: Send the report to a database or API
  });
});
