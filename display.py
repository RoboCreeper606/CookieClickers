import pygame

import entity
import text

class Display:
    def __init__(self):
        self.__display = pygame.display.set_mode((800, 600))
        self.__entity_list = []
        self.__text_list = []

    def add_entity(self, Entity: entity):
        self.__entity_list.append(Entity)

    def add_text(self, Text: text):
        self.__text_list.append(Text)

    def getDisplay(self):
        return self.__display

    def getEntityList(self):
        return self.__entity_list

    def update(self):
        self.__display.fill((255, 255, 255))
        mouseX, mouseY = pygame.mouse.get_pos()

        for E in self.__entity_list:
            self.__display.blit(E.getSprite(), E.getXY())
            if pygame.mouse.get_pressed(3)[0]:
                if E.getXY()[0] < mouseX and mouseX < E.getWidth() + E.getXY()[0]:
                    if E.getXY()[1] < mouseY and mouseY < E.getHeight() + E.getXY()[1]:
                        if E.pressed:
                            pass
                        else:
                            E.pressed = True
                            E.clicked()
            else:
                E.pressed = False
            for T in self.__text_list:
                self.__display.blit(T.getSprite(), T.getXY())
        pygame.display.flip()
