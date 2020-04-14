x = eval(input("enter any number"))

if x % 3 == 0 and x % 5 == 0:
    print("Consultadd Python Training")
if x % 3 == 0:
    print("Consutadd")
if x % 5 == 0:
    print("c")
print("bye")

# taskTwo

x = eval(input("enter a number lessthan or eqaul to 5 "))

if x == 1:
    print("Addition")
    Addition = eval(input("enter 1st number")) + eval(input("enter 2nd number"))
    if x < 0:
        print("your answer is ", Addition)
    else:
        print("zsa")
if x == 2:
    print("Subtraction")
    Subtraction = eval(input("enter 1st number:")) - eval(input("enter 2nd number:"))
    if Subtraction > 0:
        print("your answer is ", Subtraction)
    else:
        print("zsa")
if x == 3:
    print("Division")
    Division = eval(input("enter 1st number")) / eval(input("enter 2nd number"))
    if Division > 0:
        print("your answer is ", Division)
    else:
        print("zsa")
if x == 4:
    print("Multiplication")
    Multiplication = eval(input("enter 1st number")) * eval(input("enter 2nd number"))
    if Multiplication > 0:
        print("your answer is ", Multiplication)
    else:
        print("zsa")
if x == 5:
    print("Average")
    Average = (eval(input("enter 1st number")) + eval(input("enter 2nd number"))) / 2
    if Average > 0:
        print("your answer is ", Average)
    else:
        print("zsa")


# taskThree

a, b, c = 10, 20, 30
avg = (a + b + c) / 3
print("avg = ", avg)
if avg > a and avg > b and avg > c:
    print("avg is higher than a,b,c ")
elif avg > a and avg > b:
    print("avg is higher than a,b ")
elif avg > a and avg > c:
    print("avg is higher than a,c ")
elif avg > b and avg > c:
    print("avg is higher than b,c ")
elif avg > a:
    print("avg is higher than a ")
elif avg > b:
    print("avg is higher than b ")
elif avg > c:
    print("avg is higher than c ")


# taskFour


while True:
    x = eval(input("please enter a number of your choice: "))
    if x < 0:
        print("it's Over")
        break
    if x >= 0:
        print("Good Going")
        continue


# taskFive

for x in range(2000,3200):
    if (x % 7 == 0) and (x % 5 != 0):
        print(x)


# taskSix

# range function is missing, if range is used answer would be 1 to 122
# 0 error 1 error 2
# Break is used instead of break, if break is used answer is 0 1 2 3 4 if not error is displayed


# taskSeven


for x in range(6):
    if x == 3 or x == 6:
        continue
    print(x)


# taskEight

x = input("enter combination letters and numbers: ")
Letters = Digits = 0

for i in range(len(x)):
    if x[i].isalpha():
        Letters = Letters + 1
    elif x[i].isdigit():
        Digits = Digits + 1
print("letters ", Letters)
print("Digits", Digits)


# TaskNine
while True:
    number = int(input("guess the lucky number: "))
    if number == 7777:
        print("winner")
        break
    if number != 7777:
        answer = input("want to guess again Y/N: ")
        if answer == "Y":
            number = int(input("guess the lucky number: "))
        else:
            print("bye")