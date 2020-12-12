def changeUserData(rowOfUser):
    accFile = open('accounts.txt', 'r')
    fileContent = accFile.readlines()
    rowList = fileContent[rowOfUser].split()
    # checks if the password is same as the old one, if its right then the new password is added in the text file instead the old one
    while 1:
        username = input("Enter your username: ")
        if username == rowList[4]:
            username = input("Enter your new password: ")
            rowList[4] = newPassword
            newRow = " ".join(rowList)
            fileContent[rowOfUser] = newRow
            content = "\n".join(fileContent)
            with open('accounts.txt', 'w') as file:
                file.write(content)
                return 1
        else:
            print("Wrong password entered")
