import pyautogui
import pyperclip
import time


time.sleep(5)
print(pyautogui.position())
pyautogui.doubleClick(650, 450) # 已左上角为(0,0)
time.sleep(10)
content = "import win32api#先要安装pywin32，pip install pywin32" \
          "win32api.ShellExecute(0, 'open', r'D:\Program Files (x86)\Tencent\QQ\Bin\QQ.exe', '','',1)"

for s in content:
    print(s)
    pyperclip.copy(s)
    pyautogui.hotkey("ctrl", "v")