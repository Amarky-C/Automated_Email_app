#create a project that will send an automatic email every 10mins

import smtplib
from email.message import EmailMessage 
import ssl
import time

#Email content
name = "Amaka"
address_sender = 'amarkychinelle@gmail.com'
password_sender =  'roqdsjxcrbhmvnxb'
input_address_recipients = 'issabolanle44@gmail.com, okulichrist@gmail.com,delaw34@yah00.com, mosesoleka@gmail.com, chinelomojekwu@gmail.com, obidienttrainingclassb@gmail.com, callistus100@gmail.com'
address_recipients = input_address_recipients.split(',')
subject = 'Automated Email'
body =  'Hello how are you doing, this is an automated email sent every 10 minutes to remind you of your assignment submission before 7pm, pls deploy to your github account and send the link to the email. Thanks.'

email_msg = EmailMessage()

email_msg['From'] = address_sender
email_msg['To'] = ','.join(input_address_recipients)
email_msg['Subject'] = subject
email_msg.set_content(body)

#create a default connection to send bulk message
context = ssl.create_default_context()


def perform_task():
 #Connect to the SMTP server


 with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as mysmtp:
    mysmtp.login(address_sender,password_sender)
    mysmtp.sendmail(address_sender,input_address_recipients, email_msg.as_string())
    print('Hi Amaka,your message has been sent successfully')
        

       #send mail every 10 minutes
while True:
    perform_task()
    time.sleep(10)  # 10 minutes = 10 * 60 seconds