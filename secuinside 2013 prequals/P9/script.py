#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText
import sys,os

sender = "sender"
to = sys.argv[2]
data = os.popen("/home/solve1/vuln "+"'"+sys.argv[3]+"'").read()

msg = MIMEText(data)
msg['subject'] = "hello"
msg['From'] = sender
msg['To'] = to

smtpserver = 'smtp.gmail.com'
smtpuser = 'secucu09@gmail.com'
smtppass = 'qlalfqjsghsmsrlfrp'

session = smtplib.SMTP(smtpserver,587)
session.ehlo()
session.starttls()
session.ehlo()

session.login(smtpuser,smtppass)

session.sendmail(sender,[to],msg.as_string())
session.close()

