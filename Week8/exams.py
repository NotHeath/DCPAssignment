import pandas as pd
import numpy as np
from pathlib import Path 
from getpass import getpass # Adding to not display the password on screen

# New learning: Getpass
# New learning: add.axis=1
# New learning: __name__ - Stops import from taking over the main
# New learning: .strip()
# New learning: .round()
# New learning: df.drop()

# .to_csv(output_file, index=False) writes the file.
# Without index=False, pandas would add an extra column of row numbers (0, 1, 2...).

# To-do list: Sort the output by last name, or by total mark from highest to lowest.

df = pd.read_csv(Path(__file__).parent/"exams.csv")

empties = ["engagement", "assignment", "exam"]
maxattempts = 3

USERS = {
    "heath": "heath123",
    "bryan": "bryan123",
    "admin": "sudo"
}


# Bonus: Adding a username and password system:
def login():

    for attemptsleft in range(maxattempts -1, -1, -1):
        username = input("Username: ").strip().lower()
        password = getpass("Password: ")

        if USERS.get(username) == password:
            print(f"\nWelcome, {username}!\n")
            return True

        print(f"Incorrect username or password. Attempts left: {attemptsleft}\n")

    return False

def step1(): # Function to display certain aspects of the CSV
    df.head()
    len(df)
    df.info() # Columns and types

def step2(): # Step 2 (Getting rid of Nulls and replacing with 0s)

    #print(df.isna().sum()) # Shows where null values are present
    df[empties] = df[empties].fillna(0) # Filling empty slots with 0
    df[empties] = df[empties].astype(int) # Changing column types to int

    #print(df.isna().sum())
    #df.info()

def step3(): # Step 3: Displaying each row in a nice consise format

    for index, exams in df.iterrows():
        print(f"Name: {exams['last']}, {exams['first']}")
        print(f"Number: {exams['number']}")
        print(f"Engagement: {exams['engagement']}")
        print(f"Assignment: {exams['assignment']}")
        print(f"Exam: {exams['exam']}\n")

def step4(): # Step 4: Adding New Columns with row calculations

    # (engagement x 0.2) + (assignment x 0.3) + (exam x 0.5), round to 1 dp
    df["total"] = (df["engagement"]*0.2) + (df["assignment"]*0.3) + (df["exam"]*0.5)
    df["total"] = df["total"].round(1) 

    # Pass or Fail (if result is 40 or more)
    df["result"] = np.where(df["total"] >= 40, "Pass", "Fail")

    #df.info()

def print_students(df): # Making a function to call the printing so that I dont have to rewrite the printing everytime
    for index, s in df.iterrows():
        print(f"{s['last']}, {s['first']}, {s['number']}, {s['engagement']}, {s['assignment']}, {s['exam']}, {s['total']}, {s['result']}\n")

# Add a menu option that lists the incomplete records (any missing mark) separately.
def incompleterecords():
    df["incomplete"] = df[empties].isna().any(axis=1) # any.axis=1 (Reduces each row to "is anything in this row True") 

# Step 5: Adding a menu
def step5menu():
        
    while True:
        print("--------------------------------")
        print("Student Management System: ")
        print("--------------------------------")
        print("1. All Marks")
        print("2. Pass")
        print("3. Fail")
        print("4. Find Student")
        print("5. Incomplete Records")
        print("6. Save all marks to results.csv")
        print("7. Quit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            print_students(df)
            
        elif choice == "2":
           print_students(df[df["result"] == "Pass"]) # Checks if results are = Pass

        elif choice == "3":
            print_students(df[df["result"] == "Fail"]) # Same again with dail

        elif choice == "4":
            namefind = input("Please enter Surname: ")

            print_students(df[df["last"] == namefind])

        elif choice == "5":
            print_students(df[df["incomplete"]])
            print("^ If nothing is displays then there are no incomplete tables ^")

        # Add a menu option that saves the All marks output to a file called results.csv.
        elif choice == "6":
            savingfile = Path(__file__).parent / "results.csv"
            df.drop(columns="incomplete").to_csv(savingfile, index=False) # Removes the incomplete column
            print(f"\nSaved all marks to {savingfile}\n")

        elif choice == "7":
            print("\nGoodbye.")
            break

        else: print("\nNot a Valid option\n")


incompleterecords() # Run to scan for non-filled records (step 2 then cleans it up)
step2() # Running so that the NULLs are filled
step4() # Running so that the new columns are added


def main(): # Main checks the login condidtion and only shoots the menu function if successful
    if not login():
        print("Too many attempts. Closing app")
        return

    step5menu() # Runs if they get the login

# Run the program
if __name__ == "__main__": # It lets your file run as a program when started directly, while stopping main() from running automatically when another file imports it.
    main()