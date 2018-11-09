import re
import webbrowser
from datetime import datetime
from db import Db
import getpass
import subprocess
import os
import stocks

# show time
def showTime():
    print(datetime.now().strftime("%m/%d/%Y %I:%M %p"))
# open browser
def openWebpage(x):
    webbrowser.get( \
    "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(str(x))
# create account
def createAccount():
    db = Db()
    if db.createAccount(input("Username: "), getpass.getpass("Password: ")):
        print("Account created.")
    else:
        print("An error occured.")
    db.exit()
# delete account
def deleteAccount():
    db = Db()
    if db.deleteAccount(input("Username: ")):
        print("Account deleted.")
    else:
        print("This username was not previously recorded in my database.")
    db.exit()
# list users
def listUsers():
    db = Db()
    users = db.listUsers()
    for i in users:
        print(i)
# start programs
def start(x):
    subprocess.call(("start", x), shell=True)
# echo text
def echo(x):
    print(x)
# play blackjack
def blackjack():
    os.system('blackjack.py')
# plot stocks
def plotStocks(x):
    stocks.plot(x)
#help
def helper():
    print("""Show time & date - type 'show time'
Open a webpage - type a webpage url (ex. www.google.com).
Start programs - type 'start' and then a program.
Echo Text - type 'echo' and then your text.
Play Blackjack - type 'blackjack'.
Plot stocks - type 'plot stock' and then the stock's NASDAQ (ex. AAPL = Apple).""")
# checks functions
def check(x, action, *args, **kwargs):
    if x:
        action(*args, **kwargs)
        return True
    else:
        return False

# test every regex
def execute(s):
    try:
        result = re.findall(r'.*\s+(.*\.(?:com|org|net|gov).*)', s)
        if check(result, openWebpage, result[0].strip(".")): return True
    except IndexError:
        pass

    result = re.findall(r'(?:[Tt]ime)(.*)', s)
    if check(result, showTime): return True

    result = re.findall(r'(?:[Oo]pen|[Ss]tart|[Rr]un) (.*)', s)
    if check(result, start, result): return True

    result = re.findall(r'[Bb]lackjack', s)
    if check(result, blackjack): return True

    result = re.findall(r'[Hh]elp', s)
    if check(result, helper): return True
    
    try:
        result = re.findall(r'(?:[Ee]cho|[Pp]rint) (.*)', s)
        if check(result, echo, result[0]): return True
    except IndexError:
        pass
    
    try:
        result = re.findall(r'[Ss]tocks? ?[Ff]?o?r? (.*)', s)
        if check(result, plotStocks, result[0]): return True
    except IndexError:
        pass
    

    return False
    

