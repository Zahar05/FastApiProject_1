# smtp_test.py


import smtplib

host = "smtp.gmail.com"
port = 587

user = "zaipulla1989@gmail.com"
password = "rlaktcsddrplhyne"

server = smtplib.SMTP(host, port)

server.starttls()

server.login(user, password)

print("SUCCESS")

server.quit()




# import smtplib
#
# host = "smtp.yandex.ru"
# port = 587
#
# user = "zaipullarajabov@yandex.ru"
# password = "zlflinjxehvuchbt"
#
# server = smtplib.SMTP(host, port)
#
# server.starttls()
#
# server.login(user, password)
#
# print("SUCCESS")
#
# server.quit()
