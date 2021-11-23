number_of_questions = int(input())
answers = []
for _ in range(number_of_questions):
	answers.append(input())
hanh = answers[1:]
score = 0
for i in range(len(hanh)):
	if hanh[i] == answers[i]:
		score += 1
print(score)