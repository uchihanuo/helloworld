# coding:utf-8
def F2C_conversion(temp):
    temp_c = (float(temp[0: -1]) - 32) / 1.8
    return temp_c


def C2F_conversion(temp):
    temp_f = 1.8 * float(temp[0: -1]) + 32
    return temp_f


temperature = input('Please enter the temperature with unit.')
# type(temperature)
while temperature:
    if temperature[-1] in ['F', 'f']:
        temp_conversion = F2C_conversion(temperature)
        print('The temperature is {} C.'.format(temp_conversion))
        break
    elif temperature[-1] in ['C', 'c']:
        temp_conversion = C2F_conversion(temperature)
        # print(temp_conversion)
        print('The temperature is {:.2f} F.'.format(temp_conversion))
        break
    else:
        print('Enter false.')
        break
else:
    print('Do not enter nothing!!!')
