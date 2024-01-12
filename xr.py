from module.banner import *
from module.core import start_proccess
from module.validate import http_checker
from module.setting import submit_change
from module.xss_scan import *

while True:
    show_banner()
    show_menu("Choose one of the options below")
    try:

        original_menu = custom_input("home")
        

        if  original_menu == "1":
            show_banner()
            print(f"{color.costum(39)}[{color.RESET}?{color.costum(39)}]{color.RESET} Ok. Give me a URL\n")
            get_url = custom_input("GET-URL")
            
            file_name = f"{http_checker(get_url,status='remove')}"
      
            start_proccess(file_name,http_checker(get_url,status='set_http'))


        elif original_menu == "2":
            show_banner()
            xss_files = find_scanned_files()
            if not xss_files:
                exit(f"[{color.costum(124)}Notification{color.RESET}] No File For Scan")
            
            else:

                num_x = 0
                print(f"{color.costum(39)}[{color.RESET}?{color.costum(39)}]{color.RESET} Select A file\n")
                for i in xss_files:
                    print(f"{color.costum(39)}[{color.RESET}{num_x}{color.costum(39)}]{color.RESET} {i}")
                    num_x +=1
                
                xss_file_id = int(custom_input("GET-FILE"))
                xss_file_id = "logs/"+xss_files[xss_file_id]
                print(f"[{color.costum(124)}Notification{color.RESET}] Testing XSS ...")
                start_scan(xss_file_id)
                
        
        
        elif original_menu == "3":
            show_banner()
            submit_change()
            

        elif original_menu == "4":
            
            exit(f"\n[{color.costum(124)}Notification{color.RESET}] Goodbye :) ")
        
            



    except KeyboardInterrupt:
        exit(f"\n[{color.costum(124)}Notification{color.RESET}] Goodbye :) ")

    except ValueError:
        exit(f"\n[{color.costum(124)}Notification{color.RESET}] Please Enter a Number ")

