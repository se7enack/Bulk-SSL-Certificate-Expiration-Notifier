#!/usr/bin/env python3

from email.message import EmailMessage
from cryptography import x509
from datetime import date
import smtplib
import socket
import stuff
import ssl

threshold_days = stuff.threshold_days
domains = stuff.domains
password = stuff.password
sender = stuff.sender
receiver = stuff.receiver
subject = stuff.subject

domain_len = []
for domain in domains:
    domain_len.append(len(domain))
domain_pad = max(domain_len)
now = str(date.today()).split("-")
today = date(int(now[0]), int(now[1]), int(now[2]))
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
ssl._create_default_https_context = ssl._create_stdlib_context


def sendemail(body):
    em = EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, em.as_string())


def checkexp():
    print("")
    output = ""
    for domain in domains:
        try:
            with socket.create_connection((domain, 443), timeout=1) as connect:
                with context.wrap_socket(connect, server_hostname=domain) as sock:
                    kind = ""
                    data = sock.getpeercert(True)
                    pem = ssl.DER_cert_to_PEM_cert(data)
                    cert = x509.load_pem_x509_certificate(str.encode(pem))
                    exp = str(cert.not_valid_after_utc).split(" ")[0].split("-")
                    expires = date(int(exp[0]), int(exp[1]), int(exp[2]))
                    delta = expires - today
                    days = int(str(delta).split(" ")[0])
                    if days < int(threshold_days):
                        if days < 1:
                            kind = "| <--- EXPIRED --->"
                            preposition = "past"
                        else:
                            kind = "| <--- WARNING --->"
                            preposition = "till"
                        msg = f" {str(abs(days)).rjust(3, ' '):<3} days {preposition:<3} public SSL expiration for {domain:<{domain_pad}} {kind} | {expires}"
                        print(msg)
                        output += f"{msg}\n"
        except:
            pass
    print(output,'\n')
    sendemail(output)


checkexp()
 
