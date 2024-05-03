from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadProperties
from pageObjects.addCustomerPage import addNewCustomer
import time
import random
import string
class Test_Customer:
    base_url = ReadProperties.getbaseurl()
    username = ReadProperties.geturename()
    passw = ReadProperties.getpassword()
    def test_add_customer_onlyemailfield(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        lp=LoginPage(driver=self.driver)
        acp = addNewCustomer(driver=self.driver)
        lp.enter_username(username=self.username)
        lp.enter_password(password=self.passw)
        lp.click_submit()
        time.sleep(5)
        acp.click_customer_menu()
        acp.click_sub_customer_menu()
        acp.click_add_new_button()
        tesdata = random_string_generator()
        email_reg = tesdata + "@gmail.com"
        time.sleep(4)
        acp.enter_email(email_reg)

        acp.save_button_click()
        time.sleep(5)
        msg = acp.get_success_message()
        lp.logout_click()
        assert "The new customer has been added successfully." in msg

    def test_add_customer_fieldmulti(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        lp=LoginPage(driver=self.driver)
        acp = addNewCustomer(driver=self.driver)
        lp.enter_username(username=self.username)
        lp.enter_password(password=self.passw)
        lp.click_submit()
        time.sleep(5)
        acp.click_customer_menu()
        acp.click_sub_customer_menu()
        acp.click_add_new_button()
        tesdata = random_string_generator()
        email_reg = tesdata + "@gmail.com"
        time.sleep(4)
        acp.enter_firstname(tesdata)
        acp.enter_password(passwd=tesdata)
        acp.select_gender("F")
        #acp.add_customer_role("Guests")
        acp.enter_email(email_reg)
        acp.save_button_click()
        alert_text = acp.get_success_message()
        print(alert_text)
        lp.logout_click()
        assert "The new customer has been added successfully." in str(alert_text)

    def test_straight_submit(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        lp=LoginPage(driver=self.driver)
        acp = addNewCustomer(driver=self.driver)
        lp.enter_username(username=self.username)
        lp.enter_password(password=self.passw)
        lp.click_submit()
        time.sleep(5)
        acp.click_customer_menu()
        acp.click_sub_customer_menu()
        acp.click_add_new_button()
        acp.save_button_click()
        alert_text = acp.get_failiure_message()
        print(alert_text)
        lp.logout_click()
        assert "Valid Email is required for customer to be in 'Registered' role" in str(alert_text)

def random_string_generator(lenght=8):
    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k=lenght))
    return res