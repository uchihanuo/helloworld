def l2s(a_list):
    for i in range(len(a_list) - 1):
        print(a_list[i] + ', ', end='')
    print('and ' + a_list[len(a_list) - 1])


spamlist = []
while True:
    print('Please enter the cell ' + str(len(spamlist) + 1) + ' of the list, or enter nothing to end.')
    spam = input()
    if spam == '':
        break
    spamlist += [spam]
# print(spamlist)
l2s(spamlist)
