import socket,os
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore
from module.banner import show_banner
from module.validate import http_checker
user_url = ""
find_subdomains = []
numSub = 0
def subDomain_Finder(url):
    url = http_checker(url,status="remove")
    show_banner()
    global user_url
    global find_subdomains

    def get_data(subdomain):
        global numSub
        url = f"{subdomain}.{user_url}"
        try:
            response = socket.gethostbyname(url)
            numSub +=1
            find_subdomains.append(url)
            print (f"{Fore.WHITE}[{numSub}]{Fore.GREEN} Found : {url}")
            
        except:
            numSub +=1
            print(f"{Fore.WHITE}[{numSub}]{Fore.RED} Not Found : {url}")



    list_subdomains = open("module/subdomains.txt","r").read().split()

    
    user_url = url
    find_subdomains.append(user_url)
    with ThreadPoolExecutor(max_workers=30) as pool:
        response = pool.map(get_data,list_subdomains)
        for call in response:
            pass



    return find_subdomains
