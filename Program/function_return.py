def maximum(x, y):
    '''Heheda~~~.'''
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal.'
    else:
        return y


a = int(input('Please enter the first number:'))
b = int(input('Please enter the second number'))
print(maximum(a, b))
print(maximum.__doc__)

