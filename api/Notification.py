import image_process.process as process
import image_process.ocr as imageOcr
import utils.operator as operator
import utils.screenshot as screenshot
import cv2

def get_notifications():
    fullMessageArea=process.get_fullMessageArea()
    validRegion=process.split_image(fullMessageArea,255,255,255)
    notificationList=[]
    for idx, (start, end) in enumerate(validRegion):
        cropped_img = fullMessageArea[start:end + 1, :]
        
        height,width,_=cropped_img.shape
        dialogueArea=cropped_img[0:height-1,200:1080]
        
        if process.checkPixelColor(dialogueArea,247, 76, 48):
            nameArea=dialogueArea[0:68, 0:640]
            OcrID=imageOcr.get_messageList(nameArea)
            UserIDOutcome = [detection[1][0] for line in OcrID for detection in line]
            UserID=""
            for idx in range(len(UserIDOutcome)):
                UserID+=UserIDOutcome[idx] 
            print(UserID)
            notificationList.append(UserID)
    return notificationList