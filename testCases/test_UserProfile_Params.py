from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.UserProfilePage import UserProfile_Class
from utilities.readproperties import Readconfig


class Test_User_Profile_Params:
    LoginUrl = Readconfig.getLoginUrl()
    RegistrationUrl = Readconfig.getRegistrationUrl()
    User_email = Readconfig.getUser_email()
    Password = Readconfig.getPassword()

    # def test_UserRegistration_Params_004(self, setup):
    #     # 1 Browser Open
    #     self.driver = setup
    #     # 2 Go to registration url
    #     self.driver.get(self.RegistrationUrl)
    #     # 3 Enter Name
    #     self.ur = UserProfile_Class(self.driver)
    #     self.ur.Enter_Name("Kunal")
    #     # 4 Enter EMail Id
    #     self.ur.Enter_Email("kunaldeshmukh14@gmail.com")
    #     # 5 Enter Password
    #     self.ur.Enter_Password("kunal@123")
    #     # 6 Enter Confirm Password
    #     self.ur.Enter_Confirmpassword("kunal@123")
    #     # 7 Click on Register button
    #     self.ur.Click_RegisterButton()
    #
    #     # 7 Validate Registration
    #     if self.ur.Validate_Login_Or_Registration() == "Registration Pass":
    #         self.driver.save_screenshot(
    #             "C:\\Users\\KUNAL\\Desktop\\CT#10\\NEW REVISION 2023\\Scripts\\PytestFramework\\ScreenShots\\Registration_Pass.png")
    #
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             "C:\\Users\\KUNAL\\Desktop\\CT#10\\NEW REVISION 2023\\Scripts\\PytestFramework\\ScreenShots\\Registration_Fail.png")
    #
    #         assert False

    def test_case_UserLogin_params_005(self, setup, getDataForLogin):
        self.driver = setup
        self.driver.get(self.LoginUrl)
        self.ur = UserProfile_Class(self.driver)
        self.ur.Enter_Email(getDataForLogin[0])
        self.ur.Enter_Password(getDataForLogin[1])
        self.ur.Click_LoginButton()
        if self.ur.Validate_Login_Or_Registration() == "Registration Pass":
            if getDataForLogin[2] == 'Pass':
                self.driver.save_screenshot(
                    "C:\\Users\\KUNAL\\Desktop\\CT#10\\NEW REVISION 2023\\Scripts\\PytestFramework\\ScreenShots\\Login_Pass.png")

                assert True
            elif getDataForLogin[2] == "Fail":
                self.driver.save_screenshot(
                    "C:\\Users\\KUNAL\\Desktop\\CT#10\\NEW REVISION 2023\\Scripts\\PytestFramework\\ScreenShots\\Login_Pass.png")
                assert False

        else:##Login fail
            if getDataForLogin[2] == "Pass":
                self.driver.save_screenshot(
                    "C:\\Users\\KUNAL\\Desktop\\CT#10\\NEW REVISION 2023\\Scripts\\PytestFramework\\ScreenShots\\Login_Fail.png")
                assert False
            elif getDataForLogin[2] == "Fail":
                self.driver.save_screenshot(
                    "C:\\Users\\KUNAL\\Desktop\\CT#10\\NEW REVISION 2023\\Scripts\\PytestFramework\\ScreenShots\\Login_Fail.png")
                assert True
