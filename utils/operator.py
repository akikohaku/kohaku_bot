import os
import time


def click(point):
    os.system('adb shell input tap '+str(point[0][0])+' '+str(point[0][1]))

def click_xy(x,y):
    os.system('adb shell input tap '+str(x)+' '+str(y))


def back():
    os.system('adb shell input keyevent 4')

def input_text(text):
    os.system('adb shell am broadcast -a ADB_INPUT_TEXT --es msg \"'+text+'\"')

def send():
    os.system('adb shell input tap 987 2076')

def send_message(content):
    time.sleep(1)
    click_xy(200,2100)
    time.sleep(1)
    input_text(content)
    time.sleep(1)
    send()
    back()
