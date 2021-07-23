if __name__ == '__main__':
    print('This program is being run by itself.')
    print(__name__)
else:
    print('I am being imported from another module.')
    print(__name__)
