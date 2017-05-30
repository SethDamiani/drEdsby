import requests, json, configparser, os, sys

from .edsby import Edsby


class EdsbyAccess(object):
    def __init__(self):
        self.host, self.username, self.password = self.read_config()
        self.edsby = Edsby(host=self.host, username=self.username, password=self.password)

    def read_config(self):
        # Setup config
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(sys.argv[0]), 'config.ini')
        config.read(config_path)
        # Create new config if one does not exist
        if not os.path.isfile(config_path):
            config.add_section('auth')
            config.set('auth', 'host', 'your_instance.edsby.com')
            config.set('auth', 'username', 'your_username')
            config.set('auth', 'password', 'your_password')
            with open(config_path, 'w') as f:
                config.write(f)
            raise ValueError("Specify credentials in [auth] of config.ini")
        # Raise error if placeholders still present in config
        if config.get('auth', 'host') == 'your_instance.edsby.com' or config.get('auth',
                                                                                 'username') == 'your_username' or config.get(
            'auth', 'password') == 'your_password':
            raise ValueError("Specify credentials in [auth] of config.ini")
        else:
            self.host = config.get('auth', 'host')
            self.username = config.get('auth', 'username')
            self.password = config.get('auth', 'password')
        print('read')
        return self.host, self.username, self.password

    def getCurrentClasses(self):
        return self.edsby.getCurrentClasses()

    def getClassFeed(self, classNID):
        return self.edsby.getClassFeed(classNID)

    def getScrollingNews(self):
        return self.edsby.getScrollingNews()

    def getZoomRooms(self):
        return self.edsby.getZoomRooms()

    def getBaseActivity(self):
        return self.edsby.getBaseActivity()

    def getAllClasses(self):
        return self.edsby.getAllClasses()

    def getAttachmentDownloadURL(self, classNID, feedItemNID, feedItemRID, attachmentNID):
        return self.edsby.getAttachmentDownloadURL(classNID, feedItemNID, feedItemRID, attachmentNID)

    def getProfilePic(self, userNID, size=0):
        return self.edsby.getProfilePicDownloadURL(userNID, size)

    def getSchedule(self, targetDate=0):
        return self.edsby.getSchedule(targetDate)
