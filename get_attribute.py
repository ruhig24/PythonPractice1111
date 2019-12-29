from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)

# ele_val=driver.find_element_by_id("email").get_attribute("data-testid")
# print(ele_val)
# print(type(ele_val))

ele_val=driver.find_element_by_xpath("//*[@class='login_form_label_field']/div/a").text
print(ele_val)
print(type(ele_val))
