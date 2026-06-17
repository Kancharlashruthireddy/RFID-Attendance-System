from datetime import datetime

students = {
    "101": "Ravi",
    "102": "Priya",
    "103": "Kiran",
    "104": "Anjali"
}

marked_today = set()

while True:
    card_id = input("Scan RFID Card (q to quit): ")

    if card_id.lower() == "q":
        break

    if card_id in students:
        if card_id in marked_today:
            print("Attendance already marked")
        else:
            marked_today.add(card_id)

            now = datetime.now()

            with open("attendance.txt", "a") as file:
                file.write(
                    f"{students[card_id]}, "
                    f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n"
                )

            print("Attendance Saved")
    else:
        print("Invalid Card")
