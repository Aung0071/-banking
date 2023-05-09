import mysql.connector
name = input('Hello welcome to Cha Ching bank, what is your name?: ')
Money = 0
subtract = 0
Username = ""
Password = ""

def Makeaccount():
  global Username
  global Password
  while True:
    Username = input('Please input a username: ')
    if len(Username) >= 5:
      break
    else:
      print('Username too short, please input a username with 5 or more characters')
  while True:
    Password = input('Please input a password: ')
    if len(Password) >= 5:
      break
    else:
      print('Password too short, please input a password with 5 or more characters')
  print(f'Welcome {Username} to Cha Ching banking!')


def Deposit():
  global Money
  while True:
    try:
      Money += int(input(f'How much would you like to deposit into {Username}?: '))
      break
    except ValueError:
      print('Please input a valid number!')
    print(f'{Money} has been deposited into {Username}')


def Withdraw():
    global Money
    global subtract
    Sec = input(f'What is the password to {Username}?: ')
    if Sec == Password:
        while True:
            try:
                takeout = int(input(f'How much would you like to withdraw from {Username}?: '))
                if takeout > Money:
                    print("You're withdrawing more money than you have!")
                else:
                    subtract = Money - takeout
                    Money = subtract
                    print(f"You now have {Money} in {Username}")
                    break
            except ValueError:
                print('Please input a valid number!')
    else:
        print('Wrong password! Taking you back to home page.')


def Checkbalance():
    print(f'You currently have {Money} in {Username}')


def Modifyaccount():
  global Password
  global Username
  actions = input(f'''What do you wish to do with {Username}?

(1) Change password
(2) Delete account
(3) Go back

''')
  if actions == '1':
    Change = input(f'What is the current password to {Username}?: ')
    if Change == Password:
        Newpassword = input('What is your new password?: ')
        Password = Newpassword
        print(f'Your new password is {Password}')
    else:
        print('Incorrect password. Taking you back to the home page!')
  elif actions =='2':
    Del = input(f'What is the password to {Username}?: ')
    if Del == Password:
        print('Account successfully terminated')
        
        Username = ""
        Password = ""
        Money = 0
        subtract = 0
    else:
        print('Incorrect password. Taking you back to the home page!')

  if actions == '3':
    print('Going back to home page...')
  

while True:
    action = input(f'''Welcome, {name}! What would you like to do?

(1) Make an account
(2) Deposit
(3) Withdraw
(4) Check balance
(5) Settings
(6) Leave

''')

    if action == '1':
        Makeaccount()
    elif action == '2':
        if not Username:
            print('Invalid, do not have an account assoiated with Cha Ching banking')
        else:
            Deposit()
    elif action == '3':
        if not Username:
            print('Invalid, do not have an account assoiated with Cha Ching banking')
        else:
            Withdraw()
    elif action == '4':
      if not Username:
        print('Invalid, do not have an account assoiated with Cha Ching banking')
      else:
        Checkbalance()

    elif action == '5':
      if not Username:
        print('Invalid, do not have an account assoiated with Cha Ching banking')
      else:
        Modifyaccount()
    elif action == '6':
      break

