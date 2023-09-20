from colorama import Fore,Style
import os,platform,time

def show_banner():
    if platform.uname()[0] == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    b = Fore.RED+"""
               _______  _______  _______  _______  _       
 |\     /|     (  ____ )(  ____ \(  ____ \(  ___  )( (    /|
 ( \   / )     | (    )|| (    \/| (    \/| (   ) ||  \  ( |
  \ (_) /_____ | (____)|| (__    | |      | |   | ||   \ | |
   ) _ ((_____)|     __)|  __)   | |      | |   | || (\ \) |
  / ( ) \      | (\ (   | (      | |      | |   | || | \   |
 ( /   \ )     | ) \ \__| (____/\| (____/\| (___) || )  \  |
 |/     \|     |/   \__/(_______/(_______/(_______)|/    )_)
                                                           
"""
    print(b+Style.RESET_ALL)




def show_menu():
    time.sleep(0.1)
    print(Fore.RED+" ["+Fore.WHITE+"*"+Fore.RED+"]"+Fore.CYAN+" Choose one of the options below \n")
    time.sleep(0.1)
    print(Fore.RED+" [1]"+Fore.WHITE+" Start Recon\n")
    time.sleep(0.1)
    print(Fore.RED+" [2]"+Fore.WHITE+" Exit . . .\n")



def custom_input(path_name):
    return input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"X-RECON"+Fore.BLUE+"~"+Fore.WHITE+f"@{path_name}"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")