from os import get_terminal_size
from datetime import datetime
from colorama import Fore
from ctypes import windll
import requests
import os

version_tool = "1.0"
windll.kernel32.SetConsoleTitleW(f"Tikvues BOT")
url_config = "https://raw.githubusercontent.com/modox-dev/check-requests/refs/heads/main/config.py"
maintenant = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def _print(thing: str, content: str , new_line: bool = True, input: bool = False) -> str:

    print('\033[?25l', end='')

    size = get_terminal_size().columns - 10
    col = "\033[38;2;250;230;-m"
    first_part = f"[{thing}] | {content}"
    new_part = ""
        
    counter = 0
    for caracter in first_part:
        new_part += col.replace('-', str(counter * int(255/len(first_part)))) + caracter + '\033[38;2;255;255;255m'
        counter += 1 
            
    if input:
        return f"{new_part}"
            
    if not new_line:
        print(f"{new_part}{' '*(size - len(first_part))}\033[38;2;255;255;255m", end="\r")

    else:
        print(f"{new_part}{' '*(size - len(first_part))}\033[38;2;255;255;255m")

try:
    response = requests.get(url_config).text

    key = 'version_tool = "'
    start = response.find(key)

    if start != -1:
        start += len(key)
        end = response.find('"', start)
        new_version = response[start:end]

        if new_version != version_tool:
            input(Fore.RED + "[ERROR] " + Fore.WHITE + "La version du logiciel est expiré, veuillez mettre à jour le logiciel.")

        else:
            first_color = '\033[38;2;250;230;50m'
            second_color = '\033[38;2;250;230;200m'
            reset_color = '\033[0m'

            self_banner = """

████████╗██╗██╗  ██╗██╗   ██╗██╗   ██╗███████╗███████╗
╚══██╔══╝██║██║ ██╔╝██║   ██║██║   ██║██╔════╝██╔════╝
   ██║   ██║█████╔╝ ██║   ██║██║   ██║█████╗  ███████╗
   ██║   ██║██╔═██╗ ╚██╗ ██╔╝██║   ██║██╔══╝  ╚════██║
   ██║   ██║██║  ██╗ ╚████╔╝ ╚██████╔╝███████╗███████║
   ╚═╝   ╚═╝╚═╝  ╚═╝  ╚═══╝   ╚═════╝ ╚══════╝╚══════╝

            Modox ~ github.com/modox-dev

            """

            first_color, second_color = '\033[38;2;250;230;50m', '\033[38;2;250;230;200m'

            banner = ""
            display_banner = ""

            for line in self_banner.splitlines():
                display_banner += " " * (int((get_terminal_size().columns - len(line)) / 3)) + line + "\n"

            for caracter in display_banner:
                if caracter in ['╚', '═', '╝', '╔', '║', '╗']:
                    banner += second_color + caracter
                elif caracter in ' ':
                    banner += caracter
                elif caracter.isalnum():
                    banner += '\033[38;2;255;200;230m' + caracter
                else:
                    banner += first_color + caracter

            print(banner)
            video_url = input(_print('?', 'Video URL > ', input=True))

            if not video_url.strip().startswith(("https://www.tiktok.com","https://tiktok.com","https://vm.tiktok.com","https://vt.tiktok.com")):
                print()
                input(_print('!', 'TikTok URL Invalid', input=True))
                quit()

            os.system("cls")
            print(banner)
            _print('?', 'Solving Captcha...\n',)

            _print('?', 'You need to have a Captcha Solver... Contact : modox.off (discord)\n',)
            input()
            quit()
except: pass