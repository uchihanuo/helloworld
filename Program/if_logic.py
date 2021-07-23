num = 19
guess = int(input('Please input an integer which you guess '))
if guess == num:
    print("YES, you get it!\nIt's easy right?")
elif guess > num:
    print("It's a little lower than that.")
else:
    print("It's a little higher than that.")

print('Done')
