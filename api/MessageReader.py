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
    messageList=[]
    if len(messageLocation) is 0:
        return messageList
    messageLocation[0][0]+=380
    messageLocation[0][1]+=200
    operator.click(messageLocation)
    time.sleep(2.5)
    image=process.get_dialogueArea()
    validRegion=process.split_image(image,241,241,241)
    
    for idx, (start, end) in enumerate(validRegion):
        cropped_img = image[start:end + 1, :]
        #cv2.imwrite(f"{idx}.png", cropped_img)
        if process.isFullDialogue(cropped_img):
            IDimage=process.get_IDContent(cropped_img)
            #IDimage=process.enhanceID(IDimage)
            OcrID=imageOcr.get_messageList(IDimage)
            if OcrID[0] is None:
                continue
            OcrMessage=imageOcr.get_messageList(process.get_DialogueContent(cropped_img))
            if OcrMessage[0] is None:
                continue
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

def get_specific_message(messageList,Target):
    result = [item for item in messageList if Target in item[1]]
    return result

def get_at_message(messageList,Name):
    target="@"+Name
    result = get_specific_message(messageList,target)
    return result