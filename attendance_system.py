import csv
from datetime import datetime

students = {}

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students[row["RFID_ID"]] = {
            "name": row["Name"],
            "roll": row["Roll_No"]
        }

card_id = input("Scan RFID Card: ")

if card_id in students:

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            students[card_id]["roll"],
            students[card_id]["name"],
            current_time
        ])

    print("\nAttendance Marked Successfully")
    print("Name :", students[card_id]["name"])
    print("Roll :", students[card_id]["roll"])
    print("Time :", current_time)

else:
    print("Invalid RFID Card")
