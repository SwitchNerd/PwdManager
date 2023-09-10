import random

def pwdgener ():
    
    #variables
    chars = 'qwertyuiopasdfghjklzxcvbnmASDFGHJKLQWERTYUIOPZXCVBNM1234567890'
    
    length = int(input("Password length: "))
    password = ''
    for i in range (length):
        password += random.choice(chars)
    return password