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

    with open("attendance.txt", "a") as file:
        file.write(
            f"{students[card_id]}, "
            f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

    print("Attendance Saved")
else:
    print("Invalid Card")
