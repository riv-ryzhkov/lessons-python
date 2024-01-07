
# =================================================
#  Работает оправка ukr.net -> gmail.com
# =================================================
# import smtplib, ssl
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
#
# smtp_server = "smtp.ukr.net" # hostname
# port = 465
#
# login = "riv.ryzhkov@ukr.net"
# password = "CFbbZXz3NEDWjsKZ"
#
# to = 'riv.ryzhkov@gmail.com'
# subject = 'Прошло!!!'
# body = """
# Ура! Заработало!!!
# Наконец-то, все работает и отправляется!
# Поздравляю!
# """
#
# multipart_msg = MIMEMultipart()
#
# multipart_msg['From'] = login
# multipart_msg['To']= to
# multipart_msg['Subject']= subject
# multipart_msg.attach(MIMEText(body))
#
# context = ssl.create_default_context() # Только, если нужно включить SSL
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
# # with smtplib.SMTP(smtp_server, port) as server: # при использовании TSL
#     server.login(login, password)
#     # # server.starttls() # только, если подключен TSL
#     server.send_message(multipart_msg)
#
#

# ========================================================
# ========================================================
#
# import yagmail
#
#
# yag = yagmail.SMTP('riv.django@gmail.com', 'Django34!')
# yag.send(to = 'riv.ryzhkov@gmail.com',
#          subject = 'hi',
#          contents = 'Just wanted to say "hi"')
# ================================================================
# ================================================================
#
#
#
# import smtplib
#
# HOST = "smtp.ukr.net"
# SUBJECT = "Test email from Python"
# TO = "riv.ryzhkov@gmail.com"
# FROM = "riv.ryzhkov@ukr.net"
# text = "Python text is sent with smtplib!"
#
# BODY = "\r\n".join((
#     "From: %s" % FROM,
#     "To: %s" % TO,
#     "Subject: %s" % SUBJECT,
#     "",
#     text
# ))
#
# # server = smtplib.SMTP(HOST, 465)
# server = smtplib.SMTP_SSL('smtp.ukr.net', 465)
# # server.starttls()
# # server.login(FROM, 'CFbbZXz3NEDWjsKZ')
# server.login(FROM, 'CFbbZXz3NEDWjsKZ')
# server.sendmail(FROM, [TO], BODY)
# server.quit()



# ================================================================
# smtplib       email.mime
# ================================================================


# import smtplib  # Импортируем библиотеку по работе с SMTP
#
# # Добавляем необходимые подклассы - MIME-типы
# from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
# from email.mime.text import MIMEText  # Текст/HTML
#
# addr_from = "riv.ryzhkov@ukr.net"
# addr_to = "riv.ryzhkov@ukr.net"
# password = "CFbbZXz3NEDWjsKZ"  # пароль от почты addr_from
#
# msg = MIMEMultipart()  # Создаем сообщение
# msg['From'] = "riv.ryzhkov@ukr.net"  # Адресат
# msg['To'] = "riv.ryzhkov@gmail.com"  # Получатель
# msg['Subject'] = 'Тема сообщения'  # Тема сообщения
#
# body = "Текст сообщения"
# msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст
#
#
# server = smtplib.SMTP_SSL('smtp.ukr.net', 465)  # Создаем объект SMTP
# # server.starttls()             # Начинаем шифрованный обмен по TLS
# server.login(addr_from, password)  # Получаем доступ
# server.send_message(msg)  # Отправляем сообщение
# server.quit()  # Выходим


# # =====================================================
# # Работает множественная рассылка   ukr.net -> gmail.com ukr.net
# # =====================================================
#
# import smtplib
# import ssl
# from string import Template
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
#
# def get_users(file_name):
#     names = []
#     emails = []
#     with open(file_name, mode='r', encoding='utf-8') as user_file:
#         for user_info in user_file:
#             names.append(user_info.split()[0])
#             emails.append(user_info.split()[1])
#         return names, emails
#
#
# def parse_template(file_name):
#     with open(file_name, 'r', encoding='utf-8') as msg_template:
#         msg_template_content = msg_template.read()
#         return Template(msg_template_content)
#
#
# def main():
#     smtp_server = "smtp.ukr.net"  # hostname
#     port = 465
#     FROM_EMAIL = 'riv.ryzhkov@ukr.net'
#     MY_PASSWORD = 'CFbbZXz3NEDWjsKZ'
#
#     names, emails = get_users('contacts.txt') # read user details
#     message_template = parse_template('message.txt')
#
#
#     context = ssl.create_default_context() # Только, если нужно включить SSL
#     server = smtplib.SMTP_SSL(smtp_server, port, context=context)
#         # server.starttls()
#     server.login(FROM_EMAIL, MY_PASSWORD)
#
#         # Get each user detail and send the email:
#     for name, email in zip(names, emails):
#         multipart_msg = MIMEMultipart() # create a message
#
#             # add in the actual person name to the message template
#         message = message_template.substitute(USER_NAME=name.title())
#
#             # Prints out the message body for our sake
#         print(email)
#         print(message)
#         print('*'*80)
#
#             # setup the parameters of the message
#         multipart_msg['From']= FROM_EMAIL
#         multipart_msg['To']= email
#         multipart_msg['Subject']= "Ukr-net to gmail.com"
#
#             # add in the message body
#         multipart_msg.attach(MIMEText(message, 'plain'))
#
#             # send the message via the server set up earlier.
#         server.send_message(multipart_msg)
#         del multipart_msg
#
#
#         # Terminate the SMTP session and close the connection
#     server.quit()
#
#
# if __name__ == '__main__':
#     main()
#
