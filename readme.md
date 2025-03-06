# Kohaku Robot For QQ Android

一个既不高效也不快速的通过adb操作qq实现qq机器人的框架，正在开发中

### 目前可用特性

发送消息：
MessageSender.send_message(Target,Content)

读取指定对话的最近消息：
MessageReader.read_last_message(Target)
return messageList((UserID,Message))

获得当前有新消息的对话：
Notification.get_notifications()
return notificationList(UserID)

获取包含特定关键词的消息：
MessageReader.get_specific_message(messageList,Target)
return messageList((UserID,Message))

获取@消息：
MessageReader.get_at_message(messageList,Name):
return messageList((UserID,Message))