from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = None

fromAddress = "深圳"
toAddress = "武汉"
departureTime = "2022-02-27";


try:
    # 需要先下载浏览器驱动 鼠标、键盘
    chromedriver = "D:\dependenc\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)

    driver.get("https://www.12306.cn/index/index.html")

    h = driver.current_window_handle

    print(h)  # 打印首页句柄
    # 获取dom 元素api
    fromStationText = driver.find_element_by_id("fromStationText")
    #search.send_keys("webdriver" + Keys.ENTER)
    action = webdriver.ActionChains(driver)


    action.click(fromAddress).__setattr__("value", fromAddress)




    # 获取当前的handle名字
    handle = driver.current_window_handle
    print("当前的handle：" ,handle)
finally:
    driver.quit()