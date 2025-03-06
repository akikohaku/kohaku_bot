import utils.screenshot as screenshot
import image_process.process as imageProcess
import image_process.ocr as imageOcr
import utils.operator as operator
import api.MessageSender as MessageSender
import api.MessageReader as MessageReader
import api.Notification as Notification

imageOcr.init()
print("initialed")

BotName="小琥珀"


#MessageSender.send_message("琥珀","在干嘛")
message=MessageReader.read_last_message("琥狐泊")
print(message)
atlist=MessageReader.get_at_message(message,BotName)
print(atlist)
NotificationList=Notification.get_notifications()
print(Notification)
for notification in NotificationList:
    message=MessageReader.read_last_message(notification)
    print(message)
    atlist=MessageReader.get_at_message(message,BotName)
    print(atlist)

