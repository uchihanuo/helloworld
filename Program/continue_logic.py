while True:
    s = input('Enter something: ')
    if len(s) < 5:
        if s =='quit':
            break
        else:
            print('Too small.')
        continue
    else:
        print('Input is of sufficient length.')
print('Done')
