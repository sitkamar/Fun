import time
from datetime import datetime as dt
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = ""
website_list = ["www.facebook.com", "facebook.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("HAHA")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " "+website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)
            file.truncate()
        print("Sleeping")
    time.sleep(5)