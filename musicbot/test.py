import math

userNumber = int(input("Введите первое число: "))

summary = 0

while userNumber != 0:
    if userNumber % 7 == 0 and userNumber % 10 == 3:
        summary += userNumber
    userNumber = int(input("Введите новое число: "))

print(summary)