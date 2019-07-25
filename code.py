import json
import bs4
import requests
import time
import contest
import test
import webbrowser
import make_dir
from termcolor import colored
import encryption
import threading
import hashlib

master_password = "EAwpaeBxscpvSNkYQFc7Laq2"

key = hashlib.sha256(master_password.encode('utf-8')).digest()


def logout(s):
    print("Logging you out")
    s.get("https://www.codechef.com/logout")
    one_time_login = 0


def get_token(str):
    token = bs4.BeautifulSoup(str, 'html.parser')
    ans = token.find('input', id='edit-problem-submission-form-token')
    try:
        return ans['value']
    except:
        print("Some error occured")
        pass


def get_id(str):
    token = bs4.BeautifulSoup(str, 'html.parser')
    ans = token.find('input', attrs={'name': 'form_build_id'})
    try:
        return ans['value']
    except:
        print("Some error occured")
        pass


def result(obj, s):
    print(obj.url)
    status_code = obj.url.split('/')[-1]
    # print(status_code)

    try:
        print(colored("Submitting...", 'green'))
        while True:
            a1 = s.get(
                f'https://www.codechef.com/get_submission_status/{status_code}/', headers=headers)
            # print(a1.text)
            # print(type(a1.text))
            try:
                dict = json.loads(a1.text)
                x = dict['result_code']
            except:
                print("Error occuring here")
                continue
            # print(x)
            # print(dict)
            if(x != 'wait'):
                if(x == "compile"):
                    print(colored('Compilation Error', 'yellow'))
                    break
                elif(x == "runtime"):
                    print(colored("Runtime Error", 'red'))
                    break
                elif(x == "accepted"):
                    print(colored("Correct answer", 'green'))
                    break
                elif(x == "wrong"):
                    print(colored("Wrong Answer", 'red'))
                    break
            else:
                pass

    except Exception as e:
        print("Error occured")
        print(e)
        logout(s)
        pass
    #print("Status code printed")
    return 0

    #t1 = threading.Thread(target=get_token, attrs={p.text})


def submit(s, contest_c, lang, xy):
    if(xy != 'p'):
        prob = input("Enter problem to be submitted: ")
    else:
        prob = contest_c
    while True:
        print(colored(f"Submitting {prob}...", "green"))
        p = s.get(f"https://www.codechef.com/submit/{prob}", headers=headers)
        #xyz = time.time()
        form_token = get_token(p.text)
        # print(time.time()-xyz)
        form_build_id = get_id(p.text)
        # print(time.time()-xyz)
        # print(form_token)
        # print(form_build_id)
        payload = {
            'form_build_id': form_build_id,
            'form_token': form_token,
            'form_id': 'problem_submission',
            'language': lang,
            'problem_code': prob,
            'op': 'Submit'
        }
        if(xy == 'p'):
            fi = open(f"Practice/{prob}/answer.cpp")
        else:
            fi = open(f'{contest_c}/{prob}/answer.cpp')
        # f2=fi
        # print(f2.read())
        myfile = {'files[sourcefile]': fi}
        obj = s.post(
            f"https://www.codechef.com/submit/{prob}", data=payload, files=myfile, headers=headers)
        x = obj.url.split('/')[-1]
        if(x.isdigit() == True):
            print(colored(f"Submission id: {x}", "blue"))
            break
        fi.close()
    print(colored("Problem submitted successfully", "green"))
    result(obj, s)


def openf():
    inp = input("Enter problem name")
    webbrowser.open(f"https://www.codechef.com/problems/{inp}")


