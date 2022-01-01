from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = None
try:
    # 需要先下载浏览器驱动 鼠标、键盘
    chromedriver = "D:\dependenc\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://www.baidu.com/")

    loginBtn = driver.find_element_by_link_text("登录")


    webdriver.ActionChains(driver).context_click(loginBtn).perform()
    # Perform double-click action on the element
    webdriver.ActionChains(driver).double_click(loginBtn).perform()


    # Performs mouse move action onto the element
    webdriver.ActionChains(driver).move_to_element(loginBtn).perform()


finally:
    driver.quit()