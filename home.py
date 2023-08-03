from chatlog import ChatLog

class Home:
    pass

    def __init__(self, biome, camp):
        self.biome = biome
        self.camp = camp
        text = f"made camp at {self.biome} in a {self.camp}"
        chat_instance = ChatLog()
        chat_instance.speak(text)

biome_list = ["forest", "mountain", "grassland", "swamp", "wasteland"]
# desert, canyon, cave, meadow, snowy plain etc.

camp_type = ["tent", "wagon"]




