import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Ashwin Bharat'
email['to'] = '18btrse031@jainuniversity.ac.in'
email['subject'] = 'I Love you 3000'

email.set_content('I am learning python and sending email with smtplib and email libraries')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email here', 'password here')
    smtp.send_message(email)
    print('all good bigg boss!!!')
