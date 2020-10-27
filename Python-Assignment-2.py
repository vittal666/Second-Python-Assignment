usersDetails = {}

# Login authorization
def loginauth(username, password):
    if username in usersDetails:
        if password == usersDetails[username]["password"]:
            return True
    return False

# Checking username or email address is unique or not
def checkForUniqueUsername(username):
    if username in usersDetails.keys():
        return False
    return True
    
# Login
def login():
    while True:
        username = input("\nEnter Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Enter Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break

    if loginauth(username, password):
        print("Login successful!")
    else:
        print("Invalid Username or Password")

# Register or Sign up
def register():
    while True:
        username = input("\nEnter New Username or Email Address: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        else:
            break
    while True:
        password = input("Enter Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    
    if checkForUniqueUsername(username):
        usersDetails[username] = {}
        usersDetails[username]["password"] = password
        print("Account has been created successfully!")
    else:
        print('Please enter a unique Username or Email Address')


# On start
print("Welcome")
while True:
    print("\nPlease select a option: \n 1)Login \n 2)Sign up \n 3)Exit ")
    option = input()
    if option == "Login" or option == "login" or option == "1":
        login()
    elif option == "Sign up" or option == "sign up" or option == "2":
        register()
    elif option == "Exit" or option == "exit" or option == "3":
        usersDetails.clear()
        break
    else:
        print(option + " is not an option")
