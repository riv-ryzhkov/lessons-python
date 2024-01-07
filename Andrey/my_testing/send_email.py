import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


smtp_server = "smtp.gmail.com" # hostname
port = 465

login = "riv.django@gmail.com"
password = "Django34!"

to = 'riv.ryzhkov@gmail.com'
subject = 'Прошло!!!'
body = """
Ура! Заработало!!!
Наконец-то, все работает и отправляется!
Поздравляю!
"""

multipart_msg = MIMEMultipart()

multipart_msg['From'] = login
multipart_msg['To']= to
multipart_msg['Subject']= subject
multipart_msg.attach(MIMEText(body))

context = ssl.create_default_context() # Только, если нужно включить SSL
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
# with smtplib.SMTP(smtp_server, 587) as server: # при использовании TSL

    # server.starttls() # только, если подключен TSL
    server.login(login, password)
    server.send_message(multipart_msg)




# # using SendGrid's Python Library
# # https://github.com/sendgrid/sendgrid-python
# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
#
#
# message = Mail(
#     from_email='corezoid.riv@gmail.com',
#     to_emails='corezoid.riv@gmail.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# try:
#     sg = SendGridAPIClient(os.environ.get('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'))
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e)