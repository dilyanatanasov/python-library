from login import loginScreen  # import loginScreen function
from change import changePassword  # import changePassword function
from registerUser import *  # import all functions from registerUser
from addBook import * # import all functions from addBook

def main():
    # Main function
    global flag
    flag = 0  # state flag for the different screens of the system
    endless = 1

    def sysMenus(firstName, userType):
        if len(firstName) == 0:
            firstName = "Someone"

        # Sub-function for the menus after the user has logged in
        if userType == 'admin':
            print(f"""Hello {firstName}, welcome to our platform, please select an option from the menu:             
                        1. Change password
                        2. Register a person
                        3. Edit personal data
                        4. Set expiration date
                        5. Exit                      
                          """)
        elif userType == 'librarian':
            print(f"""Hello {firstName}, welcome to our platform, please select an option from the menu:             
                        1. Change password
                        2. Add new book entries
                        3. Exit   
                          """)
        elif userType == 'reader':
            print(f"""Hello {firstName}, welcome to our platform, please select an option from the menu:
                        1. Exit                      
                          """)
        else:
            print("""Your user type is undefined, contact a system administrator""")
            loginScreen()

    userData = loginScreen()
    while endless:
        userIndexFound = userData[0]
        if userIndexFound > -1:
            firstName = userData[1]
            userType = userData[2]
            sysMenus(firstName, userType)
            selectedOption = int(input("Select Menu option: "))
            if userType == 'admin':
                if selectedOption == 1:
                    changePassword(userIndexFound)
                elif selectedOption == 2:
                    username = input("Username: ")
                    first = input("First Name: ")
                    last = input("Last Name: ")
                    email = input("Email: ")
                    passw = input("Password: ")
                    type = input("User type: ")
                    if createNewUser([username, first, last, email, passw, type]) == 0:
                        print("Username is taken, please pick another one")
                        username = input("Username: ")
                        first = input("First Name: ")
                        last = input("Last Name: ")
                        email = input("Email: ")
                        passw = input("Password: ")
                        type = input("User type: ")
                        createNewUser([username, first, last, email, passw, type])
                    else:
                        print("User has been created")
                elif selectedOption == 5:
                    return loginScreen()
                else:
                    if flag == 0:
                        loginScreen()
            elif userType == 'librarian':
                if selectedOption == 1:
                    changePassword(userIndexFound)
                elif selectedOption == 2:
                    title = input("Book title: ")
                    writer = input("Writer's Name: ")
                    publisher = input("Publisher: ")
                    year = input("Year published: ")
                    genre = input("Genre: ")
                    number = input("Books number: ")
                    available = input("Is the book available: ")
                    if addNewBook([title, writer, publisher, year, genre, number, available]) == 0:
                        print("The book is already in the system! Please, add new book")
                        title = input("Book title: ")
                        writer = input("Writer's Name: ")
                        publisher = input("Publisher: ")
                        year = input("Year published: ")
                        genre = input("Genre: ")
                        number = input("Books number: ")
                        available = input("Is the book available: ")
                        createNewUser([title, writer, publisher, year, genre, number, available])
                    else:
                        print("Book added successfully!")
                elif selectedOption == 3:
                    return loginScreen()
                else:
                    if flag == 0:
                        loginScreen()
            elif userType == 'reader':
                if selectedOption == 1:
                    return loginScreen()


main()
