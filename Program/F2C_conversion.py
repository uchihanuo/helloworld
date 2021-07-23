# coding = utf-8
temp_str = input('Please enter the temperature with the unit.')
if temp_str[-1] in ['F', 'f']:
    temp_con = (eval(temp_str[0:-1]) - 32) / 1.8
    print('The temperature is {:.2f} C.'.format(temp_con))
elif temp_str[-1] in ['C', 'c']:
    temp_con = eval(temp_str[0:-1]) * 1.8 + 32
    print('The temperature is {:.2f} F.'.format(temp_con))
else:
    print('Enter false')
