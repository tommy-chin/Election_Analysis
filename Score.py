#What is the score?
score = int(input("What is your test score?"))


#Determine the test score
if score >= 90:
    print("You grade is an A.")
elif score >= 80:
    print("Your grade is a B.")
elif score >= 70:
    print("Your grade is a C")
elif score >= 60:
    print("Your grade is a D")
else:
    print("Your grade is an F")
