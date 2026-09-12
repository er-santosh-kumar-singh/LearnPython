from BasicPython.calculator import add,sub,mul,div
from BasicPython.loop import printUsingFor, printUsingForSum, printNumberUsingWhileLoop, printNumberUsingBreak_Continue
from BasicPython.ifelseprogram import printGrade

'''def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.'''


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Welcome to python program..')


# Calculator program calling
'''
add = add(10, 20)
print(add)
sub = sub(10,20)
print(sub)
mul = mul(10,20)
print(mul)
div = div(10,20)
print(div)
'''
#===============================
print('Loop program....')

'''printUsingFor(10)
printUsingForSum(10)

printNumberUsingWhileLoop(10)
printNumberUsingBreak_Continue(10)'''

# if else program...
print('If else program....')
score = int(input('Enter your score:'))
if score > 100 or score < 0:
    print('Please enter valid score')
else:
    printGrade(score)