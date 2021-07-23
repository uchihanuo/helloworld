#! python3
# coding = utf-8

import re


def fill_blanks(txtfile_name):
    txtfile = open(txtfile_name)
    txtfile_content = str(txtfile.readline())
    txtfile.close()
    if re.compile(r'ADJECTIVE').search(txtfile_content).group():
        txtfile_content = re.compile(r'ADJECTIVE').sub(input('Please enter the ADJECTIVE.'), txtfile_content)
        print(txtfile_content)
    else:
        return True
    if re.compile(r'NOUN').search(txtfile_content).group():
        txtfile_content = re.compile(r'NOUN').sub(input('Please enter the NOUN.'), txtfile_content)
        print(txtfile_content)
    else:
        return True
    if re.compile(r'(ADVERB|VERB)').search(txtfile_content).group():
        txtfile_content = re.compile(r'(ADVERB|VERB)').sub(input('Please enter the ADVERB or VERB.'), txtfile_content)
        print(txtfile_content)
    else:
        return True

    print(txtfile_content)
    txtfile = open(txtfile_name, 'w')
    txtfile.write(txtfile_content)


which_txt = str(input('Please enter the txt file\'s name.'))
if fill_blanks(which_txt):
    print('No such ADJECTIVE, NOUN, ADVERB or VERB.')
print('-----   end   -----')
