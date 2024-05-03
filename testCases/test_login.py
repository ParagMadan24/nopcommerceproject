from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadProperties
class Test_Login:
    base_url = ReadProperties.getbaseurl()
    login_username = ReadProperties.geturename()
    login_password = ReadProperties.getpassword()

    def test_title(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        print(self.driver.title)
        if self.driver.title =="Your store. Login":
            self.driver.close()
            assert True
        else:
         self.driver.close()
         assert False


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.login_username)
        self.lp.enter_password(self.login_password)
        self.lp.click_submit()
        if self.driver.title== "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("\\Screenshots\\test_ss.png")
            assert False
