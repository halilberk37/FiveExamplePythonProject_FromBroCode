import smtplib
#Google'ın izin vermemesi üzerine mail gönderilemedi.

sender = "halilberk1453@gmail.com"
receiver = "halilberk1453@gmail.com"
password = "halilberk1453"
subject = "Python email test"
body = "I wrote an email! (BroCode)"


message = f"""From: Emir Can{sender}
To: Halil Berk{receiver}
Subject: {subject}\n
{body}
"""


server =smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender,receiver,message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in!")

