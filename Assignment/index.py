# Name: Taban Heath
# Date: 18/11/2026
# Task: Display my csv details with a cli menu interface

import pandas as pd
import numpy as np

df = pd.read_csv("datalist.csv")

# Arroay of the columns to call when needed
cols = ['Day', 'Date', 'Time', 'Transport', 'People',
        'On Phone', 'Reading', 'Nothing/Sleeping']

valid_days = df['Day'].unique() # Checking for unique days

def basicdetails(): # Function to call for displaying basic details
    df.head()
    len(df)
    df.info

def displayclean():
    for index, data in df.iterrows():
        print("\n-------------------------------------------------")
        print(f"Day:  {data['Day']}")
        print(f"Date:  {data['Date']}")
        print(f"Time:  {data['Time']}")
        print(f"Transport:  {data['Transport']}")
        print(f"Total People:  {data['People']}")
        print(f"On phone:  {data['On Phone']}")
        print(f"Reading:  {data['Reading']}")
        print(f"Sleeping / Nothing:  {data['Nothing/Sleeping']}")

def printing_all(df):
    for index, data in df.iterrows():
        print(", ".join(str(data[c]) for c in cols) + "\n")

# printing_all(df)

def themenu():

    while True:
        print("--------------------------------")
        print("Search the CSV: ")
        print("--------------------------------")
        print("1. All Details")
        print("2. Days")
        print("3. Transport type")
        print("4. Average Personnel Details")
        print("5. Update CSV")
        print("6. Quit")

        choice = input("Choice: ").strip()

        if choice == "1":
            basicdetails()
            displayclean()

        elif choice == "2":

            while True:
                daychoice = input("Select a day: ").strip().title()

                if daychoice in valid_days:
                    break
                print("Please enter a valid day (check spelling)")
                
            print("\n\n")
            printing_all(df[df['Day'] == daychoice])

themenu()