# Quiz Game
# Author: Theo
# Date: Dec. 4 / 2020

quiz_score = 0

# question 1

q1 = int(input("1 + 1"))

if q1 == 2:
    print("You're right.")
    quiz_score += 1

elif q1 != 2:
    print("You're wrong, answer is 2.")
    quiz_score -= 1

# question 2

q2 = int(input("2 + 2"))

if q2 == 4:
    print("You're right.")
    quiz_score += 1

elif q2 != 4:
    print("You're wrong, answer is 4.")
    quiz_score -= 1

# question 3

q3 = int(input("3 + 3"))

if q3 == 6:
    print("You're right.")
    quiz_score += 1

elif q3 != 6:
    print("You're wrong, answer is 6.")
    quiz_score -= 1

# question 4

q4 = int(input("4 + 4"))

if q4 == 8:
    print("You're right.")
    quiz_score += 1

elif q4 != 8:
    print("You're wrong, answer is 8.")
    quiz_score -= 1

# question 5

q5 = int(input("5 + 5"))

if q5 == 10:
    print("You're right.")
    quiz_score += 1

elif q5 != 10:
    print("You're wrong, answer is 10.")
    quiz_score -= 1

# print out the score
print(f"You got {quiz_score} out of 5.")