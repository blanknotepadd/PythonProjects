import random

listOfCapitalLets = ["A", "B", "C", "D", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S","T", "U", "V", "W", "X", "Y", "Z"]
listOfLowerLets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
listofSpecialChars = ["!", "@", "$", "%", "^", "&", "*", "+", "#"]
Password = []
listOfPasswords = [Password]
PasswordLength = random.randrange(4, 17)


listOfChars = listOfCapitalLets + listOfLowerLets + listofSpecialChars

for i in range(0, PasswordLength):
    randomCharIndex = random.randrange(0, len(listOfChars))
    Password.append(listOfChars[randomCharIndex])




print(*Password, sep = "")

