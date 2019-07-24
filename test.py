import subprocess
import os
import difflib
import code


def Test(path, lang, varr):
    print("Entering Test")
    try:
        # x=input()
        path = path+'/'+varr
        print(path)
        if lang == "44":
            try:
                print("Coming to try")
                subprocess.call(
                    f"g++ {path}/answer.cpp -o {path}/answer", shell=True)
                print("File compiled")
            except:
                print("Compilation Error g++")
                return
        elif lang == "116":
            try:
                subprocess.call(
                    f"python -m compileall -b {path}/answer.py", shell=True)
            except:
                print("Compilation Error python")
                return
        elif lang == "11":
            try:
                subprocess.call(
                    f"gcc {path}/answer.c -o {path}/answer", shell=True)
            except:
                print("Compilation Error gcc")
                return

        entries = os.listdir(path)
        for entry in entries:
            if entry.endswith('.inp'):
                print(entry)
                if lang == "11" or lang == "44":
                    # print("00")
                    subprocess.call(
                        f"{path}/answer < {path}/{entry} > {path}/{os.path.splitext(entry)[0]}.out", shell=True)
                elif lang == "116":
                    subprocess.call(
                        f"{path}/answer.pyc < {path}/{entry} > {path}/{os.path.splitext(entry)[0]}.out", shell=True)

        for entry in entries:
            if entry.endswith('.out'):
                with open(f"{path}/{entry}", 'r') as file1:
                    with open(f"{path}/{os.path.splitext(entry)[0]}.oac", 'r') as file2:
                        c1 = file1.read()
                        c2 = file2.read()
                        # print(c1)
                        # print(c2)
                        # diff = difflib.context_diff(c1, c2)
                        # print(''.join(diff))
                        # # try:
                        # #     while 1:
                        # #         print(diff.next())
                        # # except:
                        # #     pass
                        d = difflib.Differ()
                        diffs = [x for x in d.compare(
                            c1, c2) if x[0] in ('+', '-')]
                        diffs = list(filter(lambda a: a != '+ \n', diffs))
                        # diffs.replace('+ \n','')
                        # diffs.replace('- \n','')
                        if diffs:
                            print("Your output:")
                            print(c1)
                            print("Required output:")
                            print(c2)
                            print("diffs:")
                            print(diffs)
                        else:
                            print('AC :)')
    except:
        print("Not working")
        pass


def Test_ac(path_code, path_ac, problem, lang, s):
    try:
        # subprocess.call(
        #     f"g++ {path_code}/answer.cpp -o {path_code}/answer", shell=True)
        # print(path_code)
        # print(path_ac)
        # print(problem)
        # print(lang)
        if lang == "44":
            try:
                subprocess.call(
                    f"g++ {path_code}/answer.cpp -o {path_code}/answer", shell=True)
                # print("compiled")
            except:
                print("Compilation Error")
                return
        elif lang == "116":
            try:
                subprocess.call(
                    f"python -m compileall -b {path_code}/answer.py", shell=True)
            except:
                print("Compilation Error")
                return
        elif lang == "11":
            try:
                subprocess.call(
                    f"gcc {path_code}/answer.c -o {path_code}/answer", shell=True)
            except:
                print("Compilation Error")
                return

        subprocess.call(
            f"g++ {path_ac}/{problem}.cpp -o {path_ac}/{problem}", shell=True)
        #print("ac compiled")
        entries = os.listdir(path_code)
        for entry in entries:
            if entry.endswith('.inp'):
                print(entry)
                if(lang == "11" or lang == "44"):
                    #print("in here")
                    subprocess.call(
                        f"{path_code}/answer < {path_code}/{entry} > {path_code}/{os.path.splitext(entry)[0]}.out", shell=True)
                    #print("generated out")
                elif lang == "116":
                    subprocess.call(
                        f"{path_code}/answer.pyc < {path_code}/{entry} > {path_code}/{os.path.splitext(entry)[0]}.out", shell=True)
                subprocess.call(
                    f"{path_ac}/{problem} < {path_code}/{entry} > {path_ac}/{os.path.splitext(entry)[0]}.oac", shell=True)
        # print("1")

        entries_code = os.listdir(path_code)
        for entry_code in entries_code:
            print(entry_code)
            if entry_code.endswith('.out'):
                with open(f"{path_code}/{os.path.splitext(entry_code)[0]}.out", 'r') as file1:
                    # for entry_ac in entries_ac:
                    #     if entry_code.endswith('.oac'):
                    #         with open(f"{path}/{entry_ac}", 'r') as file2:

                    with open(f"{path_ac}/{os.path.splitext(entry_code)[0]}.oac", 'r') as file2:
                        c1 = file1.read()
                        c2 = file2.read()
                        # diff = difflib.context_diff(c1, c2)
                        # print(''.join(diff))
                        # for line in difflib.unified_diff(c1, c2, fromfile='file1', tofile='file2', lineterm='\n'):
                        #    print(line)zz
                        # diff = difflib.ndiff(c1, c2)
                        # delta = ''.join(x[2:] for x in diff if x.startswith('- '))
                        # print(delta)
                        d = difflib.Differ()
                        diffs = [x for x in d.compare(
                            c1, c2) if x[0] in ('+', '-')]
                        diffs = list(filter(lambda a: a != '+ \n', diffs))

                        if diffs:
                            print("Your output:")
                            print(c1)
                            print("Required output:")
                            print(c2)
                            print("diffs:")
                            print(diffs)
                        else:
                            print('AC :)')
    except:
        print("Error Ocuur")
