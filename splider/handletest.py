from selenium import webdriver
driver = None
try:
    # 需要先下载浏览器驱动 鼠标、键盘
    chromedriver = "D:\dependenc\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)

    driver.get("http://bj.ganji.com/")

    h = driver.current_window_handle

    print(h)  # 打印首页句柄
    # 获取dom 元素api
    div = driver.find_element_by_class_name("enterprise-list")
    div.click()

    all_h = driver.window_handles

    print(all_h)     # 打印所有的句柄
    driver.switch_to.window(all_h[1])
    print(driver.title)
    # 关闭新窗口
    driver.close()
    # 切换到首页句柄
    driver.switch_to.window(h)
    # 打印当前的title
    print(driver.title)

    # driver.get("https://www.baidu.com")

    # 获取当前的handle名字
    handle = driver.current_window_handle
    print("当前的handle：" ,handle)
finally:
    driver.quit()