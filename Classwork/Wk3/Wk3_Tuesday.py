# Robert Higgins 07/02/18
# Programming & Scripting - Week 3: Is it Tuesday

import datetime

if datetime.datetime.today().weekday() == 1:
    print("Yay, it's Tuesday!!!")
else:
    print("Unfortunately, it's not Tuesday!!! :-(")

print("Todays Day Number is:", datetime.datetime.today().weekday())
