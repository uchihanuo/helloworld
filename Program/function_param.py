def print_max(a, b):
    if a > b:
        print(a, 'is maximum.')
    elif a < b:
        print(b, 'is maximum.')
    else:
        print(a, 'is equal to ', b, '.')


print_max(3, 4)

x = input('Please enter the first number: ')
y = input('Please enter the second number: ')
print_max(x, y)
