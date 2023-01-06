import pandas as pd
from openpyxl import load_workbook
#import pywhatkit
path='pl.csv'

#https://web.whatsapp.com/send?phone=34687634068


import os

import time
import webbrowser as web
from datetime import datetime
from re import fullmatch
from typing import List
from urllib.parse import quote
import paperclip
import pyautogui as pg
import pyperclip
import keyboard
from pywhatkit.core import core, exceptions, log

pg.FAILSAFE = False

core.check_connection()

def sendwhatmsg_instantly(
        phone_no: str,
        message: str,
        wait_time: int = 5,
        tab_close: bool = True,
        close_time: int = 3,
) -> None:
    
    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
    time.sleep(4)
   
    time.sleep(wait_time - 4)
    pg.press("enter")
    log.log_message(_time=time.localtime(), receiver=phone_no, message=message)
    
    pyperclip.copy(message) #line in work
    print("Copied")
    time.sleep(1)

    keyboard.press("ctrl")
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release("ctrl")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(4)
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(1)
    pg.hotkey("ctrl","w")
    print("sending")





with open('telefonos.txt', 'r') as fichero:
    for linea in fichero:
        print("se esta imprimiendo esto",linea)
        time.sleep(2)
        
        sendwhatmsg_instantly(linea, "Hello")
        time.sleep(20)
       
"""
fichero = open('telefonos.txt')
lineas = fichero.readlines()
for linea in lineas:
    print(linea)
        
"""
fichero.close()

#sendwhatmsg_instantly("+34687634068", "Hello")

