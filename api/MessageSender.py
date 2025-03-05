import image_process.process as process
import image_process.ocr as imageOcr
import utils.operator as operator

def send_message(targerName,content):
    messageArea=process.get_messageArea()
    messageList=imageOcr.get_messageList(messageArea)
    messageLocation=imageOcr.get_messageLoaction(messageList,targerName)
    messageLocation[0][0]+=220
    messageLocation[0][1]+=200
    operator.click(messageLocation)
    operator.send_message(content)
    operator.back()