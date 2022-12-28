import re, os, requests, json
from requests import get

logo = ('''\033[1;97m
   ___  ____  ______  __________  _______
  / _ )/ __ \/_  __/ / __/  _/  |/  /  _/
 / _  / /_/ / / /   _\ \_/ // /|_/ // /  
/____/\____/ /_/   /___/___/_/  /_/___/  
''')

os.system('clear')
print(logo)
while True:
	mess = input("\033[1;97m(+) ketik pesan : ")
	if mess in ["STOP"]:exit()
	response = get(f'https://api.simsimi.net/v2/?text={mess}&lc=id')
	print('\033[1;97m(+) bot simisimi : ', response.json().get('success'))
		
		