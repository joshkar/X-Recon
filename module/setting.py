from module.banner import custom_input
import json
from ttpalette.ttpalette import Color as color
from colorama import Fore

def change_setting(json_file, new_max_depth):

    with open(json_file, 'r') as file:
        data = json.load(file)
        
    data['max_depth'] = int(new_max_depth)

    with open(json_file, 'w') as file:
        json.dump(data, file,indent=4)


    
def submit_change():
     
    max_depth_val = json.loads(open("setting.json").read())['max_depth']
    print(f"{color.costum(39)}[{color.RESET}?{color.costum(39)}]{color.RESET} Ok, Your Max Depth is {color.costum(196)}{max_depth_val}{color.RESET}if You Want change this. give me a number(2-5)\n")
    mxdt = int(custom_input("SETTING"))
    if mxdt < 2 or mxdt > 6:
        exit(f"[{color.costum(124)}Notification{color.RESET}] Please enter a number in the range of 2 to 6")
    change_setting("setting.json",mxdt)