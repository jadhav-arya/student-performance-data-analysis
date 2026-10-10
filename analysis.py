
import csv

students = []

with open("student_performance.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)

subjects = ["Math", "Science", "English", "Computer"]

print("STUDENT PERFORMANCE ANALYSIS")
print("-" * 35)

for student in students:
    marks = [int(student[subject]) for subject in subjects]
    average = sum(marks) / len(marks)

    print(
        student["Name"],
        "- Average Marks:",
        round(average, 2)
    )

print("\nSUBJECT-WISE ANALYSIS")
print("-" * 35)

for subject in subjects:
    marks = [int(student[subject]) for student in students]

    print(subject)
    print("Average:", round(sum(marks) / len(marks), 2))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))
    print()

print("Total Students:", len(students))
