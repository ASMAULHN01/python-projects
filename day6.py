#students = []
#marks = []

#name = input( "Name of the Student : ")
#mark = int(input("Koto Number Peyeche (Out of 100): "))

#students.append(name)
#marks.append(mark)

#print(students)
#print(marks)

students = []
marks = []

for i in range (5):
    name = input("Name of the Student : ")
    mark = int(input("Mark (out of 100) :"))

    students.append(name)
    marks.append (mark)

print("\n --- RESULT ---")
for i in range(len(students)):
    m = marks [i]
    if m >= 80 :
        grade = "A"
    elif m >= 60 :
        grade = "B"
    elif m >= 40 :
        grade = "C"
    else:
        grade = "F"

    print(f"{students[i]} : {m} marks : Grade {grade} " )

