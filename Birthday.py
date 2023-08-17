from datetime import date
birthdayStringArray = ["H", "A", "P", "P", "Y", "", "B", "I", "R", "T", "H", "D", "A", "Y"]

today = date.today()
for i in range(0, len(birthdayStringArray)):
    print(birthdayStringArray[i])

print("")
inputName = input("What is your name? ")
inputMonth = input("What is %s's birth month? " % inputName.capitalize())
inputDay = input("What is %s's birth day? " % inputName.capitalize())
inputAge = input("How old are you? ")

birthYear = today.year - int(inputAge)


if (int(inputMonth) == today.month and int(inputDay) == today.day):
    print("")
    print("Happy birthday %s! You are %s years old." % (inputName.capitalize(), inputAge))

else:
    print("")
    print("Today is not your birthday :(")

if(int(inputMonth) == 3 and int(inputDay) >= 21 and int(inputDay) <= 31 or int(inputMonth) == 4 and int(inputDay) >= 1 and int(inputDay) <= 19):
    print("%s is an Aries." % inputName.capitalize())

elif((int(inputMonth) == 4 and int(inputDay) >= 20 and int(inputDay) <= 30) or (int(inputMonth) == 5 and int(inputDay) >= 1 and int(inputDay) <= 20)):
    print("%s is a Taurus." % inputName.capitalize())

elif((int(inputMonth) == 5 and int(inputDay) >= 21 and int(inputDay) <= 31) or (int(inputMonth) == 6 and int(inputDay) >= 1 and int(inputDay) <= 20)):
    print("%s is a Gemini." % inputName.capitalize())

elif((int(inputMonth) == 6 and int(inputDay) >= 21 and int(inputDay) <= 30) or (int(inputMonth) == 7 and int(inputDay) >= 1 and int(inputDay) <= 22)):
    print("%s is a Cancer." % inputName.capitalize())

elif((int(inputMonth) == 7 and int(inputDay) >= 23 and int(inputDay) <= 31) or (int(inputMonth) == 8 and int(inputDay) >= 1 and int(inputDay) <= 22)):
    print("%s is a Leo." % inputName.capitalize())

elif((int(inputMonth) == 8 and int(inputDay) >= 23 and int(inputDay) <= 31) or (int(inputMonth) == 9 and int(inputDay) >= 1 and int(inputDay) <= 20)):
    print("%s is a Virgo." % inputName.capitalize())

elif((int(inputMonth) == 9 and int(inputDay) >= 23 and int(inputDay) <= 30) or (int(inputMonth) == 10 and int(inputDay) >= 1 and int(inputDay) <= 20)):
    print("%s is a Libra." % inputName.capitalize())

elif((int(inputMonth) == 10 and int(inputDay) >= 23 and int(inputDay) <= 31) or (int(inputMonth) == 11 and int(inputDay) >= 1 and int(inputDay) <= 22)):
    print("%s is a Scorpio." % inputName.capitalize())

elif((int(inputMonth) == 11 and int(inputDay) >= 22 and int(inputDay) <= 30) or (int(inputMonth) == 12 and int(inputDay) >= 1 and int(inputDay) <= 22)):
    print("%s is a Sagittarius." % inputName.capitalize())

elif((int(inputMonth) == 12 and int(inputDay) >= 22 and int(inputDay) <= 31 or (int(inputMonth)) == 1 and int(inputDay) >= 1 and int(inputDay) <= 19)):
    print("%s is a Capricorn." % inputName.capitalize())

elif((int(inputMonth) == 1 and int(inputDay) >= 20 and int(inputDay) <= 31) or (int(inputMonth) == 2 and int(inputDay) >= 1 and int(inputDay) <= 18)):
    print("%s is an Aquarius." % inputName.capitalize())

elif((int(inputMonth) == 2 and int(inputDay) >= 19 and int(inputDay) <= 31) or (int(inputMonth) == 3 and int(inputDay) >= 1 and int(inputDay) <= 20)):
    print("%s is a Pisces." % inputName.capitalize())

else:
    print("ERROR")

print("Today's date: ", today.strftime("%m/%d/%y"))
print("%s's birthdate: %s/%s/%s " % (inputName.capitalize(), inputMonth, inputDay, birthYear))

