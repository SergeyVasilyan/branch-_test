#!/usr/bin/python
from threading import Timer
from datetime import datetime, timedelta
import smtplib
product_id="ABC-123-asas-2"
def send_mail(days):
   port = 2525
   smtp_server = "smtp.mailtrap.io"
   login = "e6c2129f4eabc9"
   password = "3cb0410fc4436f"

   sender = 'kampr@support.com'
   receiver = 'customer@mail.com'

   message = """From:Kampr Support <{}>
To: Customer <{}>
Subject: License Expiration

Dear Customer,

Your Reader with {} product ID will be expired in {} days.

Regards,
Kampr Security Systems
""".format(sender, receiver, product_id, 8 - days)

   try:
      smtpObj = smtplib.SMTP(smtp_server, port)
      smtpObj.starttls()
      smtpObj.login(login, password)
      smtpObj.sendmail(sender, receiver, message)
      print ("Successfully sent email")
   except:
      print ("Error: unable to send email")

today = datetime.today()
for second in range(7, 0, -1):
    date = today.replace(day=today.day, hour=today.hour, minute=today.minute+1, second=25+3*second, microsecond=00) + timedelta(days=0)
    delta_t = date - today
    seconds = delta_t.total_seconds()
    timer = Timer(seconds, send_mail, [second])
    timer.start()
