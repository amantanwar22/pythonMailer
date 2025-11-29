import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = "jsforwork531@gmail.com"
APP_PASSWORD = "abcdefghijklmnop" #enter here 16 digit password
# RECEIVER_EMAIL = "aparneshgaurav@gmail.com"
df = pd.read_csv("emails.csv")

SUBJECT = "Test mail using Python"
BODY = "Hello, this mail has been sent using Python and Gmail SMTP"

def send_email(to_email,message_body):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = "Testing"
    msg.attach(MIMEText(message_body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)

        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}:", e)

for index, row in df.iterrows():
    send_email(row['email'], row['message'])
