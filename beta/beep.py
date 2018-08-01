print("\007") #Windows Beep!

from pyfiglet import Figlet
f = Figlet(font="slant")
msg = f.renderText("Python")
print(msg)