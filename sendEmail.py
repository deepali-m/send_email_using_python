#importing necessary libraries
import smtplib
import imghdr
from email.message import EmailMessage

#defining a function send email
def send_email():
    #creating an object of EmailMessage()
    message = EmailMessage()    
    #assigning a subject line
    message['subject']= "Email from Deepali"
    #assigining the sender
    message['from'] = 'deepali.test2021@gmail.com'
    #assigining the recepient
    message['to']= input("Enter the recepient : ")
    
    #opening and reading html file which contains the message
    html_message = open('demo.html').read()
    message.add_alternative(html_message,subtype='html')

    # attaching an image to the email
    with open('newimg.png','rb') as attach:
        image_name = attach.name
        image_type = imghdr.what(attach.name)
        image_date = attach.read()

    message.add_attachment(image_date,maintype='image',
            subtype=image_type,filename= "WOW.png")

    #starting smtp server with a port number
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login("deepali.test2021",'deepali2021')
        smtp.send_message(message)
    print("Email sent!")
    

send_email()