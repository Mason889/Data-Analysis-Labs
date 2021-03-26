import re
import string

f = open("samsung.json","r")
t = f.read()
f.close()
xml =t.split('\n')
for i in range(len(xml)):
    t=t+" "+xml[i]
title = re.findall('"title" : "(.+?)"source"', t)
for i in range(len(title)):
    t=t+" "+title[i]

t=re.sub('"textBody" :','',t)
t=re.sub('[-–―‖[\]\/?0-9",.()$+»«—:;_...]',' ',t)
t=t.upper()
t=re.sub('\s\w\s',' ',t)
t=re.sub('\s\w\w\s',' ',t)
t=re.sub('\s\s+',' ',t)
word =t.split(' ')
word.sort()
# Dictionary building
d={} 
old="" 
n=0
for i in range(len(word)):
    if (word[i] == old):
        n=n+1
    else:
        d[old]=n
        old=word[i]
        n=1
d[old]=n

sorted_dict = {}
sorted_keys = sorted(d, key=d.get, reverse=True) # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = d[w]

print(sorted_dict)