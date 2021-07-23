def say(message, times=1):
    print(message * times)
    return times


say('Hello')
say('Hello\t', 5)
say('Hello', times=3)
