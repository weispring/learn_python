from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = None
try:
    # 需要先下载浏览器驱动 鼠标、键盘
    chromedriver = "D:\dependenc\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)

    driver.get("https://www.baidu.com/")

    h = driver.current_window_handle

    print(h)  # 打印首页句柄
    # 获取dom 元素api
    search = driver.find_element_by_id("kw")
    #search.send_keys("webdriver" + Keys.ENTER)
    action = webdriver.ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys("a").perform()
    # Enters text "qwerty" with keyDown SHIFT key and after keyUp SHIFT key (QWERTYqwerty)
    action.key_down(Keys.SHIFT).send_keys_to_element(search, "qwerty").key_up(Keys.SHIFT).send_keys("qwerty").perform()

    # Clears the entered text
    search.clear()
    print(search)
    # 获取当前的handle名字
    handle = driver.current_window_handle
    print("当前的handle：" ,handle)
finally:
    driver.quit()