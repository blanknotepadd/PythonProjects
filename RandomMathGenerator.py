import random

#generates 2 numbers from 0 to 100 and randomly generates an operator. the result is stored in a "result" variable
count = 5
for i in range(0, count):

    firstNumber = random.randrange(0, 101)
    secondNumber = random.randrange(0, 101)
    operatorArray = ["+", "=", "*", "/", "^"]
    operatorArrayIndex = random.randrange(0, len(operatorArray))

    print("1st number", firstNumber)
    print("2nd number", secondNumber)

    if (operatorArrayIndex == 0):
        result = firstNumber + secondNumber

    elif (operatorArrayIndex == 1):
        result = firstNumber - secondNumber

    elif (operatorArrayIndex == 2):
        result = firstNumber * secondNumber

    elif (operatorArrayIndex == 3):
        result = firstNumber / secondNumber

    elif(operatorArrayIndex == 4):
        result = firstNumber ** secondNumber

    print("Result:", result)
    print()

#generates a random number of randomly generated numbers from 1 to 8 then calculates the sum, length and average of that set of numbers
numberArray = []
randomArrayLength = random.randrange(1, 9)

for i in range(0, randomArrayLength):
    randomNumber = random.randrange(1, 11)
    numberArray.append(randomNumber)
    print(numberArray[i])

numberArrayAverage = sum(numberArray) / len(numberArray)
print("Sum:", sum(numberArray))
print("Length:", len(numberArray))
print("Average:", numberArrayAverage)





