student_one = {'name':'dyk', 'score':'100'}

school = "St. Law"

answer = input("Guess the school: ")

new_score = student_one['score']

if answer == school:
    print("you earned " + str(new_score) + " points!")
else:
    print("you lost " + str(new_score) + " points!")