import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.UserProfilePage import UserProfile_Class
from utilities.readproperties import Readconfig
from utilities.Logger import Logging_class


class Test_User_Profile:
    LoginUrl = Readconfig.getLoginUrl()
    RegistrationUrl = Readconfig.getRegistrationUrl()
    User_email = Readconfig.getUser_email()
    Password = Readconfig.getPassword()
    log = Logging_class.log_generator()

    def test_UserRegistration_001(self, setup):
        self.log.info("Opening test_UserRegistration_001")
        # 1 Browser Open
        self.driver = setup
        self.log.info("Opening Browser")
        # 2 Go to registration url
        self.driver.get(self.RegistrationUrl)
        # 3 Enter Name
        self.ur = UserProfile_Class(self.driver)
        self.ur.Enter_Name("Kunal")
        self.log.info("Entering Name")
        # 4 Enter EMail Id
        email = Generate_Email()
        self.ur.Enter_Email(email)
        self.log.info("Entering Email" + email)
        # 5 Enter Password
        self.log.info("Entering Password")
        self.ur.Enter_Password("kunal@123")
        # 6 Enter Confirm Password
        self.log.info("Entering Confirm Password")
        self.ur.Enter_Confirmpassword("kunal@123")
        # 7 Click on Register button
        self.log.info("Clicking on Register button")
        self.ur.Click_RegisterButton()

        # 7 Validate Registration
        if self.ur.Validate_Login_Or_Registration() == "Registration Pass":
            self.log.info("Test_UserRegistration_001 is Pass")
            self.driver.save_screenshot(
                "C:\\Users\\KUNAL\\Desktop\\CT#10\\NEW REVISION 2023\\Scripts\\PytestFramework\\ScreenShots\\Registration_Pass.png")

            assert True
        else:
            self.log.info("Test_UserRegistration_001 is Fail")
            self.driver.save_screenshot(
                "C:\\Users\\KUNAL\\Desktop\\CT#10\\NEW REVISION 2023\\Scripts\\PytestFramework\\ScreenShots\\Registration_Fail.png")

            assert False


    def test_case_UserLogin_002(self, setup):
        # 1 Browser Open
        self.driver = setup
        # 2 Go to Url https://automation.credence.in/login
        self.driver.get(self.LoginUrl)
        self.ur = UserProfile_Class(self.driver)
        # 3 Enter email
        self.ur.Enter_Email(self.User_email)
        # 4 Enter Password
        self.ur.Enter_Password(self.Password)
        # 5 Click on Login button
        self.ur.Click_LoginButton()
        # 6 Validate Login
        if self.ur.Validate_Login_Or_Registration() == "Registration Pass":
            self.driver.save_screenshot(
                "C:\\Users\\KUNAL\\Desktop\\CT#10\\NEW REVISION 2023\\Scripts\\PytestFramework\\ScreenShots\\Login_Pass.png")

            assert True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\KUNAL\\Desktop\\CT#10\\NEW REVISION 2023\\Scripts\\PytestFramework\\ScreenShots\\Login_Fail.png")

            assert False

def Generate_Email():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    domain = random.choice(['gmail.com','ymail.com','outlook.com'])
    return f"{username}@{domain}"