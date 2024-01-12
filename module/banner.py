from ttpalette.ttpalette import Color as color
from os import system
from platform import uname

menu = [
    "Start Recon",
    "Start Scan",
    "Setting",
    "Exit...",
]

banner = f"""██╗  ██╗     ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
╚██╗██╔╝     ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
 ╚███╔╝█████╗██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
 ██╔██╗╚════╝██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██╔╝ ██╗     ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║{color.costum(75)}  This one is different{color.RESET}
╚═╝  ╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
                                                        """

def show_banner():
    if uname()[0] == "Windows":
        system("cls")
    else:
        system("clear")
        
    for char in banner:
        if char == "█":
            print(f"{color.costum(124)}{char}{color.RESET}", end="")
        else:
            print(char, end="")
    
    print()
        

    


def show_menu(question):
    print(f"{color.costum(39)}[{color.RESET}?{color.costum(39)}]{color.RESET} {question}")
    for item in menu:
        print(f"{color.costum(39)}[{color.RESET}{menu.index(item)+1}{color.costum(39)}]{color.RESET} {item}")
        
    print()
    


# {color.costum(46)}{color.RESET}

def custom_input(path_name):
    return input(f"{color.costum(46)}[{color.RESET}{color.costum(196)}X{color.RESET}-RECON{color.costum(46)}]{color.RESET}{color.costum(46)}[{color.RESET}{path_name.capitalize()}{color.costum(46)}]{color.RESET}\n$ ")