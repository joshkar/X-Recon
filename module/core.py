from module.validate import http_checker
from module.engine import urls,result,scrape,get_inputs_names_and_ids
from concurrent.futures import ThreadPoolExecutor
from module.engine import allowed_domains
from module.subdomain import subDomain_Finder
from time import gmtime, strftime

time = strftime("%Y-%m-%d-%H:%M", gmtime())

def start_proccess(file_name,url):

    alw_domain_data =  subDomain_Finder(url)
    allowed_domains.extend(alw_domain_data)
    
    url_file_name = "logs/"+time+"-"+file_name+".txt"

    scrape(url,5)
    with open(url_file_name,"w") as site_links:
        for i in urls:
            if i == "":
                pass

            else:
                site_links.write(i+"\n")


    data = open(url_file_name,"r").read().split("\n")
    with ThreadPoolExecutor(max_workers=16) as pool:
        tr = pool.map(get_inputs_names_and_ids,data)
        for _ in tr:
            
            pass



    data_result = open(f"logs/{time}-{file_name}-param.txt","a")

    for i in result:
        try:

            data_result.write(i+"\n")
        except:
            pass

    data_result.close()

    print(f"File Saved To : logs/{time}-{file_name}-extracted-param.txt")
    input("If you Want back to menu > press")

