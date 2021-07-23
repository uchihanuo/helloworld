#! python3
# -*- coding: utf-8 -*-


def ASCIICoverse(words):
    new_words = ''
    for single in words:
        # if single.isalpha() or single.isdigit():
        words_asc = ord(single)
        if 126 >= words_asc >= 32:
            new_words += chr(158 - words_asc)
        elif single.isalpha():
            a_str = single.encode('unicode_escape').decode('ascii')
            a_str = '\\u' + hex(3634 - int(a_str[2:5], 16))[2:] + a_str[-1]
            new_words += a_str.encode('ascii').decode('unicode_escape')
        else:
            new_words += single
    return new_words


def main():
    print(ASCIICoverse(str(input('enter something\n'))), '\n')


if __name__ == '__main__':
    main()
