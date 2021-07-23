def strings_test(name):
    x = name.find('er')
    if name.startswith('R'):
        print('Yes, the name starts with "R".')
        return name.startswith('R')
    if 'o' in name:
        print('Yse, "o" contained in the name.')
    if name.find('er') != -1:
        print('Yse, "er" contained in the name.')
        return x


Name = input(str('Please enter your name.\n'))
strings_test(Name)

shoplist = ['apple', 'mango', 'carrot', 'banana', 'xbox']
delinimiter = '__*__'
print(delinimiter.join(shoplist))

