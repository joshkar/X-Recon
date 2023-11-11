from module.validate import http_checker,remove_www
from module.engine import urls,result,results,scrape,Processing_Extracted_Links
from concurrent.futures import ThreadPoolExecutor
from module.engine import allowed_domains
from module.subdomain import subDomain_Finder
from time import gmtime, strftime
import json

time = strftime("%Y-%m-%d-%H:%M", gmtime())

def start_proccess(file_name,url):
    alw_domain_data =  subDomain_Finder(url)
    allowed_domains.extend(alw_domain_data)
    max_depth_val = int(json.loads(open("setting.json").read())['max_depth'])
    url_file_name = "logs/"+time+"-"+file_name+".txt"

    scrape(url,max_depth_val)
    with open(url_file_name,"w") as site_links:
        for i in urls:
            if i == "":
                pass

            else:
                site_links.write(i+"\n")


    data = open(url_file_name,"r").read().split("\n")
    with ThreadPoolExecutor(max_workers=16) as pool:
        tr = pool.map(Processing_Extracted_Links,data)
        for _ in tr:
            
            pass



    json_log_name = f"logs/{time}-{file_name}-param.json"
    with open(json_log_name, 'w') as json_file:
        json.dump(results, json_file, indent=4)

    print(f"File Saved To : {json_log_name}")
    input("If you Want back to menu > press")

