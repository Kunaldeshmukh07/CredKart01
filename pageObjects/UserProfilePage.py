from selenium.webdriver.common.by import By


class UserProfile_Class():
    Text_Name_ID = (By.ID, "name")
    Text_Email_ID = (By.ID, "email")
    Text_Password_ID = (By.ID, "password")
    Text_ConfirmPassword_ID = (By.ID, "password-confirm")
    Click_Register_XPATH = (By.XPATH, "//button[@type='submit']")
    Validate_CredKart_Text_XPATH = (By.XPATH, "//h2[normalize-space()='CredKart']")
    Click_LoginButton_CSS = (By.CSS_SELECTOR, "button[type='submit']")
    Validate_Login_Text_XPATH = (By.XPATH, "//h2[normalize-space()='CredKart']")

    def __init__(self, driver):
        self.driver = driver

    def Enter_Name(self, name):
        self.driver.find_element(*UserProfile_Class.Text_Name_ID).send_keys(name)

    def Enter_Password(self, password):
        self.driver.find_element(*UserProfile_Class.Text_Password_ID).send_keys(password)

    def Enter_Email(self, email):
        self.driver.find_element(*UserProfile_Class.Text_Email_ID).send_keys(email)

    def Enter_Confirmpassword(self, confirmpassword):
        self.driver.find_element(*UserProfile_Class.Text_ConfirmPassword_ID).send_keys(confirmpassword)

    def Click_RegisterButton(self):
        self.driver.find_element(*UserProfile_Class.Click_Register_XPATH).click()

    def Validate_Login_Or_Registration(self):
        try:
            self.driver.find_element(*UserProfile_Class.Validate_CredKart_Text_XPATH)
            return "Registration Pass"
        except:
            return "Registration Fail"

    def Click_LoginButton(self):
        self.driver.find_element(*UserProfile_Class.Click_LoginButton_CSS).click()



