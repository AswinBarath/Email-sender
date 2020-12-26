import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Ashwin Bharat'
email['to'] = '18btrse031@jainuniversity.ac.in'
email['subject'] = 'I Love you 3000'

# email.set_content(html.substitute(name='TinTin'))
email.set_content(html.substitute({'name': 'Tony Stark'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email here', 'password here')
    smtp.send_message(email)
    print('all good bigg boss!!!')
