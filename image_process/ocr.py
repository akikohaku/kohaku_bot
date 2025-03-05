from pyautogui import *
import numpy as np
import cv2
from paddleocr import PaddleOCR, draw_ocr


def init():
    global ocr
    ocr = PaddleOCR(use_angle_cls=False,use_gpu=True, lang="ch",show_log=False) 

def get_messageList(image):
    result=ocr.ocr(image,cls=True)
    return result

def get_messageLoaction(OcrResult,name):
    poslist = [detection[0][0] for line in OcrResult for detection in line] #取top一个点的位置
    txtlist = [detection[1][0] for line in OcrResult for detection in line] 
 
    # 用list存文字与位置信息
    find_txt_pos = []
 
    items = 0
 
    if name == "":
        print("nothing to detect")
        return
    else:
        for i in range(len(poslist)):
            if txtlist[i] == name:
                find_txt_pos.append(poslist[i])
                items += 1
    if find_txt_pos.__len__==0:
        print("fail to detect")
        return 
    return find_txt_pos