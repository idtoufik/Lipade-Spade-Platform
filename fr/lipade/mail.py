import smtplib
from fr.lipade.config.config import Config

class Message:

	def __init__(self):
		self.receivers = []
		self.subject = ""
		self.sender = ""
		self.content = ""


	def getReceivers(self):
		return self.receivers

	def getSubject(self):
		return self.subject

	def getSender(self):
		return self.sender

	def getContent(self):
		return self.content

	def setReceivers(self, receivers):
		self.receivers = receivers

	def addReceiver(self, receiver):
		self.receivers.append(receiver)

	def addReceivers(self, receivers):
		self.receivers.extend(receivers)

	def setSubject(self, subject):
		self.subject = subject

	def setSender(self, sender):
		self.sender = sender

	def setContent(self, content):
		self.content = content

	def toString(self):
		return "\r\n".join([
			"From: " + self.getSender(),
			"To:" + ",".join(self.getReceivers()),
			"Subject: " + self.getSubject(),
			"",
			self.getContent()
		])


class MailService:

	def __init__(self, userName = None, password = None):

		self.userName = userName
		self.password = password

		if userName is None or password is None :
			config = Config()
			self.userName = config.getProperty("mail.smtp.user")
			self.password = config.getProperty("mail.smtp.password")

	def sendMessage(self, message):
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(self.userName, self.password)
		server.sendmail(message.getSender(), message.getReceivers(), message.toString())
		server.quit()

if __name__ == "__main__":
	m = MailService()
	message = Message()
	message.setSubject("test class message")
	message.addReceiver("id.toufik1@gmail.com")
	message.setSender("id.toufik3@gmail.com")
	message.setContent("test")
	m.sendMessage(message)