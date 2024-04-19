import smtplib
from email.message import EmailMessage
import os
GMAIL_PASS = os.getenv("GMAIL_PASS")
print(GMAIL_PASS)

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()

smtp.login("seoseungjae20209@gmail.com", GMAIL_PASS)
email = EmailMessage()
email["Subject"] = "이메일 제목입니다"
email["From"] = "seoseungjae20209@gmail.com"
email["To"] = "bamyam_python@yopmail.com"
email.set_content("이메일 내용입니다")
smtp.send_message(email)
smtp.quit()