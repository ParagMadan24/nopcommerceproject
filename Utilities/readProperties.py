import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadProperties:
    @staticmethod
    def getbaseurl():
        return config.get('common_info','base_url')
    @staticmethod
    def geturename():
        return config.get('common_info','login_username')
    @staticmethod
    def getpassword():
        return config.get('common_info','login_password')