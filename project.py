"""
program for adding or viewing patient data
"""
import csv
from cs50 import get_int
from rich.console import Console
from rich.traceback import install
import re
from tabulate import tabulate
console = Console()
install()

def main():
    console.print("Welcome!", style="green")
    while True:
        console.print("\nOptions:", style="cyan")
        console.print("1. Add Patient Data", style="cyan")
        console.print("2. View Patient Data", style="cyan")
        console.print("3. Exit", style="cyan")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            PatientIntro()
        elif choice == "2":
            viewData()
        elif choice == "3":
            console.print("Goodbye!", style="green")
            break
        else:
            console.print("Invalid choice. Try again.", style="red")

def PatientIntro():
    introLst = []
    lst = ["male", "female", "neutral"]
    diseases = [
        "flu", "diabetes", "hypertension", "asthma", "arthritis", "tuberculosis", "heart disease", "pneumonia", "malaria"
    ]

    while True:
        try:
            name = input("Patient name: ").lower().strip()
            # this will allow user to enter name having about two whitspaces in it
                # ^
                # |----------v-----
                # ----v---------v
            if re.search(r"^([a-z]{3,8}) ?([a-z]+)* ?([a-z]+)*$", name):
                age = input("Patient Age: ").strip()
                # first ensure that input is between 0 to 9 with infinite number of repetitions
                if re.search(r"^[0-9]+$", age):
                    if (int(age) > 0) and (int(age) <= 100):
                        gender = input("Gender(male/female/neutral): ").lower().strip()
                        if gender in lst:
                            disease = input("Patient Disease: ").lower().strip()
                            if disease in diseases:
                                introLst.append(name)
                                introLst.append(age)
                                introLst.append(gender)
                                introLst.append(disease)
                                insertingData(introLst)
                                console.print("Data added successfully!", style="green")
                                break

        except:
            userinput = input("Press 3 for Exit: ").strip()
            if userinput == "3":
                break


def insertingData(introLst):
    count = 1
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(count + introLst)
        count += 1

def viewData():
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            console.print("\nPatient Records:", style="bold blue")
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        console.print("No data found. Add some patient records first.", style="red")

if __name__ == "__main__":
    main()
