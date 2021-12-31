import configparser
config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")
class ReadConfig:
    @staticmethod
    def getipAddress():
        IP=config.get('Common Info','ipAdd')
        return IP

    @staticmethod
    def getUserName():
        username = config.get('Common Info', 'username')
        return username

    @staticmethod
    def getUserPass():
        password = config.get('Common Info', 'password')
        return password