import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\KUNAL\\Desktop\\CT#10\\NEW REVISION 2023\\Scripts\\PytestFramework\\Configuration\\config.ini")

class Readconfig():

    @staticmethod
    def getLoginUrl():
        LoginUrl = config.get('user info','loginUrl')
        return LoginUrl

    @staticmethod
    def getRegistrationUrl():
        RegistrationUrl = config.get('user info','RegistrationUrl')
        return RegistrationUrl
    @staticmethod
    def getUser_email():
        User_email = config.get('user info','User_email')
        return User_email
    @staticmethod
    def getPassword():
        Password = config.get('user info','Password')
        return Password