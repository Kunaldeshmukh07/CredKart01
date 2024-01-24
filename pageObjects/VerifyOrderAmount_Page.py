from selenium.webdriver.common.by import By


class VerifyOrderAmount_Class:

    Click_Macbook_XPATH = (By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']")
    Click_AddToCart_XPATH = (By.XPATH,"//input[@value='Add to Cart']")
    Click_ContinueShopping_XPATH = (By.XPATH,"//a[@class='btn btn-primary btn-lg']")
    Click_AppleIpad_XPATH = (By.XPATH,"//h3[normalize-space()='Apple iPad Retina']")
    Click_HeadPhone_XPATH = (By.XPATH,"//h3[normalize-space()='Headphones']")
    # Dropdown_XPATH = (By.XPATH,"//")

    def __init__(self,driver):
        self.driver = driver

    def Click_Macbook(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_Macbook_XPATH).click()

    def Click_AddToCart(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_AddToCart_XPATH).click()

    def Click_AppleIpad(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_AppleIpad_XPATH).click()

    def Click_ContinueShopping(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_ContinueShopping_XPATH).click()

    def Click_HeadPhone(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_HeadPhone_XPATH).click()

    def Check_Amount(self):
        l = len(self.driver.find_elements(By.CSS_SELECTOR, "tbody tr"))
        # print(l)
        Price_List = []
        for r in range(1, l - 2):
            Var = self.driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(" + str(r) + ") td:nth-child(4)").text
            Product_Price = (Var[1:])
            Price_List.append(float(Product_Price))

        var2 = sum(Price_List)
        Exp_SubTotal = round(var2, 2)
        # print(Exp_SubTotal)
        Exp_Tax = round((Exp_SubTotal * 0.13), 2)
        # print(Exp_Tax)
        Exp_Total = Exp_SubTotal + Exp_Tax
        # print(Exp_Total)

        Amount_List = []
        for r in range(l - 2, l + 1):
            Var = self.driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(" + str(r) + ") td:nth-child(4)").text
            # print(Var)
            var2 = (Var[1:])
            Amounts = var2.replace(',', '')
            # Amount_List.append(Amounts)
            Amount_List.append(float(Amounts))

        Act_SubTotal = Amount_List[0]
        # print(Act_SubTotal)
        Act_Tax = Amount_List[1]
        # print(Act_Tax)
        Act_Total = Amount_List[2]
        # print(Act_Total)

        if Exp_SubTotal == Act_SubTotal and Exp_Tax == Act_Tax and Exp_Total == Act_Total:
            print("Subtotal is matched")
            return "Amount is Matched"
        else:
            print("Subtotal is wrong")
            return "Amount is Not Matched"



