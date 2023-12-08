from inventory import Inventory
from cart import Cart
from user import User

def initialMenu():
    while not user.getLoggedIn():
        print("Welcome To Our Book Store!!")
        print()
        print("Menu:")
        print("1. Login to an existing account")
        print("2. Create a new account")
        print("3. Quit")
        print()
        selection = int(input("Select an option: "))
        print()

        if selection == 1:
            user.login()
        elif selection == 2:
            user.createAccount()
        elif selection == 3:
            print("Understandable. Have a nice day!")
            break
        else:
            print("Invalid option.")

    if user.getLoggedIn():
        afterLogin()

def afterLogin():
    while user.getLoggedIn():
        print("Options:")
        print("1. Log out")
        print("2. View account information")
        print("3. Inventory information")
        print("4. Cart information")
        print()
        selection = int(input("Select an option: "))
        print()

        if selection == 1:
            user.logout()
            initialMenu()
        elif selection == 2:
            user.viewAccountInformation()
        elif selection == 3:
            inventoryInfo()
        elif selection == 4:
            cartInfo()
        else:
            print("Invalid option.")

def inventoryInfo():
    inventory = Inventory(databaseName='MainDatabase.db', tableName='Inventory')

    while user.getLoggedIn():
        print("Options:")
        print("1. View the inventory")
        print("2. Search inventory")
        print("3. Go back")
        print()
        selection = int(input("Select an option: "))
        print()

        if selection == 1:
            inventory.viewInventory()

        elif selection == 2:
            while user.getLoggedIn():
                inventory.searchInventory()
                searchAgain = input("Do you want to search another book? (yes/no): ")
                print()
                if searchAgain.lower() == "yes":
                    continue
                elif searchAgain.lower() == "no":
                    break
                else:
                    print("Wrong selection.")

        elif selection == 3:
            break

        else:
            print("Invalid option.")

def cartInfo():
    cart = Cart()

    print("Options:")
    print("1. Go back")
    print("2. View cart")
    print("3. Add items to cart")
    print("4. Remove an item from cart")
    print("5. Check out")
    print()
    selection = int(input("Select an option: "))
    print()

    if selection == 1:
        afterLogin()
    elif selection == 2:
        cart.viewCart(user.getUserID())
    elif selection == 3:
        ISBN = input("Enter the ISBN of the book you want to add: ")
        cart.addToCart(user.getUserID(), ISBN)
    elif selection == 4:
        ISBN = input("Enter the ISBN of the book you want to remove: ")
        cart.removeFromCart(user.getUserID(), ISBN)
    elif selection == 5:
        cart.checkOut(user.getUserID())
    else:
        print("Invalid option.")



if __name__ == "__main__":
    user = User()
    initialMenu()
