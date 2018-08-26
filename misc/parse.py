import json

with open('tabula-gre_wordlist.json') as f:
    wordlist = json.load(f)

file = open("barrons800.txt", 'w')

for k in wordlist:
    for i in k['data']:
        if(i[0]['text']):
           print(i[0]['text'].capitalize() + ' : '  + i[1]['text'].replace('\r', \
                 ' ').capitalize() + '\n')
           file.write(i[0]['text'].capitalize() + ' : '  + i[1]['text'].replace('\r', \
                 ' ').capitalize() + '\n')

file.close()
