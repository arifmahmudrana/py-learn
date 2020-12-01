import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Private Person <from@example.com>'
email['to'] = 'A Test User <to@example.com>'
email['subject'] = 'Hi Mailtrap'

email.set_content(html.substitute({'name': 'TinTin'}, value=100), 'html')

with smtplib.SMTP(host='smtp.mailtrap.io', port=2525) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('', '')
    smtp.send_message(email)
    print('All good done 🙂️✔️')
