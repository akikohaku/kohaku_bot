import os

def get_screenshot():
    os.system("adb shell screencap -p /sdcard/screencap.png")
    os.system("adb pull /sdcard/screencap.png")
    return "screencap.png"