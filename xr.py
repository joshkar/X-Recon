from module.banner import *
from module.core import start_proccess
from module.validate import http_checker

while True:
    show_banner()
    show_menu()
    try:

        original_menu = custom_input("HOME")
        

        if  original_menu == "1":
            show_banner()
            print("Ok. Give me a URL\n")
            get_url = custom_input("GET-URL")
            
            file_name = f"{http_checker(get_url,status='remove')}"
      
            start_proccess(file_name,http_checker(get_url,status='set_http'))


        
        elif original_menu == "2":
            
            exit("\n Goodbye :) ")
        
            



    except KeyboardInterrupt:
        exit("\n Goodbye :) ")



