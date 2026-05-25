students = []

def add_student(name, roll_no, department, city):
    student = {
        "name": name,
        "roll_no": roll_no,
        "department": department,
        "city": city
    }
    students.append(student)
    print(f"{name} added successfully !")

def show_students():
    print("\n---- All Students----")
    for s in students:
        print(f"Name: {s['name']}, roll_no: {s['roll_no']}, department: {s['department']}, city: {s['city']}")

add_student("Asmaul Hoque", "11200124057", "CSE", "Murshidabad")
add_student("Jubair Ahmed", "11200124058", "CSE", "Kolkata")
add_student("Arnab Pradhan", "11200124056", "CSE", "Medinipur")
add_student("Rakibul Islam Mollah", "11200124060", "LT", "Birbhum")
add_student("Jamil Aktar", "11200124065", "CSE", "Murshidabad")

show_students()
def save_to_file():
    file = open("students.txt", "w")
    for s in students:
        file.write(f"Name: {s['name']} , roll_no: {s['roll_no']} , department: {s['department']} , city: {s['city']} \n")
    file.close()
    print("Students saved to file successfully !")
save_to_file()
