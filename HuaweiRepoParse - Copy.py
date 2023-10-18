import requests
import re
i=48723
my_file=open("HWgoodlinks.txt","w")
while i < 99999:
    i = i + 1
    link="http://download-c.huawei.com/download/downloadCenter?downloadId="+str(i)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'}
    print(i)
    if requests.head(link, headers=headers).headers.get('content-disposition') != None:
        d = requests.head(link, headers=headers).headers['Content-Disposition']
        fname = re.findall("attachment; filename=(.+)", d)
        temp=link+" : "+str(fname)+"\n"
        my_file.write(temp)      
my_file.close()