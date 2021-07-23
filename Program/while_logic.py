num = 19
# running = True
while True:  # running:
    guess = int(input('Please input an integer which you guess '))
    if guess == num:
        print("YES, you get it!\nIt's easy right?")
        # running = False
        break
    elif guess > num:
        print("It's a little lower than that.")
    else:
        print("It's a little higher than that.")
else:
    print("The while loop is over.")

print('Done')
