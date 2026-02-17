n = int(input("Enter number of students: "))

fail_count = 0

for i in range(1, n + 1):
    marks = float(input(f"Enter marks for student {i}: "))
    
    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"
        fail_count += 1
    
    print(f"Student {i} Grade:", grade)

print("Total students failed:", fail_count)
