import os, requests

logo = ('''\033[1;97m
   ___  ____  ______  __________  _______
  / _ )/ __ \/_  __/ / __/  _/  |/  /  _/
 / _  / /_/ / / /   _\ \_/ // /|_/ // /  
/____/\____/ /_/   /___/___/_/  /_/___/  
''')
os.system('clear')
print(logo)

while True:
    me = input('\033[1;97m(+) ketik pesan : ')
    url = f'https://api.simsimi.net/v2/?text={me}&lc=id'
    response = requests.get(url)
    if response.status_code == 200:
        print('\033[1;97m(+) bot simsimi : ', response.json().get('success'))
    else:
        print('bad request !')