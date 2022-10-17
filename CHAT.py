import os
import sys
import time

logo = ('''\033[1;97m
    ____  ____  ______   ________  _____  ______
   / __ )/ __ \/_  __/  / ____/ / / /   |/_  __/
  / __  / / / / / /    / /   / /_/ / /| | / /   
 / /_/ / /_/ / / /    / /___/ __  / ___ |/ /    
/_____/\____/ /_/     \____/_/ /_/_/  |_/_/    

(1) mulai chat 
(0) log out ( keluar )
 ''')

def x():
	os.system('clear')
	os.chdir('DATA')
	os.system('python run.py')
	

def masuk():
	os.system('clear')
	print(logo)
	pilih()
	
def pilih():
	pahrul = input('(+) choose : ')
	if pahrul == "":
		print ("")
		print ("(+) Ngetik Apaan Lu bangsad !!!")
		exit()
	elif pahrul == "1":
		x()
	elif pahrul == "0":
		exit()
	else:
		print ("")
		print ("(+) Ngetik Apaan Lu bangsad !!!")
		exit()
		
masuk()