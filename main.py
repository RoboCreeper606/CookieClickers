import math
import sys
import threading
import time

import pygame
pygame.init()

from display import Display
display = Display()

from entity import Entity

from text import Text

# consts
CookieX = 380
CookieY = 140

# Variables
cookiecount = 0
clickadder = 1
clicksps = 0
cookiesps = 0

clickadder_price = 5
cookiespsadder_price = 10
clicksmultiplier_price = 50
cookiesmultiplier_price = 100

resetprices_price = 100000

# On hover
def onhover_cookieclick(entity):
    pass

# On Clicks

def onlick_resetprices(entity):
    global cookiecount, resetprices_price, clickadder_price, cookiespsadder_price, clicksmultiplier_price, cookiesmultiplier_price
    if cookiecount >= resetprices_price:
        clickadder_price = 5
        cookiespsadder_price = 10
        clicksmultiplier_price = 50
        cookiesmultiplier_price = 100
        cookiecount -= resetprices_price
        resetprices_price *= 100


def onclick_cookiespsdouble(entity):
    global cookiesps, cookiecount, cookiesmultiplier_price
    if cookiecount >= cookiesmultiplier_price:
        cookiecount -= cookiesmultiplier_price
        cookiesmultiplier_price *= 5
        cookiesps *= 2

def onclick_cpsdouble(entity):
    global clickadder, cookiecount, clicksmultiplier_price
    if cookiecount >= clicksmultiplier_price:
        cookiecount -= clicksmultiplier_price
        clicksmultiplier_price *= 2
        clickadder *= 2

def onclicks_cpsadder(entity):
    global cookiesps, cookiecount,  cookiespsadder_price
    if cookiecount >= cookiespsadder_price:
        cookiecount -= cookiespsadder_price
        cookiesps += 5
        cookiespsadder_price *= 1.1
        cookiespsadder_price = math.floor(cookiespsadder_price)

def onclicks_multiplier(entity):
    global clickadder, cookiecount, clickadder_price
    if cookiecount >= clickadder_price:
        cookiecount -= clickadder_price
        clickadder_price *= 1.5
        clickadder_price = math.floor(clickadder_price)
        clickadder += 1


def onclicks_cookieclick(entity):
    global cookiecount
    cookiecount += clickadder
    entity.setXY(entity.getXY()[0], CookieY)

    def addcps():
        global clicksps, cookie_multtext
        clicksps += 1
        time.sleep(1)
        clicksps -= 1

    x = threading.Thread(target = addcps, args=())
    x.start()

cookie = Entity("sprites/Cookie.png", 256, CookieX, CookieY, **{"onClick": onclicks_cookieclick})
cookieMovingUp = False
cookieMoveSpeed = 2
cookie_shadow = Entity("sprites/CookieShadow.png", 128, CookieX + 15, CookieY + 15)

clickspsincrease = Entity("sprites/ClickMult+1.png", 256 , 10, 200, **{"onClick": onclicks_multiplier})
cookiespsincrease = Entity("sprites/CookiesPS+1.png", 256, 10, 300, **{"onClick": onclicks_cpsadder})
cookiespsdouble = Entity("sprites/ClickMultX2.png", 256, 10, 400, **{"onClick": onclick_cpsdouble})
clickspsdouble = Entity("sprites/CookiesPSX2.png", 256, 10, 500, **{"onClick": onclick_cookiespsdouble})
resetprices = Entity("sprites/ResetPrices.png", 256, 520, 410, **{"onClick": onlick_resetprices})


display.add_entity(clickspsincrease)
display.add_entity(cookiespsdouble)
display.add_entity(clickspsdouble)
display.add_entity(cookiespsincrease)
display.add_entity(cookie_shadow)
display.add_entity(cookie)
display.add_entity(resetprices)


pygame.display.set_caption("Cookie Clicker Game")

def minecraftia(fontsize):
    return pygame.font.Font("fonts\Minecraftia-Regular.ttf", fontsize)

cookie_counttext = Text(minecraftia(48), "", (207, 155, 0), 10, 0)
cookie_multtext = Text(minecraftia(28), str(clicksps) + " Clicks Per Second", (207, 155, 0), 10, 80)

clicksps_price = Text(minecraftia(20), str(clickadder_price) + " cookies", (20, 240, 20), 20, 230)
cookiesps_price = Text(minecraftia(20), str(cookiespsadder_price) + " cookies", (20, 240, 20), 20, 330)
cookiesperclickx2_price = Text(minecraftia(20), str(clicksmultiplier_price) + " cookies", (20, 240, 20), 20, 430)
cookiespsx2_price = Text(minecraftia(20), str(cookiesmultiplier_price) + " cookies", (20, 240, 20), 20, 530)

cookiesps_text = Text(minecraftia(28), str(cookiesps) + "Cookies Per Second", (207, 155, 0), 10, 140)

resetprices_text = Text(minecraftia(32), str(resetprices_price), (20, 240, 20), 500, 530)

click_multiplier = Text(minecraftia(28), str(clickadder) + " Cookies Per Click", (207, 155, 0), 10, 110)

display.add_text(cookie_counttext)
display.add_text(cookie_multtext)
display.add_text(clicksps_price)
display.add_text(click_multiplier)
display.add_text(cookiesps_price)
display.add_text(cookiesps_text)
display.add_text(cookiesperclickx2_price)
display.add_text(cookiespsx2_price)
display.add_text(resetprices_text)

# Update ClicksPerSecond
def update_everything():
    cookie_counttext.changeText(str(math.floor(cookiecount)) + " cookies")
    cookie_multtext.changeText(str(clicksps) + " Clicks Per Second")
    click_multiplier.changeText(str(clickadder) + " Cookies Per Click")
    cookiesps_text.changeText(str(cookiesps) + " Cookies Per Second")

    clicksps_price.changeText(str(clickadder_price) + " cookies")
    cookiesps_price.changeText(str(cookiespsadder_price) + " cookies")
    cookiesperclickx2_price.changeText(str(clicksmultiplier_price) + " cookies")
    cookiespsx2_price.changeText(str(cookiesmultiplier_price) + " cookies")

    resetprices_text.changeText(str(resetprices_price))

def addcookiesps():
    global cookiecount
    while True:
        cookiecount += cookiesps/100
        time.sleep(0.01)

x = threading.Thread(target = addcookiesps)
x.start()

while True:
    update_everything()

    # Move the cookie
    if cookie.getXY()[1] < 120:
        cookieMovingUp = False
    if cookie.getXY()[1] > CookieY:
        cookieMovingUp = True

    cookie_shadow.setXY(((cookie.getXY()[1] - CookieY) * 0.5) + CookieX, abs((cookie.getXY()[1] - CookieY) * 0.05) + CookieY)
    cookie_shadow.setOpacity((((cookie_shadow.getXY()[0] - CookieX + 24) / 24) * 256) - 50)

    if cookieMovingUp:
        cookie.setXY(cookie.getXY()[0], cookie.getXY()[1] - (0.05 * cookieMoveSpeed))
    else:
        cookie.setXY(cookie.getXY()[0], cookie.getXY()[1] + (0.05 * cookieMoveSpeed))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.update()