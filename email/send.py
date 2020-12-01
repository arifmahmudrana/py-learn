# import smtplib

# sender = "Private Person <from@example.com>"
# receiver = "A Test User <to@example.com>"

# message = f"""\
# Subject: Hi Mailtrap
# To: {receiver}
# From: {sender}

# This is a test e-mail message."""

# with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
#     server.login("", "")
#     server.sendmail(sender, receiver, message)


import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Private Person <from@example.com>'
email['to'] = 'A Test User <to@example.com>'
email['subject'] = 'Hi Mailtrap'

email.set_content(
    'This is a test e-mail message.')

with smtplib.SMTP(host='smtp.mailtrap.io', port=2525) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("", "")
    smtp.send_message(email)
    print('All good done 🙂️✔️')
