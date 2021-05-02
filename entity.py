import pygame

class Entity:
    def __init__(self, sprite_path, opacity, x, y, onClick):
        self.pressed = False
        self.__sprite = pygame.image.load(sprite_path)
        self.__sprite.set_alpha(opacity)
        self.__x = x
        self.__y = y
        self.__width = self.__sprite.get_width()
        self.__height = self.__sprite.get_height()
        self.__onClick = onClick

    def setOpacity(self, new_opacity):
        self.__sprite.set_alpha(new_opacity)

    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def setSprite(self, new_sprite):
        self.__sprite = new_sprite

    def getXY(self):
        return self.__x, self.__y

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getSprite(self):
        return self.__sprite

    def clicked(self):
        print("Clicked ran")
        self.__onClick(self)