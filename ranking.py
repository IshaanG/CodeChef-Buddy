import requests
import json
from termcolor import colored
c=0
def getranking(l,x,n):
    c=0
    page=1
    print(colored(f"-------------------------------------{x}--------------------------------------------\n\n",attrs=["bold"]))
    print('{:<4}{:<24}{:15}{:10}'.format("S.No.","Name","Country Rank","Rating"))
    while(1):
        if(l=='i'):
            lm=requests.get(f'https://www.codechef.com/api/ratings/all?sortBy=global_rank&order=asc&page={page}&filterBy=Institution%3D{x}')
        else:
            lm=requests.get(f'https://www.codechef.com/api/ratings/all?sortBy=global_rank&order=asc&page={page}&filterBy=Country%3D{x}')
        str=lm.text
        str=json.loads(str)
        str=str['list']
        if(len(str)==0):
            print("No name like this exist in codechef database")
            break
        for i in range(len(str)):
            c=c+1
            print(colored('{:<4}{:<24}{:^15}{:^10}'.format(c,str[i]['name'],str[i]['country_rank'],str[i]['rating']),"cyan",attrs=['dark']))
            if(c==n):
                break
        if(c==n):
            break
        page=page+1
# getranking("Birla Institute of Technology Mesra",10)

