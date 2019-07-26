import requests
import bs4
import time
import os
import practice
import threading
import subprocess
from termcolor import colored


def fuc(li, contest_code, s):
    #print("Coming to function")
    try:
        os.mkdir(contest_code)
    except:
        print(colored("Directory already found!", "red"))
    path = contest_code+'/'
    i = 0
    while (i < len(li)):
        path1 = path+li[i]
        print(path1)
        try:
            os.mkdir(path1)
        except:
            # print("Dirrint(path1)ectory already found")
            pass
        url = f'https://www.codechef.com/{contest_code}/problems/{li[i]}'
        x = s.get(url)
        y = bs4.BeautifulSoup(x.text, 'html.parser')
        z = y.find('div', class_='node clear-block')
        if(type(z) == type(None)):
            print(colored("Resolving Error", "red"))
            i = i-1
            continue
        # print(type(z))
        z = z.find('div', class_='content')
        z = str(z)
        # print(z)   #content containing question input and output
        out = ""
        # print(type(z))
        ques = z[z.find("as well")+10:z.find("Author:")]
        ques = ques.replace("\gt", ">")
        ques = ques.replace("\lt", "<")
        try:
            if(z.find('### Example Input') == -1):
                print(1/0)
            inp = z[z.find("### Example Input") +
                    21:z.find("### Example Output")-6]
        except:
            inp = ""
        try:
            # print(z[z.find('### Example Output')+23:])
            z1 = z[z.find('### Example Output'):]
            found = z1.find("```")
            if(found == -1):
                print(1/0)

            found2 = z1.find("```", found+1)
            # print(found," ",found2)
            out = z1[found+4:found2]
            # out=z[:z1.find('```')]
        except:
            out = ""
        # print(out)
        f1 = open(path1+'/input.inp', 'w')
        print(inp, file=f1)
        f2 = open(path1+'/input.oac', 'w')
        print(out, file=f2)
        f3 = open(path1+'/question.txt', 'w')
        print(ques, file=f3)
        f4 = open(path1+'/answer.cpp', 'w')
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        subprocess.call(
            f"pandoc {path1}/question.txt -o {path1}/question.pdf", shell=True)
        i = i+1

    print(li)


def fuc1(contest_code, s):
    #print("Coming to fuc1")
    try:
        os.mkdir("Practice")
    except:
        pass
    try:
        os.mkdir("Practice/"+contest_code)
    except:
        pass
    l = practice.practice(contest_code)
    # print(l)
    f1 = open(f"Practice/{contest_code}/input.inp", 'w')
    f2 = open(f"Practice/{contest_code}/input.oac", 'w')
    f3 = open(f"Practice/{contest_code}/answer.cpp", 'w')
    f4 = open(f"Practice/{contest_code}/question.txt", "w")
    print(l['input'], file=f1)
    print(l['output'], file=f2)
    print(l['ques'], file=f4)
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    subprocess.call(
        f"pandoc Practice/{contest_code}/question.txt -o Practice/{contest_code}/question.pdf", shell=True)
    return


def make_dir(contest_code, s, choice):
    #print("Entering to main dir")
    #aa = time.time()
    if(choice == 'c'):
        print(colored("Copying problem codes...", "magenta"))
        q_list = []
        url = "https://www.codechef.com/"+contest_code
        a = time.time()
        z = s.get(url)
        # print(time.time()-a)
        soup = bs4.BeautifulSoup(z.text, 'html.parser')
        pcode = soup.find('tbody')
        x = pcode.find_all('td')
        for i in range(1, len(x), 4):
            print(x[i].text)
            q_list.append(x[i].text)
        # print(time.time()-a)
        # print("Going from make dir to fuc")
        print(colored("Making Directories...", "magenta"))
        t1 = threading.Thread(target=fuc, args=(q_list, contest_code, s))
        t2 = threading.Thread(target=test_ques, args=(q_list, contest_code, s))
        t1.start()
        t2.start()
        # fuc(q_list, contest_code, s)
        # # print(time.time()-a)
        # test_ques(q_list, contest_code, s)
        t1.join()
        t2.join()
        #bb = time.time()
        # print(bb-aa)
        print(colored("Parsed problem successfully", "green"))

    else:
        print(colored("Copying problem codes...", "magenta"))
        fuc1(contest_code, s)
        test_ques1(contest_code, s)
        print(colored("Parsed problem successfully", "green"))


def test_ques1(contest_code, s):
    try:
        os.mkdir("Test_files")
    except:
        pass
    # print("Creating test file")
    i = 0
    while i < 1:
        obj = s.get(
            f"https://www.codechef.com/status/{contest_code}?sort_by=All&language=44&status=15&Submit=GO")
        soup = bs4.BeautifulSoup(obj.text, 'html.parser')
        ans = soup.text
        # print(type(ans))
        ans = (ans[ans.find("IDDate/TimeUserResultTimeMemLangSolution")+40:])
        ans = ans.replace("\n", "")
        ans = ans.replace(" ", "")
        code = ans[0:8]
        if(code.isdigit() == False):
            print(colored("Resolving error", "red"))
            continue
        print(f"Problem code: {code}")
        url = f"https://www.codechef.com/viewplaintext/{code}"
        text = requests.get(url)
        scode = bs4.BeautifulSoup(text.text, 'html.parser')
        # print(li[i])
        # print(scode.getText())
        fil = open(f"Test_files/{contest_code}.cpp", 'w')
        print(scode.getText(), file=fil)
        i = i+1
    # print("Returning from test_ques1")
    return 0


def test_ques(li, contest_code, s):
    try:
        os.mkdir("Test_files")
    except:
        pass
    i = 0
    print(colored("Creating testing files...", "magenta"))
    #rem = 0
    while(i < len(li)):
        # print(f"Running it {i} time")
        obj = s.get(
            f"https://www.codechef.com/{contest_code}/status/{li[i]}?sort_by=All&language=44&status=15&Submit=GO")
        soup = bs4.BeautifulSoup(obj.text, 'html.parser')
        ans = soup.text
        # print(type(ans))
        ans = (ans[ans.find("IDDate/TimeUserResultTimeMemLangSolution")+40:])
        ans = ans.replace("\n", "")
        ans = ans.replace(" ", "")
        code = ans[0:8]
        print(f"Problem code: {code}")
        if(code == "NoRecent"):
            break
        # if(code.isdigit() == False and rem <= 2):
        #     print("Removing error")
        #     rem = rem+1
        #     continue
        #rem = 0
        url = f"https://www.codechef.com/viewplaintext/{code}"
        text = requests.get(url)
        scode = bs4.BeautifulSoup(text.text, 'html.parser')
        # print(li[i])
        # print(scode.getText())
        fil = open(f"Test_files/{li[i]}.cpp", 'w')
        print(scode.getText(), file=fil)
        i = i+1
    return 0


def parse(s, contest_c, choice):
    make_dir(contest_c, s, choice)
    # test_ques("APRIL")
