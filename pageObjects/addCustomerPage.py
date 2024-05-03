from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class addNewCustomer:
    add_new_css_selector = "//*[@href='/Admin/Customer/Create']"
    email_locate_by_Xpath = "//*[@id='Email']"
    password_locator_by_css_s = "#Password"
    firstname_xpath = "//*[@id='FirstName']"
    lastname_xpath = "//*[@id='LastName']"
    gender_locate_by_id_M = "Gender_Male"
    gender_locate_by_id_F = "Gender_Female"
    save_button_locator_css = "[name='save']"
    success_message_xpath = "//div[contains(@class,'alert alert-success alert-dismissable')]"
    failire_message_xpath = "//div[contains(@class,'alert alert-danger alert-dismissable')]"
    customersmenu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    customer_menu2_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    custom_role_cluse_button_xpath = "//li/span[@title='delete']"
    custom_role_input_xpath = "//div[@class='input-group']//following::span[@class='select2-selection__choice__remove']"
    select_xpath_customer_role = "//li[contains(text(),'Guests')]"
    alert_text_xpath = "//div[contains(@class,'alert')]"
    def __init__(self, driver):
        self.driver = driver
    def click_customer_menu(self):
        self.driver.find_element(By.XPATH,self.customersmenu_xpath).click()
    def click_sub_customer_menu(self):
        self.driver.find_element(By.XPATH, self.customer_menu2_xpath).click()
    def click_add_new_button(self):
        self.driver.find_element(By.XPATH,self.add_new_css_selector).click()
    def enter_email(self, email):
        self.driver.find_element(By.XPATH,self.email_locate_by_Xpath).send_keys(email)
    def enter_password(self, passwd):
        self.driver.find_element(By.CSS_SELECTOR,self.password_locator_by_css_s).send_keys(passwd)
    def enter_firstname(self, firstname):
        self.driver.find_element(By.XPATH,self.firstname_xpath).send_keys(firstname)
    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH,self.lastname_xpath).send_keys(lastname)
    def select_gender(self, gender):
        if gender == "M":
            self.driver.find_element(By.ID, self.gender_locate_by_id_M).click()
        else:
            self.driver.find_element(By.ID, self.gender_locate_by_id_F).click()
    def add_customer_role(self,role):
        #self.driver.find_element(By.XPATH,self.custom_role_cluse_button_xpath).click()
        self.driver.find_element(By.XPATH,self.custom_role_input_xpath).click()
        #select = Select(self.driver.find_element(By.XPATH,self.select_xpath_customer_role))
        #select.select_by_visible_text("Guests")

    def get_alert_text(self):
        return self.driver.find_element(By.XPATH,self.alert_text_xpath).text
    def save_button_click(self):
        self.driver.find_element(By.CSS_SELECTOR,self.save_button_locator_css).click()

    def get_success_message(self):
        return self.driver.find_element(By.XPATH,self.success_message_xpath).text
    def get_failiure_message(self):
        return self.driver.find_element(By.XPATH,self.failire_message_xpath).text
