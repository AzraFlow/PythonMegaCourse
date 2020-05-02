#! python3

import time
from datetime import datetime as dt

hosts_temp = r"C:\Users\mbuhi\Desktop\azraflow\PythonMegaCourse\Section19_web_blocker\hosts"
# hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "dub119.mail.live.com",
                "www.dub119.mail.live.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8, 0) < dt.now() < \
       dt(dt.now().year, dt.now().month, dt.now().day, 16, 45):

        print("Working hours...")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()  # content is a list of line contents
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
