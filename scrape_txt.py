import requests
from bs4 import BeautifulSoup
import subprocess
from time import sleep

#数はその時の総ページ数
for page in range(1,234):
    s = requests.Session()
    r = s.get("http://ssimas72.blog.jp/?p={}".format(page))
    soup = BeautifulSoup(r.text)

    #各記事のURLの取得
    urls=[]
    for aa in soup.find_all(class_="article-title"):
        urls.append(aa.a.get("href"))

    for unum,url in enumerate(urls):
        #安全のため
        sleep(1)

        try:
            s = requests.Session()
            r = s.get(url)
            soup = BeautifulSoup(r.text)
            text=[]
            for bb in soup.find_all(class_="t_b"):
                text.append(bb.get_text())

            f=open("ss_texts/p"+str(page)+"_"+str(unum)+".txt",'a')
            for i in text:
                f.write(i)
            f.close()
        except:
            print("p"+str(page)+"_"+str(unum)+" failed")
    print("page {} finished".format(page))
