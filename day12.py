def greet(name):
    print(f"Hello, {name} !")
greet("Asmaul "+ "Hoque")
greet("Jubair " + "Ahmed")
greet("Arnab " + "Pradhan")

def add(a, b):
    #result = a + b
    #return result

answer = add (25, 27)
print("The answer is: ", answer)

def greet(name , message = "How are you ?"):
    #print(f"Hello,{name} ! {message}")

greet("Asmaul")
greet("Jubair", "Welcome , Whats up ?")
greet("Jamil Aktar", "How are you doing ?")

def calculate_grade (marks, total = 80):

    percentage = (marks / total) * 100

    if percentage >=80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F"
    
    return grade, percentage

g , p = calculate_grade(75)
print(f"grade is : {g} and percentage is : {p} %")

g,p = calculate_grade(60)
print(f"grade is : {g} and percentage is : {p} %")

