import requests
from colorama import Fore, init
from random import choices, choice

init(autoreset=True)

colors = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
]

def check():
    while True:
        username = ''.join(choices('abcdefghijklmnopqrstuvwxyz1234567890', k=2))
        col = choice(colors)
        headers = {
            'authority'                : 'guns.lol',
            'accept'                   : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language'          : 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer'                  : 'https://guns.lol/',
            'sec-ch-ua'                : '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile'         : '?0',
            'sec-ch-ua-platform'       : '"Windows"',
            'sec-fetch-dest'           : 'document',
            'sec-fetch-mode'           : 'navigate',
            'sec-fetch-site'           : 'same-origin',
            'sec-fetch-user'           : '?1',
            'upgrade-insecure-requests': '1',
            'user-agent'               : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }

        try:
            response = requests.get(f'https://guns.lol/{username}', headers=headers)
            if response.status_code == 200:
                print(f"{Fore.RED}[-] {username} Taken")
            else:
                print(f"{Fore.GREEN}[+] {username} Available")
                with open("Available.txt", 'a') as f:
                    f.write(username + '\n')
        except requests.RequestException as e:
            print(f"{Fore.YELLOW}[!] Error: {e}")

if __name__ == "__main__":
    check()
