#aff612b5dc50a0adfe6fab73017b17bcc5a98971- apikey
# 88085a4f1cedfcc7b6febcf56ca9f92042bca11f - secret
import tkinter
import requests
import time
import hashlib
import math
import webbrowser
from functools import partial


def current_milli_time():
    return round(time.time())


handles = int(input("Enter the number of handles you want to stalk :"))
handle_list = []
for i in range(handles):
    hh = input("Enter handle "+str(i+1)+" ")
    handle_list.append(hh)


# print(data)
while(True):
    k = 1
    
    for j in range(handles):
        
        handle = handle_list[j]
        tim = current_milli_time()
        response = requests.get(
            "https://codeforces.com/api/user.status?handle="+handle+"&from=1&count=10")
        data = response.json()
        if(data['status'] == "FAILED"):
            print(data['comment'])
            continue
        print("last 10 problems solved by ", handle, " are : ")
        
        for i in range(10):
            
            print(data['result'][i]['problem']['index']+" "+data['result'][i]
                  ['problem']['name']+" ", data['result'][i]['problem']['rating'], " ")
            delay1 = (tim-(data['result'][i]['creationTimeSeconds']))
            delay = round((tim-(data['result'][i]['creationTimeSeconds']))/60)
            verdict = data['result'][i]['verdict']
            
            if((delay1 <= 5+k*60+i) and ((verdict == "OK") or (verdict == "PARTIAL"))):
                window = tkinter.Tk()
                url = "https://codeforces.com/problemset/problem/" + \
                    str(data['result'][i]['contestId'])+"/" + \
                    data['result'][i]['problem']['index']
                window.title(" problem solved")
                stri = "your rival " + handle + " has just solved a "+str(data['result'][i]['problem']['rating']) + " rated broblem " + data[
                    'result'][i]['problem']['index'] + " "+data['result'][i]['problem']['name']
                label = tkinter.Label(window, text=stri).grid(row=0, column=0)

                def button1():
                    window.destroy()

                def button2(url):
                    webbrowser.open_new(url)
                    window.destroy()

                bt1 = tkinter.Button(
                    window, text="Do it Later", command=button1).grid(column=1, row=0)
                bt2 = tkinter.Button(
                    window, text="Upsolve Now", command=lambda: button2(url)).grid(column=1, row=1)
                window.mainloop()

        # print(data['result'][i]['creationTimeSeconds'])
        # print(delay)
            if(delay > 60):
                
                hr = math.floor(delay/60)
                if(hr > 24):
                    day = math.floor(hr/24)
                    delay -= hr*60
                    hr -= day*24
                    print(day, "days ", hr, "hours ", delay, "minutes ")
                else:
                    delay -= hr*60
                    print(hr, "hours ", delay, "minutes ")
            else:
                
                print(delay, " minutes")

        time.sleep(1)
    time.sleep(60-handles-1)
