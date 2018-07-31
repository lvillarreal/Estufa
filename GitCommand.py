#!/usr/bin/python
import time
import os
import sys 

#Se obtiene la fecha y hora
fyh = time.strftime("%c")

#Se ejecutan comandos de git, para actualizar la informacion
os.system('cd ~/Estufa')
os.system('git add -A')
os.system('git commit -m "%s"'%(fyh))
os.system('git push origin gh-pages')
