import socket,os
from requests import get
from ttpalette.ttpalette import Color as color
from concurrent.futures import ThreadPoolExecutor
from module.banner import show_banner
from module.validate import http_checker,remove_www
user_url = ""
find_subdomains = []
numSub = 0
def subDomain_Finder(url):
    url = remove_www(url)
    url = http_checker(url,status="remove")
    
    show_banner()
    global user_url
    global find_subdomains

    def get_data(subdomain):
        global numSub
        url = f"{subdomain}.{user_url}"
        try:
            response = socket.gethostbyname(url)
            
            page = get(url=f"https://{url}").text
                
            
            if "404" in page:
                numSub +=1
                print(f"[{numSub}]{color.costum(220)} It exists but it's a{color.costum(196)} 404 {color.RESET}: {url}")
            else:
                numSub +=1
                find_subdomains.append(url)
                print(f"[{numSub}]{color.costum(46)} It exists {color.RESET}: {url}")
                
            
            
            
            
        except:
            numSub +=1
            print(f"[{numSub}]{color.costum(196)} It does not exist {color.RESET}: {url}")



    list_subdomains = open("module/subdomains.txt","r").read().split()

    
    user_url = url
    find_subdomains.append(user_url)
    with ThreadPoolExecutor(max_workers=30) as pool:
        response = pool.map(get_data,list_subdomains)
        for call in response:
            pass



    return find_subdomains
