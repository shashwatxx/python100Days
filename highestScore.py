

student_scores = list(
    map(int, input("Input list of Students Scores\n").split()))

# print(student_scores)
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score


print(f"The highest Score is {highest_score}")
