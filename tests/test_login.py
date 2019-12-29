#
#
# import pytest
# from pages.loginpage import LoginPage
# import testdata.constants as dataVal
#
#
# @pytest.mark.usefixtures("test_setup")
# class TestLogin:
#
#     def test_login(self):
#         driver = self.driver
#         lp=LoginPage(driver)
#         lp.enter_username()
#         lp.enter_pwd()
#         lp.click_on_login()
#
#         driver.find_element_by_xpath("//*[@id='topnav']/tbody/tr[1]/td[5]/a/div[2]").click()
#
# #