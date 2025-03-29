from email.message import EmailMessage
import smtplib
import getpass

message = EmailMessage()
sender = "mtbuffum9@gmail.com"
recipient = "ctbuffum@gmail.com"
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'What UP Dad'
body = """Listen HERE!


I'm learning to send emails using Python!
Because I had a smart dad that taaught me to like computers."""
message.set_content(body)
mail_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
mail_pass = getpass.getpass('Enter Your APP Password? ')
mail_server.login(sender, mail_pass)
mail_server.send_message(message)



mail_server.quit()
