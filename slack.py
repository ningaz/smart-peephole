from slacker import Slacker
import configparser

class Notifier():
    def __init__(self,token, botname, channel):
        self.msgQueue = []
        self.slack = Slacker(token)
        self.channel = channel
        self.bot = bot
    def getNotification(self):
        if  len(self.msgQueue) > 1:
            return self.msgQueue.pop(0)
        return ''
    def sendSlackNotification(self, msg, file = None):
        #self.slack.chat.post_message(self.channel, msg, self.bot,icon_emoji='vhs',as_user=True)
        if(file != None):
            self.slack.files.upload(file_=file,filetype='jpeg',title=msg,channels=self.channel)            
    def setNotification(self, msg):
        self.msgQueue.append(msg)

conf = configparser.RawConfigParser()
conf.read('config.cfg')
token = conf.get('slack', 'token')
bot = conf.get('slack', 'botname')
channel = conf.get('slack', 'channel')
msg = conf.get('slack', 'msg')
img = conf.get('main', 'img')

notify = Notifier(token, bot, channel)
notify.sendSlackNotification(msg, img)
