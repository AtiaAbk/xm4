n = int(input("Enter number of students: "))

fail_count = 0

for i in range(1, n + 1):
    marks = float(input("Enter marks for student: "))
    
    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "fail"
        fail_count += 1
    
    print(grade)

print("total students failed:", fail_count)
