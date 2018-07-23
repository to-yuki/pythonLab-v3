# -*- coding: UTF-8 -*-

from datetime import datetime
from subprocess import Popen
from pywinauto import application , Desktop
from time import sleep

Popen('calc.exe', shell=True)
dlg = Desktop(backend="uia").Calculator
print(dlg)
#dlg.type_keys('2*3=')
dlg.print_control_identifiers()

