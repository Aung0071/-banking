name = input('Hello welcome to Cha Ching bank, what is your name? ')
action = input(f'welcome, {name} what would you like to do? ')


def Makeaccount():
    global Username
    global Password
    while True:
        Username = input('Please input a username: ')
        if len(Username) >= 5:
            break
        else:
            print('username to short please input username with 5 or more characters')
    while True:
        Password = input('Please input a password: ')
        if len(Password) >= 5:
            break
        else:
            print('username to short please insert password with 5 or more characters')
    print(f'Welcome {Username} to Cha Ching banking!')

def Deposit():
    global Money
    while True:
        try:
            Money = int(input(f'How much would you like to deposit into {Username}?: '))
            break
        except ValueError:
            print('please input a valid number!')

    
    print(f'{Money} has been deposited into {Username}')

def Withdraw():
    global Newcash
    global subtract
    Sec = input(f'what is the password to {Username}?: ')
    if Sec == (Password):
        while True:
            try:
                takeout = int(input(f'How much would you like to withdraw from {Username}?: '))
                if takeout > Money:
                    print('looks like your gonna be in dept!')
                else:
                    subtract = Money - takeout
                    break
            except ValueError:
                print('please input a valid number!')
                
        
        Newcash = print(f'you now have {subtract} in {Username}')
    else:
        print('FRAUD DETECTED GET OUT OF THIS ACCOUNT! Now everything will be reset this is how we ensure our bank is totally safe -_-')

                

Makeaccount()
Deposit()
Withdraw()
