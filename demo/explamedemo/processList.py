import wmi
import psutil


c = wmi.WMI()

for process in c.Win32_Process():
    p = psutil.Process(int(process.ProcessId))
    try:
        path = p.exe()
    except:
        path = "-"
    finally:
        print(path)