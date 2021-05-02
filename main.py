import sys
import threading
import time

import pygame
pygame.init()

from display import Display
display = Display()

from entity import Entity

from text import Text

# Variables
cookiecount = 0
clickadder = 1
cps = 0

# On Clicks
def empty(entity):
    return

def onclicks_cookieclick(entity):
    global cookiecount
    cookiecount += clickadder
    entity.setXY(entity.getXY()[0], 169)
    cookie_counttext.changeText(str(cookiecount) + " cookies")
    cookie_multtext.changeText("Ran")

    def addcps():
        global cps, cookie_multtext
        cps += 1
        cookie_multtext.changeText(str(cps) + " CPS")
        time.sleep(1)
        cps -= 1
        cookie_multtext.changeText(str(cps) + " CPS")

    x = threading.Thread(target = addcps, args=())
    x.start()

cookie = Entity("sprites/Cookie.png", 256, 269, 169, onclicks_cookieclick)
cookieMovingUp = False
cookieMoveSpeed = 2
cookie_shadow = Entity("sprites/CookieShadow.png", 128, 269 + 15, 169 + 15, empty)

display.add_entity(cookie_shadow)
display.add_entity(cookie)


pygame.display.set_caption("Heyy")
def minecraftia(fontsize):
    return pygame.font.Font("fonts\Minecraftia-Regular.ttf", fontsize)

cookie_counttext = Text(minecraftia(48), "", (207, 155, 0), 50, 0)
cookie_multtext = Text(minecraftia(28), f"Current Multiplier: {cps}", (207, 155, 0), 50, 80)
display.add_text(cookie_counttext)
display.add_text(cookie_multtext)
cookie_counttext.changeText(str(cookiecount) + " cookies")

print(pygame.font.get_fonts())

while True:
    # Move the cookie
    if cookie.getXY()[1] < 120:
        cookieMovingUp = False
    if cookie.getXY()[1] > 169:
        cookieMovingUp = True

    #print(f"cookie moving up is {cookieMovingUp}")

    cookie_shadow.setXY(((cookie.getXY()[1] - 169) * 0.5) + 269, abs((cookie.getXY()[1] - 169) * 0.05) + 169)
    cookie_shadow.setOpacity((((cookie_shadow.getXY()[0] - 245) / 24) * 256) - 50)

    if cookieMovingUp:
        cookie.setXY(cookie.getXY()[0], cookie.getXY()[1] - (0.05 * cookieMoveSpeed))
    else:
        cookie.setXY(cookie.getXY()[0], cookie.getXY()[1] + (0.05 * cookieMoveSpeed))

    #print(((cookie_shadow.getXY()[0] - 245) / 24) * 256)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    display.update()