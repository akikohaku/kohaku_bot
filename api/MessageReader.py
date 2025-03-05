import image_process.process as process
import image_process.ocr as imageOcr
import utils.operator as operator
import utils.screenshot as screenshot
import cv2

def read_last_message():
    image=process.get_dialogueArea()
    validRegion=process.split_image(image)
    for idx, (start, end) in enumerate(validRegion):
        cropped_img = image[start:end + 1, :]
        OcrResult=imageOcr.get_messageList(cropped_img)
        print(start)
        print(end)
        print(OcrResult)
        print("------------------------------\n")
    
