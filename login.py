def loginScreen():
    # login function

    print("Login\n")

    accFile = open('accounts.txt', 'r')
    fileContent = accFile.readlines()
    usernameList = []
    firstNameList = []
    passwordList = []
    userTypeList = []
    for line in fileContent:
        usernameList.append(line.split()[0])  # gets all usernames and creates a list
        firstNameList.append(line.split()[1])  # gets all first names and creates a list
        passwordList.append(line.split()[4])  # gets all passwords and creates a list
        userTypeList.append(line.split()[5])  # gets all user types and creates a list
    accFile.close()

    username = input("Enter your username: ")
    pwd = input("Enter your password: ")
    try:
        try:


            if usernameList.index(username) > -1 and passwordList[usernameList.index(username)] == pwd:  # check if the index of the username matches the index of the password
                rowOfUser = usernameList.index(username)
                firstName = firstNameList[rowOfUser]
                userType = userTypeList[rowOfUser]
                return [rowOfUser, firstName, userType]
            else:
                print("The password is incorrect, please try again!")
                loginScreen()
        except ValueError:
            print("No such password")
            loginScreen()
    except ValueError:
        print("No such username found")
        loginScreen()
    return 0
