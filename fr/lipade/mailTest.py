import smtplib

fromaddr = 'id.toufik3@gmail.com'
toaddrs  = ['id.toufik1@gmail.com', 'id.toufik@hotmail.com']

msg = "\r\n".join([
  "From: id.toufik3@gmail.com",
  "To: id.toufik1@gmail.com, id.toufik@hotmail.com",
  "Subject: Just a message",
  "",
  "python test"
  ])


username = 'user_me@gmail.com'
password = 'pwd'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login("id.toufik3@gmail.com","standard1")
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
