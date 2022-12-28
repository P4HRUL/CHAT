import re, os, requests, json
from requests import get

logo = ('''\033[1;97m
   ___  ____  ______  __________  _______
  / _ )/ __ \/_  __/ / __/  _/  |/  /  _/
 / _  / /_/ / / /   _\ \_/ // /|_/ // /  
/____/\____/ /_/   /___/___/_/  /_/___/  
''')
def pesan():
	while True:
		os.system('clear')
		print(logo)
		mess = input("\033[1;97m(+) ketik pesan : ")
		response = get(f'https://api.simsimi.net/v2/?text={mess}&lc=id')
		print('\033[1;97m(+) simi bot : \033[1;92m', response.json().get('success'))
		
		
pesan()