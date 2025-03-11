class MessageEventRegistry:
    def __init__(self):
        self.functions = []  # 存储注册的函数

    def register(self, func, command=""):
        """ 注册一个函数 """
        if callable(func):
            self.functions.append((command,func))
        else:
            raise ValueError("必须是可调用的函数")

    def execute_message_event(self,command,message):
        """ 执行所有注册过的函数 """
        for func in self.functions:
            if func[0] == command:
                func[1](message)  # 调用每个注册的函数
            if func[0] == "":
                func[1](message)


MessageEvent = MessageEventRegistry()  # 创建 registry 实例