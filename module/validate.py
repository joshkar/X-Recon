from urllib.parse import urlparse

def correct_url(main_url, found_url):
   main_url = main_url[:-1] if main_url.endswith("#") else main_url
   main_url = main_url if main_url.endswith("/") else main_url+"/"
   parsed = urlparse(main_url)
   if found_url.lower().startswith("https://") or found_url.lower().startswith("http://"):
      return found_url
   elif found_url.startswith("/"):
      return parsed.hostname+found_url
   else:
      return main_url+found_url




def http_checker(url,status):
   if status == "remove":
      if url.lower().startswith("https://"):
         fix = url.replace("https://","").replace("/","")
         return fix
         
      elif url.lower().startswith("http://"):
         fix = url.replace("http://","").replace("/","")
         return fix
      
      else:
         return url.replace("/","")
    

   
   elif status == "set_http":
      parsed_url = urlparse(url)
      
      if parsed_url.scheme not in ('http', 'https'):
        url = 'http://' + url
        return url
      else:
         return url
   

def remove_www(url):
   if urlparse(url).netloc[0:4] == "www.":
      url = url.replace("www.","")
   
   return url
