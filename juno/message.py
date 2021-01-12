names = input("Enter names: ").title().split(",")
assignments = input("Enter assignments: ").split(",")
grades = input("Enter grades: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades): 
    message.format(name, assignment, grade, int(grade) + int(assignment)*2)
    print(message)