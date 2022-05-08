import smtplib
from email.mime.text import MIMEText

def sendEmail(sender_email, password, to, subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        message = MIMEText('{msg}')
        # message = f'From: {sender_email}\nTo: {to}\nSubject: {subject}\n\n{msg}'
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = to
        print(message)

        server.sendmail(sender_email, to, message.as_string())
        server.quit()
        print("Email Sent")
    except:
        print("Some Error Occured")

# if __name__ == '__main__':
#     SENDER_EMAIL = "youremail@xyz.com"
#     PASSWORD = "password"
#     TO = "yourfrnds@email.com"
#     SUBJECT = "Just having fun"
#     MESSAGE = "hey dawg! it's my first Email"
#     sendEmail(SENDER_EMAIL, PASSWORD, TO, SUBJECT, MESSAGE)
