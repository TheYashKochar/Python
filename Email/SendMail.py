# Program to Send a mail to someone
# goto https://www.google.com/settings/security/lesssecureapps and click Enable to make this code run
import smtplib
conn = smtplib.SMTP('smtp.gmail.com',587)
#conn = smtplib.SMTP('out.mailsac.com',587)
print(type(conn))
print(conn.ehlo())
q=conn.starttls()
print(q)
fromid = input('Enter your Gmail Id : ')
idpass = input('Enter your Password : ')
toid = input('Enter Sender\'s Mail ID :')
mess = input('Enter the Message :\n')
conn.login(fromid,idpass)
conn.sendmail(fromid,toid,mess)
print('Mail Sent.')
print(conn.quit())
