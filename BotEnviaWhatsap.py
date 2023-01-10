import pandas as pd
from openpyxl import load_workbook
#import pywhatkit
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

#https://web.whatsapp.com/send?phone=34666555444    url para el envio de mensajes

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
    time.sleep(30)
   
    time.sleep(wait_time - 4)
    pg.press("enter")
    log.log_message(_time=time.localtime(), receiver=phone_no, message=message)
    
    pyperclip.copy(message) #line in work
    print("Copied")
    #time.sleep(1)
    #keyboard.press("ctrl")
    #keyboard.press("v")
    #keyboard.release("v")
    #keyboard.release("ctrl")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(4)
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(1)
    pg.hotkey("ctrl","w")
    print("sending")

fichero = open('telefonos.txt')
lineas = fichero.readlines()
for i in range(len(lineas)):
    s= lineas[i].split(',') #s separador en el txt            
    sendwhatmsg_instantly(s[0], s[1])  #se envian los datos al metodo para ser impreso
    print(s[0],s[1], end=" ") # imprime los telefonos primera columna
    time.sleep(20)

fichero.close()