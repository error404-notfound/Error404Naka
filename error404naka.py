#!/usr/bin/env python
import random
import string
import smtplib
import os
from time import sleep
from getpass import getpass
from subprocess import call

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan  

def clear():
	os.system('clear')
	
def msms():
	clear()
	print ""+W+" "
	print """

     
'||''''|                                    ,          , 
 ||  .    ... ..  ... ..    ...   ... ..   /|   /\\   /| 
 ||''|     ||' ''  ||' '' .|  '|.  ||' '' / |  || || / | 
 ||        ||      ||     ||   ||  ||     __|_ || || __|_
.||.....| .||.    .||.     '|..|' .||.    ---- || || ----
                                            |  || ||   | 
                                           '-'  \\/   '-'                                           
	 

	"""

        print ""+T+" "
	phonelst = raw_input(color.UNDERLINE + 'Path De la lista:' + color.END) 
	phonelst = open(phonelst, 'rb')
        print ""+T+" "
	gmail = raw_input(color.UNDERLINE + 'Correo:' + color.END)
        print ""+T+" "
        fromname = '.' + ' ' + raw_input(color.UNDERLINE + 'Nombre que vera el objetivo:' + color.END)
        print ""+T+" "
	password = getpass(color.UNDERLINE + 'Password:' + color.END)
        o = smtplib.SMTP("smtp.gmail.com:587")
        o.starttls()
        o.login(gmail, password)

	message = raw_input(color.UNDERLINE + 'Mensaje:' + color.END)
        print ""+T+" "
	counter = input(color.UNDERLINE + '# de envios:' + color.END)
        print ""+T+" "
	for phone in phonelst:
		try:
			spam_msg = "De: {} \r\nPara: {} \r\n\r\n {}".format(fromname, phone, message)
			print (color.UNDERLINE + ''+G+'[+] Enviando...' + color.END)
			for i in range(counter):
			    o.sendmail(fromname, phone, spam_msg)
			sleep(0.004)
			print(phone)
			print (color.UNDERLINE + ''+G+'[+] Se ha enviando correctamente!' + color.END), counter ,(color.UNDERLINE + ''+G+'[*] messages!' + color.END)
			
		except:
			print("Algo esta mal. Porfavor resiva nuevamente la informacion")
			print("Tu informacion esta aqui:", " ", gmail, " ", password, " ", spam_msg)
			b = raw_input("Presiona enter para continuar")	
			msms()
			
def ssms():
	clear()
	print ""+B+" "
	print ("""
		-SMS Bomber Nakamura- 

'||''''|                                    ,          , 
 ||  .    ... ..  ... ..    ...   ... ..   /|   /\\   /| 
 ||''|     ||' ''  ||' '' .|  '|.  ||' '' / |  || || / | 
 ||        ||      ||     ||   ||  ||     __|_ || || __|_
.||.....| .||.    .||.     '|..|' .||.    ---- || || ----
                                            |  || ||   | 
                                           '-'  \\/   '-'                                        
	
[]Colombia[]                            []Puerto Rico[]
  @clarocolombia.com.co                   @vtexto.com
  @sms.tigo.com.co
  @movistar.com.co

[]Mexico[]                              []Nicaragua[]
  @txt.att.net                            @ideasclaro-ca.com
  @smsiusacell.com.mx
  @itelcel.com
  @msgnextel.com.mx

[]Argentina[]                           []Dominicana[]
  @sms.movistar.net.ar                    @digitextdm.com
  @sms.ctimovil.com.ar
  @alertas.personal.com.ar
  @sms.movistar.net.ar

[]Espana[]                              []Costa Rica[]                
  @movistar.net                            @sms.ice.cr
  @esendex.net

[]Panama[]
  @cwmovil.com

 Ejemplo numero@txt.att.net

	""")
	
	provider = raw_input(color.UNDERLINE + 'Provedor De telefonia:' + color.END)
        print ""+T+" "
	phone_num = raw_input(color.UNDERLINE + 'Numero de la Victima:' + color.END) + provider
        print ""+T+" "
	gmail = raw_input(color.UNDERLINE + 'Correo:' + color.END)
        print ""+T+" "
	password = getpass(color.UNDERLINE + 'Password:' + color.END)
	fromname = '.' + ' ' + raw_input(color.UNDERLINE + 'Nombre que vera el objetivo:' + color.END)

        o = smtplib.SMTP("smtp.gmail.com:587")
        o.starttls()
        o.login(gmail, password)
        
	print ""+T+" "
	message = raw_input(color.UNDERLINE + 'Mensaje>' + color.END)
        print ""+T+" "
	counter = input(color.UNDERLINE + '# de envios>' + color.END)
        print ""+T+" "
        spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(fromname, phone_num, message)
	print (color.UNDERLINE + ''+G+'[+] Enviando...' + color.END)
        for i in range(counter):
            o.sendmail(gmail, phone_num, spam_msg)
        sleep(0.004)
        print(phone_num)
	print (color.UNDERLINE + ''+G+'[+] Se ha enviando correctamente!' + color.END)
	
def menu():
	clear()
	print ""+O+" "
	print ("""
		
		""")
	print ""+P+" "
	print ("""
		


Yb        dP                 w            
 Yb  db  dP  .d88 8d8b 8d8b. w 8d8b. .d88 
  YbdPYbdP   8  8 8P   8P Y8 8 8P Y8 8  8 
   YP  YP    `Y88 8    8   8 8 8   8 `Y88 
                                     wwdP 



Este programa esta hecho con fines educativos
cualquier uso indebido sera responsabilidad
de quien lo utilice.

		""")
	print ""+C+" "	
	opcion = raw_input("Un Solo objetivo 'u' Varios objetivos 'm':")
	if opcion == "u":
		clear()
		ssms()
	elif opcion == "m":
		clear()
		msms()
	else:
		clear()
		print ""+R+" "
		print ("Oops! Insertatste una opcion invalida")
		p = raw_input("Presiona enter para continuar")	
		menu()	
			
			
			
menu()	

		
