from selenium.webdriver.common.by import By
class LoginPage:
    email_username_name = "Email"
    email_username_pass_id = "Password"
    submit_button_xpath = "//*[@type='submit']"
    logout_link_text = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.email_username_name).clear()
        self.driver.find_element(By.NAME,self.email_username_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.email_username_pass_id).clear()
        self.driver.find_element(By.ID,self.email_username_pass_id).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.XPATH,self.submit_button_xpath).click()

    def logout_click(self):
         self.driver.find_element(By.LINK_TEXT,self.logout_link_text).click()
         self.driver.close()