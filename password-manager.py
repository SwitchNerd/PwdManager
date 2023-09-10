# Install module (pip install cryptography)
from cryptography.fernet import Fernet
#importing random generator
from generator import pwdgener

def main():
    
    #main variables
    master_pwd = input("Master Password: ")
    key = load_key()
    global fer
    fer = Fernet(key)
    
    if master_pwd == "": #Change to prefered masterpassword
        while True:
            Options = input("Would you like to view or add accounts? (view, add) ('stop' to exit): ").lower()
            if Options == 'stop':
                break
            elif Options == 'add':
                add()
            elif Options == 'view':
                view()
            else:
                print("Error occured: invalid option")
                
    else: 
        print("Incorrect password")
    
    
def add():
    name = input("Enter account name: ")
    pwd = input("Enter a password or generate a random one (generate): ")
    if pwd == 'generate':
        pwd = pwdgener()
    
    with open('passwords.txt', 'a') as file:
        file.write(f'{name}|{fer.encrypt(pwd.encode()).decode()}\n')
        
def view(): #Example password in passwords.txt
    with open('passwords.txt', 'r') as file: 
        for line in file.readlines():  
            data = line.rstrip()
            user, password = data.split("|")
            print(f"User: {user} | Password: {fer.decrypt(password.encode()).decode()}")
            
''' # Don't run again

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''
        
        
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

#add function to delete from passwords.txt
def delete():
    pass

main()