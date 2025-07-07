# CamAlert

Originally created for VBPS

## Purpose
CamAlert checks a list of cameras to confirm whether they are online. If any cameras are unreachable, it sends an email with the IP addresses of those cameras.

## Technology Stack:
Python, SMTP

## How to Use

### Initial Setup:
1. Open `CamAlert.py` with a text editor of your choice (Notepad++ is recommended).
2. Update **Line 35** to specify the email address you would like to use as the sender.  
   **Note:** This must be a Gmail account.
3. Update **Line 36** with the password for the chosen email account.
4. Update **Line 37** with the recipients' email addresses to receive the alerts.

### After Setup:
1. Ensure that you have the latest version of Python installed on your machine.
2. Run the script.

### Tip:
Consider using a task scheduler to run the script automatically once a night. Windows has a built-in feature for this, which you can research.

