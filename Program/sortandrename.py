#! python3
# -- coding: utf-8 --


import os, shutil, pprint, insertionSort, howmany


def sortandrename(folder):
    start_content = 'capitalsquiz'
    end_content = '.txt'
    num = 0
    # lost_num = []
    folder = os.path.abspath(folder)
    os.chdir(folder)
    for filename in os.listdir(folder):
        num += 1
        if filename == start_content + str('%02d' % num) + end_content:
            continue
        else:
            print('The file name should be {} not {}.'.format(start_content + str('%02d' % num) + end_content, filename))
            # lost_num += [('%02d' % num)]
            shutil.copy(filename, start_content + str('%02d' % num) + end_content)
            # num += 1
    pprint.pprint(os.listdir(folder))


def enterblank(folder):
    start_content = 'capitalsquiz'
    end_content = '.txt'
    # file_list = [os.listdir(folder)]
    num_list = []
    while True:
        num = input('Please enter the blank number.')
        if num is '':
            break
        num_list += ['%02d' % int(num)]
    num_list = insertionSort.insertionSort2High(num_list)
    for n in num_list:
        while int(n) - 1 < int(num_list[num_list.index(n) + 1]) or num_list.index(n) + 1 == len(num_list):
            m = int(n) + 1
            m = '%02d' % m
            shutil.copy(start_content + n + end_content,
                        start_content + m + end_content)
    pprint.pprint(os.listdir(folder))


while True:
    work_mode = input('Please choice the work mode " 1 " for SORT the file, " 2 " for INSERT the blank.')
    target_folder = str(input('Please enter the folder.'))
    if work_mode is '1' and os.path.exists(target_folder):
        sortandrename(target_folder)
        break
    elif work_mode is '2' and os.path.exists(target_folder):
        print('Function building.')
    #     enterblank(target_folder)
        break
    else:
        print('Please enter the right NUMBER or your folder may not exist.')
