# IMPORTS
import os
import datetime
import subMethods
""" 
= = = NEED TO ENCHANCE = = =
> Added [PAY] command:
    * [FULL] and [PART] merged to a single command: [PAY]
    * [PAY] should automatically update the profile's database
    * If balance reaches zero? It will update customer's status.
    * [PAY] command should replace the [CHECK] in Profile MENU.
        * SELECT-MENU [VIEW/ADD/PAY?/BACK/EXIT]
> [SELECT] command update:
    * When used, total amount due will be shown after viewing data.
"""
# GLOBALS
viewAll_path = "./allProfiles.txt"
profileFolder_path = "./allProfiles/"

# [VIEW] CODE SECTION
def viewAllProfiles():
    print("Viewing the list of all profiles in the database...")
    with open(viewAll_path, "r") as f:
        viewContent = f.read()
        print(viewContent)
# [ADD] CODE SECTION
def addAProfile():
    # Adds the profile name to the allProfiles.txt file
    print("You can now add a new profile. ")
    print("Enter (x) to cancel and go back to Main Menu.")
    customerName = input("Please enter customer name: ")
    if customerName == 'x':
        print("Operation cancelled.\n" 
                "Going back to Main Menu...\n")
        return 0  # Will return nothing, hence will go back to main menu.
    with open(viewAll_path, "r") as f:
        content = f.read()
        num = subMethods.file_lineCounter(content)  # Submethod
    final_num, final_name = subMethods.inputEditor(str(num - 1), customerName)  # Submethod
    with open(viewAll_path, "a") as f:
        f.write(f"{final_num}|{final_name}|{subMethods.dateToday()}    |\n")

    # Create a file for this specific profile.
    complete_profileFolder_path = profileFolder_path + str(num - 1) + "." + customerName.title().replace(" ", "_") + ".txt"
    with open(complete_profileFolder_path, "a") as f:  
        f.write(f"{customerName.title()} | Date: {subMethods.dateToday()}\n")
        f.write(f"*   |product name        |price |date\n")  # 4 | 20 | 6 | date

    # Notification
    print(f'Added "{customerName.title()}" to the database.\n')
