import getpass
import time
import choices
from setup import *

# prints opening text
for i in openingTxt:
    print(i)
    time.sleep(0.5)
print()

# main loop
while run:
    x = input(">>> ")
    if x == "exit":
        exit()
    else:
        choices.execute(x)
    

exit()