def login():
    global one_time_login
    payload = {
        'form_id': 'new_login_form',
        'op': 'Login'
    }
    decrypted = encryption.decrypt(key, "ivfile", "new.json")
    # print(type(decrypted))
    decrypted.decode('utf-8')
    # str=json.load(open('new.json','r'))
    str = json.loads(decrypted)
    # print(str)
    payload['name'] = str['username']
    payload['pass'] = str['password']
    lang = str["language"]
    with requests.Session() as s:
        while(1):
            print("----------------Type help to view commands----------------")
            # print(r.text)
            str = input()
            li = str.split(' ')
            if(len(li) == 2 and li[0] != "race"):
                choice = li[0]
                contest_c = li[1]
                # print("Enter\np-Practice\nc-Contest\n")
                # choice=input()
                # if(choice=='c'):
                #     print("Enter contest name")
                # else:
                #     print("Enter problem name")
                # contest_c=input()
                # print(make_dir.parse())
                while True:
                    print("----------------Type help to view commands----------------")
                    print(colored("ENTER: ", attrs=['bold']))
                    inp = input()
                    if(inp == "submit" and choice == 'c'):  # Not working for contest
                        try:
                            if(one_time_login == 0):
                                while(1):
                                    print(
                                        colored("Logging in...", "green"), end="\r")
                                    ti = time.time()
                                    p = s.get(
                                        "https://www.codechef.com/", headers=headers)
                                    soup = bs4.BeautifulSoup(
                                        p.text, 'html.parser')
                                    if(type(soup) != type(None)):
                                        break
                                a = soup.find('input', attrs={"name": 'form_build_id'})[
                                    'value']
                                payload['form_build_id'] = a
                                s.post('https://www.codechef.com/',
                                       data=payload, headers=headers)
                                # print(time.time()-ti)
                                print(colored("Logged in     ", "yellow"))
                                one_time_login = one_time_login+1
                            submit(s, contest_c, lang, 'c')
                        except:
                            logout(s)
                    # Working for practice as well as contest but not parsing question and have to add multithreading
                    elif(inp == "parse" and choice == 'c'):
                        try:
                            if(one_time_login == 0):
                                while(1):
                                    print(
                                        colored("Logging in...", "green"), end="\r")
                                    ti = time.time()
                                    p = s.get(
                                        "https://www.codechef.com/", headers=headers)
                                    soup = bs4.BeautifulSoup(
                                        p.text, 'html.parser')
                                    if(type(soup) != type(None)):
                                        break
                                a = soup.find('input', attrs={"name": 'form_build_id'})[
                                    'value']
                                payload['form_build_id'] = a
                                s.post('https://www.codechef.com/',
                                       data=payload, headers=headers)
                                # print(time.time()-ti)
                                print(colored("Logged in     ", "green"))
                                one_time_login = one_time_login+1
                            make_dir.parse(s, contest_c, choice)
                        except:
                            logout(s)
                    elif(inp == "test" and choice == 'c'):
                        varr = input("Enter problem name: ")
                        test.Test(contest_c, lang, varr)
                    elif(inp == 'open' and choice == 'c'):  # complete
                        openf()
                    elif(inp == "upcontest"):  # complete
                        contest.get_comp(s, 0, 1)
                    elif(inp == "ctest" and choice == 'c'):
                        xc = input("Enter problem name: ")
                        # if entered wrong contest name in try
                        test.Test_ac(f'{contest_c}/{xc}',
                                     'Test_files', xc, lang, s)
                    elif(inp == 'race'):  # complete
                        contest.race(s, contest_c)
                    elif(inp == "parse" and choice == "p"):
                        try:
                            make_dir.parse(s, contest_c, choice)
                        except:
                            logout(s)
                    elif(inp == "open" and choice == 'p'):
                        webbrowser.open(
                            f"https://www.codechef.com/problems/{contest_c}")
                    elif(inp == 'test' and choice == 'p'):
                        ti1 = time.time()
                        test.Test("Practice", lang, contest_c)
                        # print(time.time()-ti1)
                    elif(inp == "ctest" and choice == 'p'):
                        test.Test_ac(
                            f'Practice/{contest_c}', 'Test_files', contest_c, lang, s)
                    elif(inp == "submit" and choice == "p"):
                        try:
                            if(one_time_login == 0):
                                while(1):
                                    print(
                                        colored("Logging in...", "green"), end="\r")
                                    p = s.get(
                                        "https://www.codechef.com/", headers=headers)
                                    soup = bs4.BeautifulSoup(
                                        p.text, 'html.parser')
                                    if(type(soup) != type(None)):
                                        break
                                a = soup.find('input', attrs={"name": 'form_build_id'})[
                                    'value']
                                payload['form_build_id'] = a
                                r = s.post('https://www.codechef.com/',
                                           data=payload, headers=headers)
                                print(colored("Logged in     ", "green"))
                                one_time_login = 1
                            ti2 = time.time()
                            submit(s, contest_c, lang, 'p')
                            # print(time.time()-ti2)
                        except:
                            logout(s)
                    elif(inp == "help"):
                        print(colored("parse - Parsing Contest or Problem\nsubmit-Submitting Problem\nopen-Opening question\ntest-To test your cases against standard io\nctest-To test custom cases against custom io\nquit-To leave the current mode", "cyan"))
                    elif(inp == "quit"):
                        break
            elif(li[0] == "upcontest"):
                with requests.Session() as s:
                    contest.get_comp(s, 0, 1)
                print("Upcoming contests")
            elif(li[0] == "prcontest"):
                with requests.Session() as s:
                    contest.get_comp(s, 0, 0)
                print("Present Contests")
            elif(li[0] == "pacontest"):
                with requests.Session() as s:
                    contest.get_comp(s, 0, 2)
                print("Past Contests")
            elif(li[0] == "race"):
                with requests.Session() as s:
                    #cont = input("Enter name of contest: ")
                    contest.race(s, li[1])
                #print("Entering Race")
            elif(li[0] == "help"):
                print(colored("c <Contest Name> - To enter codechef in contest mode\np <Question Name> - To enter codechef in practice mode\nupcontest - To view upcoming contests\nprcontest - To view present contests\npacontest - To view past contests\nrace - To parse contest as soon as contest start\nquit - to logout and quit the program", "cyan"))

            elif(li[0] == "quit"):
                logout(s)
                break


if __name__ == "__main__":
    one_time_login = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'cache-control': 'private, max-age=0, no-cache'
    }
    a = time.time()
    login()  # better structure needed
    # print(time.time()-a)
