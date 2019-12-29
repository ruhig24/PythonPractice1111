
import testdata.constants as dataVal
class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_txt_name='username'
        self.pwd_txt_name='pwd'
        self.logib_btn_xpath='//*[@id="loginButton"]/div'

    def enter_username(self):
        self.driver.find_element_by_name(self.username_txt_name).send_keys(dataVal.USERNAME)


    def enter_pwd(self):
        self.driver.find_element_by_name(self.pwd_txt_name).send_keys(dataVal.PASSWORD)


    def click_on_login(self):
        self.driver.find_element_by_xpath(self.logib_btn_xpath).click()


