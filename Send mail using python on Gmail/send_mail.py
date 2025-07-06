import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "your_email@gmail.com"
sender_password = "your_app_password"

receiver_email = input("Enter recipient's email address: ")
subject = input("Enter subject: ")
body = input("Enter email body: ")

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Failed to send email.")
    print("Error:", e)
