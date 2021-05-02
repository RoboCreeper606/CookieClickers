class Text:
    def __init__(self, font, text, color, x, y):
        self.__img = font.render(text, True, color)
        self.color = color
        self.__font = font
        self.__x = x
        self.__y = y

    def changeText(self, new_text):
        self.__img = self.__font.render(new_text, True, self.color)

    def getSprite(self):
        return self.__img

    def getXY(self):
        return self.__x, self.__y