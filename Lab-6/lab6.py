import pandas as pd
from pathlib import Path

# Step 1:

# Need to path externally
DATA = Path(__file__).resolve().parent.parent.parent / "dcp26" / "data"

students = []

 # Step 4: pass or fail

def results(student):
    totalmark = (student[engagement]*0.2) + (student[assignment]*0.3) + (student[exam]*0.5)

    if totalmark >= 40:
        return "Pass"
    else: return "Fail"


with open(DATA / "exams.prn") as f:
    header = f.readline() # Read (and skip) the first time
    #for line in f:
      #  print(line, end="") # Print each line that ends in \n

    

    # Step 2:

    for line in f:
        lname = line[0:14].strip()
        fname = line[14:25].strip()
        #print(f"Name: {lname}, {fname}")

        number = line[25:42].strip()
        #print(f"Number: {number}")
        
        engagement = line[42:56].strip() or "0"
        #print(f"Engagement: {engagement}")

        assignment = line[56:58].strip() or "0"
        #print(f"Assignment: {assignment}")
        
        exam = line[68:80].strip() or "0"
        #print(f"Name: {exam}\n\n")


        # Step 3: Storing them in an list of students with details
    
        student = {
            "last": lname,
            "first": fname,
            "number": number,
            "engagement": int(engagement),
            "assignment": int(assignment),
            "exam": int(exam)
            }
        student["result"] = results(student)
        students.append(student)


# Step 5: menu

    while True:
        count = 0
        print("Student Management System")
        print("1. All marks")
        print("2. Pass")
        print("3. Fail")
        print("4. Find student")
        print("5. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "5":
            break;

        if choice == "4":
            search = input("Enter Student Number: ").strip()
            found = False
            for s in students:
                if s["number"] == search:
                    print(f"Name: {s['last']}, {s['first']}")
                    print(f"Number: {s['number']}")
                    print(f"Engagement: {s['engagement']}")
                    print(f"Assignment: {s['assignment']}")
                    print(f"Exam: {s['exam']}")
                    print(f"Total: {s['total']:.1f}")
                    print(f"Result: {s['result']}")
                    found = True
                    break

            if not found:
                print("Not student with that number")

        if choice == "2":
            for student in students:
                if student["result"] == "Fail":
                    print(f"{student['last']},
                     {student['first']},
                     {student['number']},
                     {student['engagement']},
                     {student['assignment']},
                     {student['exam']},
                     {student['total']:.1f},
                     {student['result']}")
                    count = count+1

        if choice == "2":
            for student in students:
                if student["result"] == "Pass":
                    print(f"{student['last']},
                     {student['first']},
                     {student['number']},
                     {student['engagement']},
                     {student['assignment']},
                     {student['exam']},
                     {student['total']:.1f},
                     {student['result']}")
                    count = count+1    

        if choice == "1":
        for student in students:
            print(f"{student['last']},
                  {student['first']},
                  {student['number']},
                  {student['engagement']},
                  {student['assignment']},
                  {student['exam']},
                  {student['total']:.1f},
                  {student['result']}")


        else:
            print("Invalid option")


   
    #for student in students:
        #print(student)

    #print(len(students))

