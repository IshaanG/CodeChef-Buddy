import requests
import bs4
import time
from datetime import datetime, timedelta
import make_dir
import threading
import sys
from threading import Timer


def get_comp(s,x):
    while True:
        try:
            url = 'https://www.codechef.com/contests'
            z = s.get(url)
            soup = bs4.BeautifulSoup(z.text, 'html.parser')
            #print(table)
            table = soup.find_all('table', attrs={'class': 'dataTable'})[1]
            table = table.find('tbody')
            if(x==0):
                print(table.text)
            break
        except:
            pass
    print("Returning table")
    return table


def race(s, pname):
    x=pname[len(pname)-1]
    pname=pname[0:len(pname)-1]
    print(pname)
    print("Coming to race")
    str = get_comp(s,1)
    ra = str.find_all('tr')
    for i in range(len(ra)):
        x = ra[i].find_all('td')
        if(x[0].getText() == pname):
            contesttime = x[2].getText()
            li = contesttime.split(' ')
    #print(li)
    countdown(li, s, pname,x)



def countdown(ctime, s, pname,x):
    print("Coming to countdown")
    now = datetime.now()
    t2 = ctime[4]
    li2 = t2.split(':')
    contest_time = timedelta(
        hours=int(li2[0]), minutes=int(li2[1]), seconds=int(li2[2]))
    current_time = timedelta(
        hours=now.hour, minutes=now.minute, seconds=now.second)
    print(contest_time)
    print(current_time)
    delay = (contest_time-current_time).total_seconds()
    print(delay)
    for i in range(int(delay)):
        now = datetime.now()

        current_time = timedelta(
            hours=now.hour, minutes=now.minute, seconds=now.second)

        print(contest_time-current_time, end="\r")
        #
        time.sleep(1)
    make_dir.parse(pname+x,s)
    #
    # print("he")
    #make_dir.parse(s, pname)


