import smtplib

HOST = "mail.example.com"
PORT = 25
SUBJECT = "Hi"
TO = "sara.kedd@gmail.com"
NAME = "Adam"
SURNAME = "Benes"
FROM = "%s" % NAME.lower() + ".%s" % SURNAME.lower() + "@"
print("FROM: %s" % FROM)
text = "Dobry den,\n\n Nice \n \n S pozdravem,\n %s %s" % (NAME, SURNAME)
BODY = "\r\n".join((
    "From: %s" % NAME +" %s" % SURNAME + " %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text)
)
server = smtplib.SMTP(HOST, PORT)
server.sendmail(FROM, [TO], BODY)
server.quit()