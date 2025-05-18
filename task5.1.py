student_marks={"Alice":85,"Ben":92,"Micheal":81}
student=input("Enter the Student's name: ")
if student in student_marks:
    print("{}'s marks: {}".format(student,student_marks[student]))
else:
    print("student not found.")