import requests
import bs4
from termcolor import colored


def userinfo(s, name):
    url = f"https://www.codechef.com/users/{name}"
    x = s.get(url)
    soup = bs4.BeautifulSoup(x.text, 'html.parser')
    rating = soup.find_all("div", class_="rating-number")
    # print(rating[0].text)
    li = soup.find("div", class_="rating-header text-center")
    li = li.find("small")
    # print(li.text)
    details = soup.find("section", class_="user-details")
    str = details.text
    str = str[0:str.find("Teams List:")]
    str = str.replace("\n\n\n", "")
    str = str.replace("\n\n", "\n")
    # str = str.replace("\n\n", "\n")

    print(colored(str+"Rating: "+rating[0].text+" "+li.text, "yellow"))
    # print("Rating: "+rating[0].text+" "+li.text)