# AI-Log-Analyzer

## Overview  
AI-Powered Log Analyzer is a Python-based tool that leverages **Google's Gemini AI** to analyze server logs, detect cyber threats, and classify them using the **MITRE ATT&CK framework**. It helps security professionals and IT students assess logs for potential attacks, Indicators of Compromise (IoCs), and provides mitigation strategies.  

## Features  
- **AI-Driven Analysis**: Uses **Gemini AI** to classify logs as normal or attack-related.  
- **MITRE ATT&CK Integration**: Identifies attack techniques, privilege escalation, and post-exploitation activities.  
- **IoC Detection**: Highlights suspicious patterns, persistence mechanisms, and forensic insights.  
- **Mitigation Strategies**: Provides security recommendations with references to CVEs.

## Requirements  
- Python 3.12.x.
- Google Generative AI (`google-generativeai`)  
- Standard Python libraries: `os`, `json`, `time`  

## Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/stellados53/AI-Log-Analyzer.git

2. Navigate to the project folder:
   ```bash
   cd ai-log-analyzer

3. Get the Gemini API Key:
- Go to [Google AI Studio](https://aistudio.google.com/apikey) and sign in.
- Navigate to the API Keys section.
- Generate a new API key and copy it.
- Now modify with your actual API key. `nano main.py`.
- Set up the API Key.
   ```
   genai.configure(api_key="aaouewnvbsxxxxxx")
- Replace `api_key` with your actual API key in `line 27`.

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
## Usage
- Run the script:
   ```bash
   python main.py
```
==============================
      AI LOG ANALYZER 
==============================
 + -- --=[ AI-powered log analysis tool ]--  
 + -- --=[ Detects attacks & references MITRE ATT&CK ] 
 + -- --=[ Provides forensic insights & mitigation steps ] 
  
Enter the log file path: 
```
- Enter the path to the log file when prompted.
- Some of the sample logs are provided in the `samplelogs` folder.
- Review the AI-generated forensic analysis in real time.
 
Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
