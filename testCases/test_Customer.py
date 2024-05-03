from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadProperties
from pageObjects.CustomerSearchPage import CustomerSearchPage
from pageObjects.addCustomerPage import addNewCustomer
import time
import random
import string
class Test_Customer:
    base_url = ReadProperties.getbaseurl()
    username = ReadProperties.geturename()
    passw = ReadProperties.getpassword()
    def test_add_customer(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        lp=LoginPage(driver=self.driver)
        cp = addNewCustomer(driver=self.driver)
        lp.enter_username(username=self.username)
        lp.enter_password(password=self.passw)
        lp.click_submit()
        time.sleep(5)
        cp.click_customer_menu()
        time.sleep(4)
        cp.click_sub_customer_menu()
        tesdata=random_string_generator()
        email_reg = tesdata+"@gmail.com"
        cp.enter_email(email_reg)
        cp.enter_first_name(tesdata)
        cp.enter_last_name(tesdata)
        cp.select_dob("5","17")
        time.sleep(5)
def random_string_generator(lenght=8):
    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k=lenght))
    return res