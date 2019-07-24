import requests
import bs4
import time
import os
import practice


def fuc(li, contest_code, s):
    print("Coming to function")
    try:
        os.mkdir(contest_code)
    except:
        print("Directory already found")
    path = contest_code+'/'
    for i in range(len(li)):
        path1 = path+li[i]
        print(path1)
        try:
            os.mkdir(path1)
        except:
            #print("Directory already found")
            pass
        url = f'https://www.codechef.com/{contest_code}/problems/{li[i]}'
        x = s.get(url)
        y = bs4.BeautifulSoup(x.text, 'html.parser')
        z = y.find('div', class_='node clear-block')
        if(type(z) == type(None)):
            print("Removing Error")
            i = i-1
            continue
        print(type(z))
        z = z.find('div', class_='content')
        z = str(z)
        # print(z)   #content containing question input and output
        out = ""
        # print(type(z))
        ques = z[z.find("as well")+10:z.find("### Example Input")]
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

    print(li)


def fuc1(contest_code, s):
    print("Coming to fuc1")
    try:
        os.mkdir("Practice")
    except:
        pass
    try:
        os.mkdir("Practice/"+contest_code)
    except:
        pass
    l = practice.practice(contest_code)
    print(l)
    f1 = open(f"Practice/{contest_code}/input.inp", 'w')
    f2 = open(f"Practice/{contest_code}/input.oac", 'w')
    f3 = open(f"Practice/{contest_code}/answer.cpp", 'w')
    print(l['input'], file=f1)
    print(l['output'], file=f2)
    return


def make_dir(contest_code, s, choice):
    print("Entering to main dir")
    if(choice == 'c'):
        print("Coming to make dir")
        q_list = []
        url = "https://www.codechef.com/"+contest_code
        a = time.time()
        z = s.get(url)
        print(time.time()-a)
        soup = bs4.BeautifulSoup(z.text, 'html.parser')
        pcode = soup.find('tbody')
        x = pcode.find_all('td')
        for i in range(1, len(x), 4):
            print(x[i].text)
            q_list.append(x[i].text)
        print(time.time()-a)
        print("Going from make dir to fuc")
        fuc(q_list, contest_code, s)
        print(time.time()-a)
        test_ques(q_list, contest_code, s)
    else:
        print("Coming to right place")
        fuc1(contest_code, s)
        test_ques1(contest_code, s)
        print("Parsed problem successfully")


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
            print("Removing error")
            continue
        print(code)
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
    print("Creating Testing files")
    rem = 0
    while(i < len(li)):
        print(f"Running it {i}st time")
        obj = s.get(
            f"https://www.codechef.com/{contest_code}/status/{li[i]}?sort_by=All&language=44&status=15&Submit=GO")
        soup = bs4.BeautifulSoup(obj.text, 'html.parser')
        ans = soup.text
        print(type(ans))
        ans = (ans[ans.find("IDDate/TimeUserResultTimeMemLangSolution")+40:])
        ans = ans.replace("\n", "")
        ans = ans.replace(" ", "")
        code = ans[0:8]
        print(code)
        if(code.isdigit() == False and rem <= 2):
            print("Removing error")
            rem = rem+1
            continue
        rem = 0
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
