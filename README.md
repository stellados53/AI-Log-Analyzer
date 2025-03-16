# AI-Log-Analyzer

## Overview  
AI-Powered Log Analyzer is a Python-based tool that leverages **Google's Gemini AI** to analyze server logs, detect cyber threats, and classify them using the **MITRE ATT&CK framework**. It helps security professionals and IT students assess logs for potential attacks, Indicators of Compromise (IoCs), and provides mitigation strategies.  

## Features  
- **AI-Driven Analysis**: Uses **Gemini AI** to classify logs as normal or attack-related.  
- **MITRE ATT&CK Integration**: Identifies attack techniques, privilege escalation, and post-exploitation activities.  
- **IoC Detection**: Highlights suspicious patterns, persistence mechanisms, and forensic insights.  
- **Mitigation Strategies**: Provides security recommendations with references to CVEs.  
- **Interactive Interface**: Includes a **typewriter effect** for realistic AI-generated responses.  

## Requirements  
- Python 3.12  
- Google Generative AI (`google-generativeai`)  
- Standard Python libraries: `os`, `json`, `time`  

## Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/ai-log-analyzer.git

2. Navigate to the project folder:
   ```bash
   cd ai-log-analyzer
3. Get the Gemini API Key:
- Go to Google AI Studio and sign in.
- Navigate to the API Keys section.
- Generate a new API key and copy it.
- Set up the API Key:

Create a .env file in the project folder:
bash
Copy
Edit
touch .env
Open the .env file and add the following line:
env
Copy
Edit
GEMINI_API_KEY=your_api_key_here
Replace your_api_key_here with your actual API key.
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Run the script:
bash
Copy
Edit
python log_analyzer.py
Enter the path to the log file when prompted.
Review the AI-generated forensic analysis in real time.
Example Output
lua
Copy
Edit
==============================
          AI LOG ANALYZER  
==============================
Enter the log file path: logs.txt  

--- AI Forensic Analysis Result ---  
Analyzing logs...  
Detected possible brute-force attack (MITRE ATT&CK T1110).  
Indicators of Compromise: Multiple failed login attempts from the same IP.  
Mitigation: Enable account lockout policies and 2FA.  
Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
