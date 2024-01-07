import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



# Настройки SMTP сервера и учетных данных
smtp_server = 'smtp.gmail.com'  # Замените на адрес вашего SMTP сервера
smtp_port = 587  # Порт вашего SMTP сервера (обычно 587 для TLS)
smtp_username = 'riv.ryzhkov@gmail.com'  # Ваша почта
smtp_password = 'iphone34R'  # Ваш пароль


# import smtplib
#
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
#
# print('==========')
# server = smtplib.SMTP(smtp_server, smtp_port)
# print(server)
# breakpoint()




# Адрес отправителя и получателя
from_email = 'riv.ryzhkov@gmail.com'  # Ваша почта
to_email = 'riv.ryzhkov@gmail.com'  # Адрес получателя
print('=========================')
# Создаем объект SMTP
try:
    print('************')
    server = smtplib.SMTP(smtp_server, smtp_port)
except Exception as e:
    print(f"Ошибка при подключении: {str(e)}")
print('=========================')
# Устанавливаем TLS соединение (шифрование)
server.starttls()
print('=========================')
# Логинимся на почтовом сервере
server.login(smtp_username, smtp_password)
print('=========================')

# Создаем сообщение
subject = 'Тема письма'
message = 'Привет, это тестовое письмо.'
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Отправляем письмо
server.sendmail(from_email, to_email, msg.as_string())

# Закрываем соединение с SMTP сервером
server.quit()


"""
Прежде чем использовать этот код, замените следующие значения:

smtp_server - адрес SMTP сервера вашего почтового провайдера.
smtp_port - порт SMTP сервера (обычно 587 для TLS).
smtp_username - ваш адрес электронной почты.
smtp_password - ваш пароль для электронной почты.
from_email - ваш адрес электронной почты.
to_email - адрес получателя.
subject - тема письма.
message - текст сообщения.

Пожалуйста, будьте осторожны с хранением пароля. 
Настоятельно рекомендуется использовать временные пароли при подключении к SMTP серверу,
 чтобы обеспечить безопасность вашей учетной записи."""