def print_max(a, b):
    '''Prints the maximum of two numbers

    The two values must be integers.'''
    if a > b:
        print(a, 'is maximum.')
    elif a < b:
        print(b, 'is maximum.')
    else:
        print(a, 'is equal to ', b, '.')


x = int(input('Please enter the first number:'))
y = int(input('Please enter the second number'))
print_max(x, y)
print(print_max.__doc__)
