import sys
from db import Db

openingTxt = ['  _______ _____ _______       _   _ ',' |__   __|_   _|__   __|/\\   | \\ | |',
         '    | |    | |    | |  /  \\  |  \\| |','    | |    | |    | | / /\\ \\ | . ` |',
         '    | |   _| |_   | |/ ____ \\| |\\  |','    |_|  |_____|  |_/_/    \\_\\_| \\_|', '', 'Created By:', '  Zane Bellefeuille',
         '  Brady Bhalla', '  Tim Roberts', "Type 'help' to display functions."  ]

run = True
loggedIn = False
db = Db()

def exit():
    db.exit()
    sys.exit()
