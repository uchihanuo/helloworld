#! python3
# -*- coding: utf-8 -*-


# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")
def binarysearch(arr, key):
    min = 0
    max = len(arr) - 1
    if key in arr:
        while True:
            center = int((min + max) / 2)
            if key > arr[center]:
                min = center + 1
            elif key < arr[center]:
                max = center - 1
            elif key == arr[center]:
                print(str(key) + ' is in the array of ' + str(center))
                return arr[center]
    else:
        print('There is NO this ' + str(key))


if __name__ == '__main__':
    array = [3, 4, 7, 9, 13, 17, 19, 24, 29, 37, 42, 49, 51]
    while True:
        num = input('Please enter a number, or press ENTER to EXIT.')
        if num == '':
            break
        else:
            binarysearch(array, int(num))
    print('END.')
