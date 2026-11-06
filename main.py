import json

print("University Information System")

while True:
    try:
        with open("database/database.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("ERROR, can't load json file. File was renamed or removed, please resolve and try again!")
        break
    option = input("1) Display Subjects information\n2) Display all students:\n3) Add new student:\n4) Display which students pass specific subject:\nEnter: ")
    if option == "1":
        print("Subjects:")
        count = 1
        for subject in data["subjects"]:
            subject_id = subject["id"]
            subject_name = subject["subject_name"]
            credits = subject["credits"]
            required_attendance = subject["min_attendance"]
            required_exam_score = subject["min_final_exam_score"]
            prof_name = subject["professor"]["name"]
            prof_surname = subject["professor"]["surname"]
            print(f"{count}. {subject_name} - Credits: {credits}, Professor: {prof_name} {prof_surname}, Required exam points: {required_exam_score}, Required attendance:{required_attendance}")
            count+=1

    elif option == "2":
        print("Displaying Students: ")
        count = 1
        for student in data["students"]:
            student_id = student["id"]
            name = student["name"]
            surname = student["surname"]
            total_subjects = len(student["subjects"])
            print(f"{count}. {name} {surname} - registered on {total_subjects} subjects")
            count+=1

    elif option == "3":
        print("Adding new student:")
        while True:
            id = input("Enter ID number of a student: ")
            if id.isnumeric():
                break
            else:
                print("ID must be numeric!")
        name = input("Enter Name: ")
        surname = input("Surname: ")
        subjects = []
        while True:
            subject_id = input("Enter subject id, type stop when you are finished: ")
            if subject_id.lower() == "stop":
                break
            attendance = input("Enter how many times student attended the subject: ")
            exam_score = input("Enter how many points did student get on the exam: ")
            if subject_id.isnumeric() and attendance.isnumeric() and exam_score.isnumeric():
                subjects.append({"id": int(subject_id), "attendance": int(attendance), "score": int(exam_score)})
            else:
                print("Wrong data-type entered, must be numeric!")
        data["students"].append({"id": id, "name": name, "surname": surname, "subjects": subjects})
        with open("database/database.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Student was successfully added!")
    elif option == "4":
        passing_students = []
        while True:
            wanted_subject = input("Enter Subject ID: ")
            if wanted_subject.isnumeric():
                wanted_subject = int(wanted_subject)
                break
            else:
                print("Invalid value, must be numerical.")
        for subject in data["subjects"]:
            if subject["id"] == wanted_subject:
                min_attendance = subject["min_attendance"]
                min_score = subject["min_final_exam_score"]
                for student in data['students']:
                    for sub in student['subjects']:
                        if sub['id'] == subject['id'] and sub['attendance'] >= min_attendance and sub['score'] >= min_score:
                            passing_students.append(student)
                break
        if passing_students != []:
            count = 0
            for i in passing_students:
                count+=1
                print(f"{count}) {i['name']} {i['surname']} - Passed this subject")
        else:
            print("Everyone failed this subject!")
    else:
        print("Wrong entry, type 1 or 2 or 3 or 4")
    break_loop = input("Run again? y/n: ")
    if break_loop.upper() != "Y":
        break