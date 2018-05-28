# -*- coding: UTF-8 -*-
from __future__ import with_statement
import pyautogui as gui
from time import sleep

with open("clicks.csv") as f:
    for line in f:
        line = line.strip()
        list = line.split(',')
        # マウスカーソルの移動
        gui.moveTo(int(list[0]),int(list[1]))
        #gui.click()
        gui.keyDown('ctrl')
        gui.keyUp('ctrl')
        # クリック間隔
        sleep(int(list[2]))

