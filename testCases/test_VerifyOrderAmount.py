import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.UserProfilePage import UserProfile_Class
from pageObjects.VerifyOrderAmount_Page import VerifyOrderAmount_Class
from utilities.readproperties import Readconfig


class Test_VerifyAmount:
    LoginUrl = Readconfig.getLoginUrl()
    RegistrationUrl = Readconfig.getRegistrationUrl()
    User_email = Readconfig.getUser_email()
    Password = Readconfig.getPassword()

    def test_VerifyAmount(self, setup):
        self.driver = setup
        self.up = UserProfile_Class(self.driver)
        self.voa = VerifyOrderAmount_Class(self.driver)
        self.driver.get(self.LoginUrl)
        self.up.Enter_Email(self.User_email)
        self.up.Enter_Password(self.Password)
        self.up.Click_LoginButton()

        self.voa.Click_Macbook()
        self.voa.Click_AddToCart()
        self.voa.Click_ContinueShopping()
        self.voa.Click_AppleIpad()
        self.voa.Click_AddToCart()
        self.voa.Click_ContinueShopping()
        self.voa.Click_HeadPhone()
        self.voa.Click_AddToCart()
        time.sleep(2)
        if self.voa.Check_Amount() == "Amount is Matched":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False

# pytest -v --html=HtmlReports/ChromeReport.html --browser chrome -n=3 --alluredir="C:\Users\KUNAL\Desktop\CT#10\NEW REVISION 2023\Scripts\PytestFramework\AllureReports"