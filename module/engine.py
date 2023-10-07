import requests,re
from urllib.parse import urlparse,unquote
from bs4 import BeautifulSoup
from module import validate
from colorama import Fore

urls = set()
paths = set()
result = set()


header = {
   "Accept": "*/*",
   "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

regex = re.compile(r"((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)", re.DOTALL)

block_list = (".css",".js",".mp4",".zip","png",".svg",".jpeg",".webp",".jpg")

allowed_domains = list()

def get_all_urls(url):
   valid_urls = set()
   response = requests.get(url,headers=header).text
   for match in regex.findall(response):
      valid_urls.add(match[0])
   soup = BeautifulSoup(response,features="xml")
   

   for elem in soup.select("[href]"):
      valid_urls.add(validate.correct_url(url,elem['href']))
   for elem in soup.select("[src]"):
      valid_urls.add(validate.correct_url(url,elem['src']))
   return valid_urls


numb = 1

def scrape(url,max_depth,current_depth=1):
    global numb
    print(Fore.RED+f"[{numb}] {Fore.WHITE+unquote(url)}")
    numb+=1

    if current_depth > max_depth:
        return
    
    if url.endswith(block_list) or ".js?ver" in url or ".css?ver" in url or "#" in url:
        pass
    else:

        urls.add(url)
    found_urls = get_all_urls(url)
    for u in found_urls:
        parsed = urlparse(u)
        if parsed.hostname in allowed_domains[0]:
            if u.endswith(block_list) or ".js?" in u or ".css?" in u or "#" in u or parsed.path in paths:
                continue
            else:
                urls.add(u)
                paths.add(parsed.path)
                
                scrape(u,max_depth,current_depth+1)
    

num = 1
def get_inputs_names_and_ids(valid_url):
    global num
    for i in valid_url.split("\n"):
        print(Fore.LIGHTBLUE_EX+f"[{num}] Extract Parametrs > {Fore.WHITE+unquote(i)}")
        num +=1
        try:

            http = requests.get(i).text
            soup = BeautifulSoup(http,"html.parser")
            for i in soup.select("input"):
                result.add(i.get('id'))
                result.add(i.get('name'))

        except:
            pass

    
        
    