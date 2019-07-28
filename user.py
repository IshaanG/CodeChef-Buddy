import requests
import bs4,re
from termcolor import colored


def userinfo(s, name,xy):
    i = 0
    while(i < 2):
        url = f"https://www.codechef.com/users/{name}"
        x = s.get(url)
        soup = bs4.BeautifulSoup(x.text, 'html.parser')
        ac=soup.text
        ac=(ac[ac.find("Highcharts.chart('submissions-graph',"):ac.find("var problem_solved_count")])
        ac=ac[ac.find("data:"):]
        print(ac)
        reg=re.compile("y:(\w+),")
        lis=reg.findall(ac)
        #print(lis)
        rating = soup.find_all("div", class_="rating-number")
        # print(rating[0].text)

        li = soup.find("div", class_="rating-header text-center")
        if(type(li) != type(None)):

            li = li.find("small")
            #print(li.text)
            details = soup.find("section", class_="user-details")
            str = details.text
            str = str[0:str.find("Teams List:")]
            str = str.replace("\n\n\n", "")
            str = str.replace("\n\n", "\n")
            # str = str.replace("\n\n", "\n")
            print(lis)
            if(xy==0):
                print(colored(str+"Rating: "+rating[0].text+" "+li.text, "yellow"))
                print("------------------------------------------")
                print(colored("Correct Answer: "+lis[5],"green"))
                print(colored("Partially Accepted: "+lis[0],"green"))
                print(colored("Wrong Answer: "+lis[4],"red"))
                print(colored("Time Limit Exceeded: "+lis[3],"red"))
                print(colored("Compilation Error: "+lis[1],"yellow"))
                print(colored("Runtime Error: "+lis[2],"yellow"))

            # print("Rating: "+rating[0].text+" "+li.text)
            list=[lis[4],lis[0],lis[3],lis[2],lis[1]]
            return list
            break
        i = i+1
    if(i == 2):
        print("User not found")
# userinfo(requests.Session(),'ishaang12',0)

