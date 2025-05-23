# SCT_CS_3
🔐 Password Strength Checker (Python CLI)
This is a simple command-line Python tool to check the strength of a password based on essential security criteria. It provides real-time feedback and a final verdict on the password’s strength.

📋 Features
🔍 Checks for:

Minimum length (8+ characters)

At least one digit

At least one uppercase letter

At least one lowercase letter

At least one special character

📊 Displays a report with pass/fail status for each rule

🛡️ Gives a final verdict: Very Strong, Moderate, or Weak

💻 Clean and beginner-friendly CLI interface

🧰 Requirements
Python 3.x

🧠 How It Works
The tool checks the entered password against 5 rules:

Rule	Description
Length	At least 8 characters
Digits	At least one numeric digit (0-9)
Uppercase Letters	At least one capital letter (A-Z)
Lowercase Letters	At least one lowercase letter (a-z)
Special Characters	At least one symbol (e.g., @, #, etc)

🏁 Verdict Logic
✅ Very Strong 🔐 – Passes all 5 checks

⚠️ Moderate – Passes 3 or 4 checks

❌ Weak – Passes fewer than 3 checks

🧾 Sample Output
yaml
Copy
Edit
==========================================
  Welcome to Password Strength Checker 🔐
       Created by: Cyber Expert 💻🛡️
==========================================

Enter your password to check strength: MyPass123!

Password Strength Report:
✅ Length check: Passed
✅ Digits check: Passed
✅ Uppercase check: Passed
✅ Lowercase check: Passed
✅ Symbols check: Passed

Final Verdict: Very Strong 🔐

📜 License
This project is licensed under the MIT License.
