import random

def pwdgener ():
    print('Intialized')
    
    #variables
    chars = 'qwertyuiopasdfghjklzxcvbnmASDFGHJKLQWERTYUIOPZXCVBNM!@#$%^&*,./;(),1234567890'
    
    amount = int(input("Amount of passwords to generate: "))
    length = int(input("Password length: "))
    
    print("Generating password...")
    
    for x in range (amount):
        password = ''
        for i in range (length):
            password += random.choice(chars)
        print(password)

pwdgener()