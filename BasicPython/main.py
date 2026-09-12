from BasicPython.calculator import add,sub,mul,div
from BasicPython.loop import printUsingFor, printUsingForSum, printNumberUsingWhileLoop, printNumberUsingBreak_Continue
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Welcome to calculator program..')


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

printUsingFor(10)
printUsingForSum(10)

printNumberUsingWhileLoop(10)
printNumberUsingBreak_Continue(10)

