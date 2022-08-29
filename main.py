from rich.console import Console
import sys
import colorama

from colorama import Fore, init

from pystyle import Center, Colors, Colorate, System

from settings.settings import MenuSettings
from settings.settings_session import SessionsRead

console = Console()

session_list = SessionsRead()
list_function = MenuSettings()

banner = r'''

⠄⠄⠄⠄⠄⠄⢴⣿⣿⣿⣷⣤⣤⣄⡀⢠⣤⣄⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠙⢿⣿⣟⣉⣠⣤⣤⣤⣉⡻⢿⣇⣠⣤⣤⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⣿⣿⣿⠟⢋⣁⣄⡈⠻⣿⢃⣴⠷⠄⠄⠄⠄⠄ 
⠄⠄⠄⠄⠄⠄⠄⢀⡴⠶⢾⣿⣿⣿⣿⣿⠟⣩⣭⣭⣄⡀⠛⢡⣾⡏⠉⠄⠄⠄
⠄⠄⠄⠄⠄⠄⢸⡏⠄⠄⠢⠘⣿⣿⣿⠘⣿⣿⡿⠁⠙⣿⡄⢸⣿⡇⢰⡷⠄⠄   Rofl-fork by Commit 404
⠄⠄⠄⠄⠄⢀⣼⣧⠄⠄⠄⢰⣿⣿⠋⣷⢸⣿⠇⢰⠆⣿⡇⠈⢿⡿⠆⠄⣠⡄   
⠄⠄⣀⣴⣾⣿⣿⣿⣆⠄⠄⣾⣿⣿⣇⢿⡌⠻⣤⣤⠶⠟⣁⠐⡖⠒⠂⢉⣩⣀   
⠄⣼⣿⣿⡿⠛⣥⣤⣤⡄⠄⠘⠋⠛⠿⡌⠛⠳⠶⠆⣠⣴⣿⣷⡘⢋⣽⣿⡿⠟
⣼⣿⣿⣿⡇⢸⣇⡈⠟⢠⣄⣰⢏⡠⠄⠰⢶⣶⣶⣾⣿⣿⣿⣿⠿⠿⣟⣡⠴⠄
⢿⣿⣿⣿⣧⠈⣿⣷⠄⢸⣿⣿⣯⣠⠞⣠⣈⠻⠿⠿⢿⣛⣉⠤⠶⠛⣫⡀⠄⠄
⠈⣿⣿⣿⣿⣷⠙⢿⡄⣸⣿⣿⣿⣷⣾⠟⠁⠄⠄⠄⠄⠨⣻⡄⣀⣴⠏⠄⠄⠄
⠄⠄⠙⢿⣿⣿⣿⡖⣸⣿⣿⣿⣿⠋⣠⣾⡿⠇⣀⡀⠄⠄⠁⣿⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠈⠛⠿⢀⣿⣿⣿⣿⡇⣤⣤⣴⠶⠟⠛⠉⠙⠛⠛⠁⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⢠⣾⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄

GitHub: https://github.com/Madara225/vk-raid-botnet
Authors' channel: https://t.me/Pepe_devs and https://t.me/huis_bn

Author's channel of fork: https://t.me/CrimsonBots
'''

System.Clear()
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))  

def botnet_main():

    menu_function={}

    print(f'botnet accounts >> {len(session_list.sessions)}')
    for num_function, function in enumerate(
            list_function.menu_botnet,
            start=1
        ):

        menu_function[num_function]=function
        print(f'[{num_function}] {function.__doc__}')

    try:
        menu = int(console.input('>> '))

        for num, classes in menu_function.items():
            if num == menu:
                classes(session_list.sessions)

    except KeyboardInterrupt:
        print('\n[blue]<https://t.me/pepe_devs>[/]')
        sys.exit()

    except:
        botnet_main()

botnet_main()
