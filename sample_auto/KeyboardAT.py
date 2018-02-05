# -*- coding: UTF-8 -*-

import pyautogui as gui
from pywinauto import application
import time

# Win32 API(Default)
app = application.Application(backend="win32") 
app.start("notepad.exe")

# 指定された文字列の key を press
gui.typewrite("Hello Python world!",0.25)
gui.typewrite("\n")

gui.typewrite(["P","y","t","h","o","n"],0.25)
gui.typewrite("\n")

# KeyDownとKeyUpとpress
gui.keyDown("shift")
gui.keyDown("p")
gui.keyUp("shift")
gui.keyUp("p")
gui.press('enter')
