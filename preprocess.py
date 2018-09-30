import os
import MeCab
tagger = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

files=os.listdir("ss_texts/")
n=0
for file in files:
    validtext=[]
    f=open("ss_texts/{}".format(file))
    for sent in f.readlines():
        if ("「" in sent) and ("」" in sent):
            validtext.append(sent.rstrip())

    for num in range(len(validtext)-1):
        #異なる人物間の会話のみを抽出
        if validtext[num].split("「")[0] != validtext[num+1].split("「")[0]:
            f1=open("call.txt","a")
            f1.write(tagger.parse(validtext[num].split("「")[1].split("」")[0]))
            f1.write("\n")
            f2=open("reply.txt","a")
            f2.write(tagger.parse(validtext[num+1].split("「")[1].split("」")[0]))
            f2.write("\n")

    n+=1
    #途中経過
    if n%100==0:
        print(n)
