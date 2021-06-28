import random
import csv
import os.path
import os
from word_list import adj, nouns, symbols

###
class colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
###


print("Welcome to Password Generator!")

loop = 1
while loop == 1:
    symbolOption = input("Do you want to include a symbol? y/n: ")
    if symbolOption == "y":
        symbol = (random.choice(symbols))
        loop = 0
    elif symbolOption == "n":
        symbol = ""
        loop = 0
    else:
        print("Please enter 'y' for yes or 'n' for no.")

loopTwo = 1
while loopTwo == 1:
    numOption = input("Do you want to include a number? y/n: ")
    if numOption == "y":
        loopThree = 1
        while loopThree == 1:
            numAmount = input("How many numbers would you like to include? (1-3): ")
            if numAmount == "1":
                num = (random.randrange(10))
                loopTwo = 0
                loopThree = 0
            elif numAmount == "2":
                num = (random.randrange(11, 99))
                loopTwo = 0
                loopThree = 0
            elif numAmount == "3":
                num = (random.randrange(100, 999))
                loopTwo = 0
                loopThree = 0
            else:
                print("Please enter a number between 1 and 3.")
    elif numOption == "n":
        num = ""
        loopTwo = 0
    else:
        print("Please enter 'y' for yes or 'n' for no.")

word1 = random.choice(adj)
word2 = random.choice(adj)
word3 = random.choice(nouns)

password = word1.capitalize() + word2.capitalize() + word3.capitalize() + symbol + str(num)

print("Your password is: " + colour.BOLD + password + colour.END)

storeLoop = 1
while storeLoop == 1:
    store = input("Do you want to store the password? (y/n): ")
    if store == "y":
        storeLoop = 0
        # Gives the password a tag so the user can remember which password is for what
        tag = input("What is this password for?: ")

        # Asks the user to provide a username (Can be left blank)
        usr = input("What is the username?: ")

        # Determines the users windows username so the file can be saved to the desktop
        username = os.getlogin()

        # Determines if the password file exists already or not
        isFile = os.path.isfile(f"C:/Users/{username}/Desktop/passwords.csv")

        # If it exists, the new tag and password are added
        if isFile is True:
            with open(f"C:/Users/{username}/Desktop/passwords.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([tag, usr, password])
                print("Your password has been stored.")

        # Creates the csv file on the desktop and fills it with the password and tag (Could ask for directory?)
        else:
            with open(f"C:/Users/{username}/Desktop/passwords.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Tag", "Username", "Password"])
                writer.writerow([tag, usr, password])
                print("Your password has been stored.")

    elif store == "n":
        storeLoop = 0
    else:
        print("Please enter 'y' for yes or 'n' for no.")

print("Thank you for using Password Generator!")