# [SELECT] CODE SECTION
def selectAProfile():
    print("Viewing the database...")
    with open(viewAll_path, "r") as f:  # opens "allProfiles.txt" file, read mode.
        viewAllContent = f.read()
        print(viewAllContent)
    print("Select a profile by entering it's corresponding profile ID.")
    customerId = int(input("Enter profile ID no: "))
    print("")  # new line, space
    selectedPath = profileFolder_path + subMethods.pathGenerate(viewAllContent, customerId) # subMethods.py
    # SELECT-MENU [VIEW/ADD/CHECK/BACK/EXIT]
    isRepeat2 = True
    while isRepeat2:
        with open(selectedPath, "r") as f:  # opens user-input "customerId" txt file, read mode.
            viewContent = f.read()
            total = subMethods.file_TotalCalculator(viewContent)
            print(f"{viewContent}Total due amount: {total}\n")
        print("= = Profile MENU = =")
        command = input("Select your desired command: \n"
                    "[VIEW] View profile\n"
                    "[ADD] New Entry\n"
                    "[PAY] Pay now?\n"
                    "[BACK] Back to menu\n"
                    "[EXIT] Exit application\n"
                    "User-input: ").upper()
        print(f"User uses the command '[{command}]'\n")
        # [VIEW] CODE SECTION
        if command == 'VIEW':
            with open(selectedPath, "r") as f:  # opens user-input "customerId" txt file, read mode.
                viewContent = f.read()
                print(viewContent)
        # [ADD] CODE SECTION
        elif command == 'ADD':
            isDone = False
            while not isDone:
                print("Enter (x) to cancel and go back to Main Menu.")
                productName = input("Enter product name: ").capitalize()
                quantity = input("Quantity: ")
                price = input("Price per item: ")
                if productName == 'x' or productName == 'X' or quantity == 'x' or quantity == 'X' or price == 'x' or price == 'X':
                    print("Operation cancelled.\n" 
                            "Going back to Main Menu...\n")
                    return 0  # will return nothing and go back to Main Menu.
                totalPrice = int(price) * int(quantity)
                with open(selectedPath, "a") as f:  # opens user-input "customerId" txt file, append mode.
                    f.write(subMethods.inputEditor2(str(quantity), productName, str(totalPrice)) + subMethods.dateToday() + "\n")  # subMethods.py
                    print(f'\nAdded {quantity} * {productName} @ {price} each| Total: {totalPrice}')  # detailed report
                addAgain = input("Add new entry again? \n"
                            "Press any key if (Yes), enter (X) if not.\n"
                            "User-input: ").upper()
                print("")  # new line, space
                if addAgain == 'X':
                    isDone = True
        # [PAY] CODE SECTION
        elif command == 'PAY':
            # ASK FOR DETAILS
            print(f"Balance: {total}")
            paymentAmount = input("Payment amount: ")
            diffAmount = int(total) - int(paymentAmount)
            # COMPUTATIONS
            print(f"= = = = = = = = \n"
                            f"Credit amount: {str(total)}\n"
                            f"Paid amount: {str(paymentAmount)}")
            if diffAmount <= 0:  # Means fully paid, change(?)
                print(f"Change amount: {str(diffAmount * -1)}")
            elif diffAmount > 0:
                print(f"Remaining balance: {str(diffAmount)}")
            # Y/N - CONFIRMING DETAILS
            isConfirmed = False
            while not isConfirmed:
                confirmation = input("Check every details. Shall we proceed? (Y/N): ").upper()
            # Y - UPDATING THE PROFILE
                if confirmation == 'Y':
                    with open(selectedPath, "a") as f:  # opens user-input "customerId" txt file, append mode.
                        print(f"paymentAmount: {int(paymentAmount) * -1}")
                        f.write(subMethods.inputEditor2("*", "PAYMENT", str(int(paymentAmount) * -1)) + subMethods.dateToday() + "\n")
            # Y - IF(?)VIEWING THE UPDATED DATABASE/PROFILE
                    if diffAmount <= 0:
                        with open(selectedPath, "a") as f:  # opens user-input "customerId" txt file, append mode.
                            f.write(f"\nFully paid the remaning balance of {total}\n"
                                    f"\twith the amount of {paymentAmount}\n"
                                    f"\twith a change of {str(diffAmount * -1)}.\n"
                                    f"Checked by: Ac Villarin, {subMethods.dateToday()}\n")
                        with open(viewAll_path, "w") as f:  # opens "allProfiles.txt" file, write mode.
                            print("")  # new line, space
                            print("Viewing the updated database...")
                            updatedStatus = subMethods.statusAdder(viewAllContent, customerId)  # subMethods.py
                            f.write(updatedStatus)
                    isConfirmed = True
                    isPaymentMenuDone = True  # back to SELECT-MENU [VIEW/ADD/PAY/BACK/EXIT]
            # N - GOING BACK TO PROFILE-MENU
                elif confirmation == 'N':
                    print("Going back to the profile menu...\n")
                    isConfirmed = True
                    isPaymentMenuDone = True  # back to SELECT-MENU [VIEW/ADD/PAY/BACK/EXIT]
                else:
                    print("Unknown command. Enter a correct command!\n")
        # [BACK] CODE SECTION
        elif command == 'BACK':
            isRepeat2 = False
        # [EXIT] CODE SECTION
        elif command == 'EXIT':
            quit()
        else:
            print("Enter a correct command!")

print("Credit App | Created by AC")
# MAIN MENU [VIEW/NEW/SELECT/EXIT]
isRepeat = True
while isRepeat:  # Will force user to enter a correct command
    print("= = MAIN MENU = =")
    command = input("Enter your command: \n"
            "[VIEW] View all profiles \n"
            "[NEW] Add a new profile \n"
            "[SELECT] Select a profile \n"
            "[EXIT] Exit application \n"
            "User-input: ").upper()
    print(f"User uses the command '[{command}]'\n")
    if command == 'VIEW':
        viewAllProfiles()
    elif command == 'NEW':
        addAProfile()
    elif command == 'SELECT':
        selectAProfile()
    elif command == 'EXIT':
        print("Closing the app... Bye!")
        quit()
    else:
        print("Incorrect command! Enter again.")