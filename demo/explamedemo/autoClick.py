import pyautogui
import pyperclip
import time
time.sleep(5)
for s in range(0, 15):
    print(pyautogui.position())
    #pyautogui.leftClick(188, 575) # 已左上角为(0,0)
    #pyautogui.leftClick(237, 251) # 已左上角为(0,0)

    pyautogui.leftClick(240, 525) # 已左上角为(0,0)
    pyautogui.leftClick(273,233) # 已左上角为(0,0)
    time.sleep(3)