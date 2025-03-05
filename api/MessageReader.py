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
        cv2.imwrite(f"{idx}.png", cropped_img)
        if process.isFullDialogue(cropped_img):
            #OcrResult=imageOcr.get_messageList(cropped_img)
            OcrID=imageOcr.get_messageList(process.get_IDContent(cropped_img))
            OcrMessage=imageOcr.get_messageList(process.get_DialogueContent(cropped_img))
            print(OcrID)
            ID = [detection[1][0] for line in OcrID for detection in line][0] 
            print(ID)
            MessageOutcome = [detection[1][0] for line in OcrMessage for detection in line]
            Message=""
            for idx in range(len(MessageOutcome)):
                Message+=MessageOutcome[idx]
            print(Message)
            print("------------------------------\n")
    
