#!/usr/bin/python
import time
import os
import sys 

#Se obtiene la fecha y hora
fyh = time.strftime("%c")

#Se abre el archivo 
f = open('/home/pi/Estufa/index.html','+')

# Se lee el archivo
linea = f.readline()

#Se encuentra la linea donde se especifica la fecha y hora, y se actualiza
while linea != '':
	if linea == '				<!-- FECHA Y HORA -->':
		linea = f.readline()
		f.write('				<font size="30%">%c</font>'%(fyh))
		linea = ''

#Se cierra el archivo
f.close()



#Se ejecutan comandos de git, para actualizar la informacion
#os.system('cd ~/Estufa')
#os.system('git add -A')
#os.system('git commit -m "%s"'%(fyh))
