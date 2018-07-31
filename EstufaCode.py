#!/usr/bin/python
import time
import os
import sys 

#Se obtiene la fecha y hora
fyh = time.strftime("%c")
print(fyh)
os.system('cd ~/Estufa')
os.system('git add -A')
os.system('git commit -m "%s"'%(fyh))
