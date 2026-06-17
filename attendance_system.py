students = {
    "101": "Ravi",
    "102": "Priya",
    "103": "Kiran",
    "104": "Anjali"
}

card_id = input("Scan RFID Card: ")

if card_id in students:
    print("Attendance Marked")
    print("Student:", students[card_id])
else:
    print("Invalid Card")
