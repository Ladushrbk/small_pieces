#!/usr/bin/env python3

import smtplib

smtp_server = "smtp.gmail.com"
smtp_port = 587
server = smtplib.SMTP(smtp_server, stmp_port)
server.starttls()

email_address = "my_email@gmail.com"
password = "my_app_with_password"
server.login(email_address, password)
