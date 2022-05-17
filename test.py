#!/usr/bin/python3

import os,  sys, re, requests, smtplib, ssl

url = 'https://status.digitalocean.com/api/v2/scheduled-maintenances.json'

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
    if '"scheduled_maintenances":[],' in r.text:
        print ( '"scheduled_maintenances":[],' in r.text)
        if  '"incidents":[],' in r.text:
            print( '"incidents":[],' in r.text)
            if '"status":"operational"' in r.text:
                print('"status":"operational"' in r.text)
                return True

def sendmail():
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port, timeout=3) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("EMAIL SENT: "  + sender_email + '\n' + receiver_email + '\n' + password + '\n' + smtp_server + ':' + port + '\n')

def run():
    if status():
        print("OK")
    else:
        print("ISSUES")
        sendmail()

run()

