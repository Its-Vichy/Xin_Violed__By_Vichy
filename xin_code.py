import os, requests
from colorama import Fore,init
init()
os.system('cls')if os.name == 'nt' else 'clear'
print(f"""\t{Fore.LIGHTCYAN_EX} _____ __   _ _______  _____ \n\t   |   | \  | |______ |     |\n\t{Fore.LIGHTMAGENTA_EX} __|__ |  \_| |       |_____|\n""")
r = requests.get('https://discord.com/api/v6/users/@me', headers = {'Authorization': input('Token >'), 'Content-Type': 'application/json'})
data_ = r.json() if r.status_code == 200 else print('Invalid Token')+exit()
for data in data_: exec("""try:print(f'{Fore.LIGHTCYAN_EX}{data} :{data_[f"{data}"]}')\nexcept:pass""")