import random

def upLow(strr):
    if catchInt(strr):
        return "num"
    if strr == " ":
        return "space"
    if strr.islower():
        return "lower"
    if strr.isupper():
        return "upper"
    else: 
        return "char"

def catchInt(i):
    try:
        i = int(i)
        return True
    except:
        return 
        
def tilt():
    n = random.randint(0, 5)
    if (n == 1):
        return True
    else:
        return False