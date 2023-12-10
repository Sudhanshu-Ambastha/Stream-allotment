marks = []
subjects = ['English', 's.st', 'maths', 'science']
for i in range(4):
    m = int(input("Enter marks for " + subjects[i] + ": "))
    marks.append(m)

if all(m >= 80 for m in marks):
    print("All subjects have more than 80 marks = Science stream")
elif marks[0] > 80 and marks[2] >= 50 and marks[3] >= 50:
    print("English > 80 and math & science above 50 - Commerce stream")
elif marks[0] > 80 and marks[1] > 80:
    print("English > 80 and s.st > 80 - Humanities stream")
else:
    print("Sorry, you don't qualify for any stream")
