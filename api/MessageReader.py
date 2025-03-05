import image_process.process as process
import image_process.ocr as imageOcr
import utils.operator as operator
import utils.screenshot as screenshot
import cv2
import time

def read_last_message(targerName):
    messageArea=process.get_messageArea()
    messageList=imageOcr.get_messageList(messageArea)
    messageLocation=imageOcr.get_messageLoaction(messageList,targerName)
    messageLocation[0][0]+=220
    messageLocation[0][1]+=200
    operator.click(messageLocation)
    time.sleep(0.5)
    image=process.get_dialogueArea()
    validRegion=process.split_image(image)
    messageList=[]
    for idx, (start, end) in enumerate(validRegion):
        cropped_img = image[start:end + 1, :]
        #cv2.imwrite(f"{idx}.png", cropped_img)
        if process.isFullDialogue(cropped_img):
            IDimage=process.get_IDContent(cropped_img)
            #IDimage=process.enhanceID(IDimage)
            OcrID=imageOcr.get_messageList(IDimage)
            OcrMessage=imageOcr.get_messageList(process.get_DialogueContent(cropped_img))
            #print(OcrID)
            UserIDOutcome = [detection[1][0] for line in OcrID for detection in line]
            UserID=""
            for idx in range(len(UserIDOutcome)):
                UserID+=UserIDOutcome[idx] 
            MessageOutcome = [detection[1][0] for line in OcrMessage for detection in line]
            Message=""
            for idx in range(len(MessageOutcome)):
                Message+=MessageOutcome[idx]
            #print(UserID,Message)
            messageList.append((UserID,Message))
    operator.back()
    return messageList
