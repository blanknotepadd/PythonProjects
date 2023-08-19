import random

count = 1
for i in range(0, count):
    firstNumber = random.randrange(1, 67)
    secondNumber = random.randrange(firstNumber + 1, 68)
    thirdNumber = random.randrange(secondNumber + 1, 69)
    fourthNumber = random.randrange(thirdNumber + 1, 70)
    fifthNumber = random.randrange(fourthNumber + 1, 71)
    print("Lottery Numbers: ", firstNumber, secondNumber, thirdNumber, fourthNumber, fifthNumber)
    count = count + 1
    