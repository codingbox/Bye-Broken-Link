import requests
import threading
import os
import time

link_url = "https://cdn.jsdelivr.net/gh/codingbox/Pixiv-Craw@latest/url.txt"

os.system("curl -O " + link_url)

url_list = []
f = open("url.txt", "r")
line = f.readline()
while line:
    url_list.append(line.rstrip('\n'))
    line = f.readline()

url_list_ok = []
def request_url(n, k):
    for i in range(0, len(url_list)):
        if i % n != k:
            continue
        try:
            r = requests.get(url_list[i])
            print("pic " + url_list[i] + " " + (str)(r.status_code))
            if (r.status_code == 200):
                url_list_ok.append(url_list[i])
        except:
            print("Error " + url_list[i])

threads = []

for i in range(0, 10):
    threads.append(threading.Thread(target = request_url, args=(10, i)))
for i in range(0, 10):
    threads[i].start()
for i in range(0, 10):
    threads[i].join()

with open("url_ok.txt", 'a') as f:
    f.seek(0)
    f.truncate()
    for pic_url in url_list_ok:
        f.write(pic_url + "\n")

os.remove("url.txt")
