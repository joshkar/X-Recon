from module.banner import *
from module.core import start_proccess
from module.validate import http_checker
from module.setting import submit_change
from module.xss_scan import *
import json

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
            show_banner()
            xss_files = find_scanned_files()
            if not xss_files:
                exit("No File For Scan")
            
            else:

                num_x = 0
                print(" Select A file \n ")
                for i in xss_files:    
                    print(f"{Fore.WHITE} [{num_x}] {Fore.RED}{i}\n")
                    num_x +=1
                
                xss_file_id = int(custom_input("GET-FILE"))
                xss_file_id = "logs/"+xss_files[xss_file_id]
                print("Testing XSS . . .")
                start_scan(xss_file_id)
                
        
        
        elif original_menu == "3":
            show_banner()
            submit_change()
            

        elif original_menu == "4":
            
            exit("\n Goodbye :) ")
        
            



    except KeyboardInterrupt:
        exit("\n Goodbye :) ")

    except ValueError:
        exit("\n Please Enter a Number")

