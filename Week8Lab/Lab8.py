import pandas as pd
import numpy as np
from pathlib import Path

df = pd.read_csv(Path(__file__).parent/"exams.csv")

def step1(): # Function to display certain aspects of the CSV
    df.head()
    len(df)
    df.info() # Columns and types

def step2(): # Step 2 (Getting rid of Nulls and replacing with 0s)


    #print(df.isna().sum()) # Shows where null values are present

    empties = ["engagement", "assignment", "exam"]
    df[empties] = df[empties].fillna(0) # Filling empty slots with 0
    df[empties] = df[empties].astype(int) # Changing column types to int

    #print(df.isna().sum())
    #df.info()

step2() # Running so that the NULLs are filled

def step3(): # Step 3: Displaying each row in a nice consise format

    for index, exams in df.iterrows():
        print(f"Name: {exams['last']}, {exams['first']}")
        print(f"Number: {exams['number']}")
        print(f"Engagement: {exams['engagement']}")
        print(f"Assignment: {exams['assignment']}")
        print(f"Exam: {exams['exam']}\n")

# Step 4: Adding New Columns with row calculations

# (engagement x 0.2) + (assignment x 0.3) + (exam x 0.5), round to 1 dp
df["total"] = (df["engagement"]*0.2) + (df["assignment"]*0.3) + (df["exam"]*0.5)
df["total"].round(1)

# Pass or Fail (if result is 40 or more)
df["result"] = np.where(df["total"] >= 40, "Pass", "Fail")

df.info()

# Step 5: Adding a menu

# Bonus: Adding a username and password system: E.g. username: Heath, password: taban123 (only display the following menu if they get in, limit of 3 password attempts)

usernames = {"heath", "bryan", "admin"}
passwords = {"heath123", "bryan123", "sudo"}



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

     choice = input("\nChoice: ")

     if choice == "1":
          for index, exams in df.iterrows():
            print(f"{exams['last']}, {exams['first']}, {exams['number']}, {exams['engagement']}, {exams['assignment']}, {exams['exam']}, {exams['total']}, {exams['result']}\n")

     if choice == "2":
         for index, exams in df.iterrows():
            if exams['result'] == "Pass":
                print(f"{exams['last']}, {exams['first']}, {exams['number']}, {exams['engagement']}, {exams['assignment']}, {exams['exam']}, {exams['total']}, {exams['result']}\n")


     if choice == "3":
         for index, exams in df.iterrows():
            if exams['result'] == "Fail":
                print(f"{exams['last']}, {exams['first']}, {exams['number']}, {exams['engagement']}, {exams['assignment']}, {exams['exam']}, {exams['total']}, {exams['result']}\n")


     if choice == "4":
         namefind = input("Please enter Surname: ")

         for index, exams in df.iterrows():
            if exams['last'] == namefind:
                print(f"{exams['last']}, {exams['first']}, {exams['number']}, {exams['engagement']}, {exams['assignment']}, {exams['exam']}, {exams['total']}, {exams['result']}\n")


    # Add a menu option that lists the incomplete records (any missing mark) separately.
     if choice == "5":
         for index, exams in df.iterrows():
            if df.isna().sum():
                print(f"{exams['last']}, {exams['first']}, {exams['number']}, {exams['engagement']}, {exams['assignment']}, {exams['exam']}, {exams['total']}, {exams['result']}\n")


    # Add a menu option that saves the All marks output to a file called results.csv.

    # Sort the output by last name, or by total mark from highest to lowest.

     if choice == "7":
         print("\nGoodbye.")
         break;

     else: print("\nNot a Valid option\n")
         

