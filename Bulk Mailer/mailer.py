""" This is a script
to send an e-mail in bulk along with pdf attachments.
Make sure to insert the emails line by line in the "emails.txt" file,
at the time of writing this, I'm just copying and
pasting mails from a google sheet. """

import os
import smtplib
from email.message import EmailMessage

#env variables
#getting e-mail account's login creds
EMAIL_ADDRESS = os.environ.get('USER_EMAIL')
EMAIL_PASSWORD = os.environ.get('USER_PASS')

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

mailing_list = []

#clearing up new lines and blank lines
emails = open("emails.txt")
for email in emails:
    email = email.rstrip()
    if email == "":
        continue
    mailing_list += [email]


msg = EmailMessage()

#insert subject
msg['Subject'] = "FBI open up"
msg['From'] = EMAIL_ADDRESS
msg['To'] = mailing_list

#the body of your message 
msg.set_content('...')

#insert your pdf file(s), have them in src directory or mention the path.
files = ['example2021.pdf']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)
    #octet-stream is like generec bag of bits acc to python doc

server.send_message(msg)
server.quit()
