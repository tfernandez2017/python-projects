import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Tory Fernandez'
email['to'] = 'fernandt896@gmail.com'
email['Subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # introduce yourself to the server
    smtp.starttls()  # upgrade secure connection
    smtp.login('fernandt896@gmail.com', 'bjmm zidr dheq nyew')
    smtp.send_message(email)
    print('all good boss!')