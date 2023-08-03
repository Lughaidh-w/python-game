from chatlog import ChatLog

class Thing:
    def __init__(self, name):
        self.name = name
        text = f"Made a {name}, a type of {self.__class__.__name__}"
        chat_instance = ChatLog()
        #chat_instance.speak(text)
        chat_instance.speak(text)
