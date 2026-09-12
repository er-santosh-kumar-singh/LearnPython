#Type of loops in python:
#for, while, break and continue

# For loop example
def printUsingFor(inputNumber: int):
    for i in range(inputNumber):
        print(i)

def printUsingForSum(inputNumber: int):
    sum = 0
    for i in range(inputNumber):
        sum += i
    print('The sum of numbers is ', sum)

# while loop example
# Prints out 0,1,2,3,4,5,6,7,8,9,10
def printNumberUsingWhileLoop(inputNumber: int):
    print('Program using while loop')
    inputNumber=0
    while inputNumber<10:
        print(inputNumber)
        inputNumber+=1

# Prints out 0,1,2,3,4
def printNumberUsingBreak_Continue(inputNumber: int):
    print('\nProgram using break and continue program..')
    print('\nProgram using break program..\n')
    inputNumber = 0
    while True:
        print(inputNumber)
        inputNumber += 1
        if inputNumber >= 5:
            break
    print('\nProgram using continue program..\n')
    # Prints out only odd numbers - 1,3,5,7,9
    for x in range(10):
        # Check if x is even
        if x % 2 == 0:
            continue
        print(x)