from slacker import Slacker

class Notifier():
    msgQueue = []
    slack = Slacker('put this your Slack token')
    def getNotification(self):
        #print len(self.msgQueue)
        if  len(self.msgQueue) > 1:
            return self.msgQueue.pop(0)
        return ''
    def sendSlackNotification(self, msg, file = None):
        #self.slack.chat.post_message('#channel', msg, '@botname',icon_emoji='icon',as_user=True)
        if(file != None):     
		self.slack.files.upload(file_=file,filetype='jpeg',title='New guest',channels='#channel')

    def setNotification(self, msg):
        self.msgQueue.append(msg)
        #print msg
		
notify = Notifier()		
notify.sendSlackNotification(str('New guest'),'path to image.jpeg')
