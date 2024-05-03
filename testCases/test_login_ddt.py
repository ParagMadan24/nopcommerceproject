from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadProperties
from Utilities.excelReadtdata import XLread
import time
class Test_Login_ddt:
    base_url = ReadProperties.getbaseurl()
    path=".\\TestData\\test_data.xlsx"
    sheet='Sheet1'
    rows=XLread.noofrows(path,sheet)
    def test_login(self, setup):
        lst=[]
        for i in range(2, self.rows + 1):
            self.driver = setup
            self.driver.get(self.base_url)
            self.lp = LoginPage(self.driver)
            self.login_username = XLread.read_data(self.path,self.sheet,i,1)
            self.login_password = XLread.read_data(self.path,self.sheet,i,2)
            self.result = XLread.read_data(self.path,self.sheet,i,3)
            print(self.login_username,self.login_password)
            self.lp.enter_username(self.login_username)
            self.lp.enter_password(self.login_password)
            self.lp.click_submit()
            if self.driver.title== "Dashboard / nopCommerce administration":
                self.driver.close()
                if self.result=="Pass":
                    lst.append("Pass")
                else:
                    lst.append("Fail")
            else:
                if self.result=="Fail":
                    lst.append("Pass")
                else:
                    lst.append("Fail")
            time.sleep(5)
            self.driver.close()
        assert "Fail" not in lst
