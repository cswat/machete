#! usr/bin/env python3
# pulls some info from html
# namely sales rank, price, title, reviews, pages(?)

import bs4
import pyautogui as gui
import time

def get_html(subject_string, num_of_pages):
    time.sleep(2)
    for i in range(0,num_of_pages):
        attempts = 0
        nxtPage = gui.locateCenterOnScreen("nxtPage.png")
        while nxtPage == None:
            gui.scroll(-500)
            nxtPage = gui.locateCenterOnScreen("nxtPage.png")
            time.sleep(3)
            attempts += 1
            if attempts >= 8:
                print("Page not found.")
                quit()
        print("Page found.")
        gui.hotkey("ctrl", "s")
        time.sleep(.5)
        gui.typewrite(subject_string + "AMZNPage" + str(num_of_pages))
        gui.hotkey("enter")
        print("Page saved as " + subject_string + "AMZNPage" + str(num_of_pages))
        time.sleep(3)
        gui.click(nxtPage)
        time.sleep(1)
        
get_html("Romance", 5)
