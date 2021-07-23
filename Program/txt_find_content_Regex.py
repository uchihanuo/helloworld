#! python3
# coding = utf-8

import re, pprint, os, traceback


# find all txt file in the path.
def find_txt_Regex(a_path):
    file_list = os.listdir(a_path)
    txt_list_Regex = []
    for f in file_list:
        if re.compile(r'.*(\.txt)$').search(str(f)):
            txt_list_Regex += [f]
    #    try:
    #        re.compile(r'.*(\.txt)$').search(str(f)).group()
    #        txt_list_Regex += [f]
    #    except AttributeError:
    #        errorflie = open(a_path + os.sep + 'errorInfo.txt', 'w')
    #        errorflie.write(f + '\n\n')
    #        errorflie.write(traceback.format_exc())
    #        errorflie.close()
    #        continue
    # pprint.pprint(txt_list_Regex)
    return txt_list_Regex


def find_txt(a_path):
    txt_list = []
    for f in os.listdir(a_path):
        if f.endswith('.txt'):
            txt_list += [f]
    return txt_list


# find txt files' content with c.
def find_content(a_list, target_path, c = ''):
    pprint.pprint(a_list)
    if c is not '':
        for f in a_list:
            a_file = open(target_path + '\\' + f)
            if re.compile(c).search(a_file.readline()):
                file_content = re.compile(c).search(a_file.readline()).group()
                pprint.pprint(file_content)
        #    try:
        #        file_content = re.compile(c).search(a_file.readline()).group()
        #        pprint.pprint(file_content)
        #    except AttributeError:
        #        continue


Your_path = str(input('Please enter your path:'))
Your_case = str(input('Please enter your case:'))
find_content(find_txt(Your_path), Your_path, Your_case)
find_content(find_txt_Regex(Your_path), Your_path, Your_case)
