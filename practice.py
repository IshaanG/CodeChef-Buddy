import requests
import bs4
import re


def practice(prob):
    print("Entering practice function")
    z = requests.get(f"https://www.codechef.com/problems/{prob}")
    soup = bs4.BeautifulSoup(z.text, 'html.parser')
    str = soup.text
    str1 = str
    # str='### h Input'
    ques = str[str.find("as well")+10:str.find("Author:")]
    ques = ques.replace("\gt", ">")
    ques = ques.replace("\lt", "<")
    reg = re.compile(r'###(.*Input)')
    mo = reg.findall(str)
    # x=mo[1]
    pos = str.find(mo[1])+len(mo[1])
    str = str[pos:]
    str = str[str.find('```')+3:]
    inp = str[:str.find('```')]
    # print(inp)
    # reg1=reg=re.compile(r'###(.*Output)')
    reg = re.compile(r'###(.*Output)')
    mo1 = reg.findall(str1)
    # x1=mo1[1]
    # print(x1)
    pos1 = str1.find(mo1[1])+len(mo1[1])
    str1 = str1[pos1:]
    # print(str1)
    str1 = str1[str1.find('```')+3:]
    out = str1[:str1.find('```')]
    # print(out)
    dict = {"input": inp, "output": out, "ques": ques}
    return dict
# x=practice("ADAKNG")
# print(x)
