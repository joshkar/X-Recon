import requests,re,json
from urllib.parse import urlparse,unquote
from bs4 import BeautifulSoup
from module import validate
from colorama import Fore

urls = set()
paths = set()
result = set()
results = []

header = {
   "Accept": "*/*",
   "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

regex = re.compile(r"((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)", re.DOTALL)

block_list = tuple(json.loads(open("setting.json").read())['block_list'])

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
        if parsed.netloc in allowed_domains:
            if u.endswith(block_list) or ".js?" in u or ".css?" in u or "#" in u or parsed.path in paths:
                continue
            else:
                urls.add(u)
                paths.add(parsed.path)
                
                scrape(u,max_depth,current_depth+1)
    

def extract_form_and_inputs(html, url):
    global results
    soup = BeautifulSoup(html, 'html.parser')
    form_inputs = soup.find_all('input', {'name': True})

    form_dict = {}
    non_form_inputs = []

    form_methods = {}

    for input_element in form_inputs:
        param_name = input_element['name']
        parent_form = input_element.find_parent('form')

        input_type = input_element.get('type', 'text')

        if parent_form:
            method = parent_form.get('method', 'GET')
            is_form = True

            if parent_form in form_dict:
                form_dict[parent_form]["parametr"].append(param_name)
                form_dict[parent_form]["type"].append(input_type)
            else:
                form_dict[parent_form] = {"parametr": [param_name], "type": [input_type]}

            form_methods[parent_form] = method
        else:
            method = None
            is_form = None
            non_form_inputs.append(param_name)


    for form, param_info in form_dict.items():
        result = {
            "url": url,
            "parametr": [{"name": param_info["parametr"], "type": param_info["type"]}],
            "method": str(form_methods[form]).lower(),
            "is_form": True
        }
        results.append(result)

    for input_name in non_form_inputs:
        result = {
            "url": url,
            "parametr": [{"name": [input_name], "type": ["text"]}],
            "method": None,
            "is_form": None
        }
        results.append(result)

    return results

num = 1
def Processing_Extracted_Links(valid_url):
    global num
    for i in valid_url.split("\n"):
        if i == "":
            pass
        
        else:

            print(Fore.LIGHTBLUE_EX+f"[{num}] Extract Parametrs > {Fore.WHITE+unquote(i)}")
            num +=1
            try:

                http = requests.get(i).text
                rr = extract_form_and_inputs(http,i)
                # print(rr)

            except Exception as ex:
                # pass
                print(ex)
