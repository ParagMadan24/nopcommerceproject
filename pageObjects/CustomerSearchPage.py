from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class CustomerSearchPage:
    customersmenu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    customer_menu2_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    add_new_xpath = "//*[@href='/Admin/Customer/Create']"
    email_by_id = "SearchEmail"
    username_by_id="SearchFirstName"
    lastname_by_xpath = "//div/input[@id='SearchFirstName']//ancestor::div[contains(@class,'form-group')]//following::input[@id='SearchLastName']"
    date_of_b_selectxpath_month = "//*[@id='SearchMonthOfBirth']"
    date_of_b_selectxpath_day = "//*[@id='SearchDayOfBirth']"
    search_button_id = "search-customers"
    email_value_row_xpath = "//table[@id='customers-grid']//following::tr/td[2]"
    name_value_row_xpath = "//table[@id='customers-grid']//following::tr/td[3]"
    def __init__(self,driver):
        self.driver = driver
    def click_customer_menu(self):
        self.driver.find_element(By.XPATH,self.customersmenu_xpath).click()
    def click_sub_customer_menu(self):
        self.driver.find_element(By.XPATH, self.customer_menu2_xpath).click()
    def enter_email(self,emailid):
        self.driver.find_element(By.ID,self.email_by_id).send_keys(emailid)
    def enter_first_name(self,first_name):
        self.driver.find_element(By.ID,self.username_by_id).send_keys(first_name)
    def enter_last_name(self,last_name):
        self.driver.find_element(By.XPATH, self.lastname_by_xpath).send_keys(last_name)
    def select_dob(self,month,day):
        select_month_class = Select(self.driver.find_element(By.XPATH,self.date_of_b_selectxpath_month))
        select_month_class.select_by_value(month)
        select_day_class = Select(self.driver.find_element(By.XPATH,self.date_of_b_selectxpath_day))
        select_day_class.select_by_visible_text(day)
    def click_search(self):
        self.driver.find_element(By.ID,self.search_button_id).click()

    def return_email_address_col_value(self):
        return self.driver.find_element(By.XPATH,self.email_value_row_xpath).text

    def return_name_col_value(self):
        return self.driver.find_element(By.XPATH, self.name_value_row_xpath).text
