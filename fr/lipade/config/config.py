from ConfigParser import ConfigParser
import fr.lipade.config as config
class Config(ConfigParser):

	def __init__(self):
		ConfigParser.__init__(self)
		self.read("/".join([config.__path__[0], "config.properties"]))

	def getProperty(self, key):
		return self.get("section", key)


if __name__ == "__main__":
	config = Config()
	print config.getProperty("mail.smtp.host")