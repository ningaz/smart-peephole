from slacker import Slacker

class Notifier():
    msgQueue = []
    slack = Slacker('xoxb-98814092768-gDZCppKCakyAZpio3KYw72Tx')
    def getNotification(self):
        #print len(self.msgQueue)
        if  len(self.msgQueue) > 1:
            return self.msgQueue.pop(0)
        return ''
    def sendSlackNotification(self, msg, file = None):
        #self.slack.chat.post_message('#vaapi', msg, '@vabot',icon_emoji='vhs',as_user=True)
        if(file != None):     
		self.slack.files.upload(file_=file,filetype='jpeg',title='New guest',channels='#vaapi')

    def setNotification(self, msg):
        self.msgQueue.append(msg)
        #print msg
		
notify = Notifier()		
notify.sendSlackNotification(str('New guest'),'/home/root/image.jpeg')
