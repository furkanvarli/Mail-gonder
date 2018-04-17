import smtplib, time, getpass, datetime, socket


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#------------------------------------------------



mail_gonderici = "furkanvarlive@gmail.com"
mail_sifresi = "15590271594f"
kime_gidecek = "furki3411@outlook.com"

baslik = "Uyarı"

msg = MIMEMultipart()
msg['From'] = mail_gonderici
msg['To'] = kime_gidecek
msg['Subject'] = baslik


msg.attach(MIMEText("sasasdsd", 'plain'))


dosya_yolu = open("download.jpg", "rb")
dosya_adi = "download.jpg"

part = MIMEBase('application', "octet-stream")
part.set_payload((dosya_yolu).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename= %s' % dosya_adi)

msg.attach(part)

mesaj = msg.as_string()

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(mail_gonderici, mail_sifresi)
server.sendmail(mail_gonderici, kime_gidecek, mesaj)
print("E-mail başarıyla gönderildi")

