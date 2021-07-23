def revers(text):
    return text[::-1]


def is_palindrome(text):
    return text == revers(text)


something = input('Enter something')
if is_palindrome(something):
    print("Yes, it's palindrome.")
else:
    print("No,it isn't.")
