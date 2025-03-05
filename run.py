import utils.screenshot as screenshot
import image_process.process as imageProcess
import image_process.ocr as imageOcr
import utils.operator as operator
import api.MessageSender as MessageSender
import api.MessageReader as MessageReader

imageOcr.init()
print("initialed")


#MessageSender.send_message("琥珀","在干嘛")
MessageReader.read_last_message()
