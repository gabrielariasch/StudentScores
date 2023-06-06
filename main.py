student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if score > 90:
        student_grades[key] = "Outstanding"
    elif score in range(81,90):
        student_grades[key] = "Exceeding Expectations"
    elif score in range(71,80):
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"


print(student_grades)