from selenium import webdriver

driver = webdriver.chrome("C:\Users\srini\PycharmProjects\selenium1\webdrivers\chromedriver.exe")
driver.set_page_load_timeout("10")
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("udemy")
driver.find_element_by_name("btnk").click()

element.close()
