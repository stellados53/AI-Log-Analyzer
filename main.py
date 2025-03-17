
import google.generativeai as genai
import json
import os
import time

def typewriter_effect(text):
    """Simulates AI typing effect for a realistic output experience."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.002)  # Adjust typing speed
    print()  


def load_log_file(file_path):
    """Reads the log file content if the file exists."""
    if not os.path.exists(file_path):
        print("Error: File not found.")
        return None
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def analyze_logs_with_gemini(log_content):
    """Uses Gemini API to analyze logs and categorize them as normal or attack with detailed MITRE ATT&CK framework references."""
    try:
        genai.configure(api_key="API_KEY")
        model = genai.GenerativeModel("gemini-1.5-pro")
        
        prompt = (
            "Analyze the following server logs sequentially. For each log entry, determine whether it represents normal activity or an attack. "
            "If it's an attack, classify it using the MITRE ATT&CK framework, provide relevant TTPs, explain the attack technique, and outline its impact in informative and effective and technical manner for IT student. "
            "If it's normal, state it clearly. Also, highlight indicators of compromise (IoCs), privilege escalation attempts, persistence mechanisms, "
            "post-exploitation activities, and any unusual patterns observed. Provide a technical assessment with mitigation recommendations and references to CVEs or similar attack reports.and also just give the text don't bold. \n\n"
            f"Log Content:\n{log_content}"
        )
        
        response = model.generate_content(prompt)
        return response.text if response else "No response from AI."
    except Exception as e:
        return f"Error during AI analysis: {str(e)}"

def main():  
    while True:
        print("\n==============================")
        print("                     AI LOG ANALYZER ")
        print("==============================")
        print("\n + -- --=[ AI-powered log analysis tool ]--  \n + -- --=[ Detects attacks & references MITRE ATT&CK ] \n + -- --=[ Provides forensic insights & mitigation steps ] \n  ")
        log_file_path = input("Enter the log file path: ")  # Ask for log file path at runtime
        logs = load_log_file(log_file_path)
        
        if logs is None:
            retry = input("Invalid file path.\n Do you want to run again or exit? (y/n): ").strip().lower()
            if retry != 'y':
                print("Exiting Log Analyzer.")
                break
            continue

        
        print("\n--- AI Forensic Analysis Result ---\n")
        analysis_result = analyze_logs_with_gemini(logs)
        typewriter_effect(analysis_result)
        
        
        retry = input("\nDo you want to run the analysis again? (y/n): ").strip().lower()
        if retry != 'y':
#	    print("Exiting...!!")
            break


if __name__ == "__main__":
    main()
