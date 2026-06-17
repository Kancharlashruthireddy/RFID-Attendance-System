from datetime import datetime

students = {
    "101": "Ravi",
    "102": "Priya",
    "103": "Kiran",
    "104": "Anjali"
}

card_id = input("Scan RFID Card: ")

if card_id in students:
    now = datetime.now()
    print("Attendance Marked")
    print("Student:", students[card_id])
    print("Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
else:
    print("Invalid Card")
