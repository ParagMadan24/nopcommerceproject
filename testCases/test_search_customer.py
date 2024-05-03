from pageObjects.CustomerSearchPage import CustomerSearchPage
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadProperties
from pageObjects.addCustomerPage import addNewCustomer
import time
import random
import string
class TestSearch_Customer:
    base_url = ReadProperties.getbaseurl()
    username = ReadProperties.geturename()
    passw = ReadProperties.getpassword()
    def test_search_by_email(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        lp=LoginPage(driver=self.driver)
        acp = addNewCustomer(driver=self.driver)
        sp = CustomerSearchPage(self.driver)
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
        acp.enter_email(email_reg)
        acp.save_button_click()
        alert_text = acp.get_success_message()
        assert "The new customer has been added successfully." in str(alert_text)
        sp.enter_email(email_reg)
        sp.click_search()
        time.sleep(15)
        assert sp.return_email_address_col_value()==email_reg
        lp.logout_click()

    def test_search_by_name(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        lp=LoginPage(driver=self.driver)
        acp = addNewCustomer(driver=self.driver)
        sp = CustomerSearchPage(self.driver)
        lp.enter_username(username=self.username)
        lp.enter_password(password=self.passw)
        lp.click_submit()
        time.sleep(5)
        acp.click_customer_menu()
        acp.click_sub_customer_menu()
        acp.click_add_new_button()
        testdata = random_string_generator()
        email_reg = testdata + "@gmail.com"
        time.sleep(4)
        acp.enter_firstname(testdata)
        acp.enter_lastname(testdata)
        acp.enter_password(passwd=testdata)
        acp.select_gender("F")
        acp.enter_email(email_reg)
        acp.save_button_click()
        alert_text = acp.get_success_message()
        assert "The new customer has been added successfully." in str(alert_text)
        sp.enter_first_name(testdata)
        sp.click_search()
        time.sleep(15)
        assert sp.return_name_col_value()==testdata+" "+testdata
        lp.logout_click()

def random_string_generator(lenght=8):
    return ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k=lenght))
