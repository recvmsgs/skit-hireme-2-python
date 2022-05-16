#!/usr/bin/python3

import os,  sys, re, requests, smtplib, ssl

url = 'https://status.digitalocean.com/api/v2/summary.json'

smtp_server = os.environ.get('SMTP_ADDR','smtp.gmail.com')
port = os.environ.get('SMTP_PORT',587)
sender_email = os.environ.get('MAIL_FROM','skit.alerts@gmail.com')
receiver_email = os.environ.get('SKIT_ALERT_EMAIL','recvmsgs@gmail.com')
password = os.environ.get('MAIL_PASS','nepoviemHesl0')

subject = 'ISSUES, see https://status.digitalocean.com/'
text = subject
message = 'Subject: {}\n\n{}'.format(subject, text)

def status():
    r = requests.get(url)
    if re.search('\"scheduled_maintenances\":\[\],', r.text):
        if re.search('"incidents":\[\],', r.text):
            if re.search('"status":"operational"', r.text):
                return True
def sendmail():
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port, timeout=3500) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("EMAIL SENT")
def run():
    if status():
        print("OK")
    else:
        print("ISSUES")
        sendmail()

run()

