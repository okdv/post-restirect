from email.mime.text import MIMEText 
from flask import Flask, request
import smtplib
import email.utils
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])

def result():
    print(os.environ.get('DEBUG'))
    msg = MIMEText('Test body')
    msg['To'] = email.utils.formataddr((os.environ.get('TO_NAME'), os.environ.get('TO_EMAIL')))
    msg['From'] = email.utils.formataddr((os.environ.get('FROM_NAME'), os.environ.get('FROM_EMAIL')))
    msg['Subject'] = 'Test'

    server = smtplib.SMTP_SSL(os.environ.get('SMTP_ADDR'))
    server.connect(os.environ.get('SMTP_ADDR'), int(os.environ.get('SMTP_PORT', 465)))
    server.login(os.environ.get('SMTP_USERNAME'), os.environ.get('SMTP_PASSWORD'))
    server.set_debuglevel(int(os.environ.get('DEBUG', 0)))

    try:
        server.sendmail(os.environ.get('FROM_EMAIL'),[os.environ.get('TO_EMAIL')], msg.as_string())
        print(request.form['foo'])
    finally:
        server.quit()
        return "received"
    
