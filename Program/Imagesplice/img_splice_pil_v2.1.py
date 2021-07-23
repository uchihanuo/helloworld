#! python3
# -*- coding: utf-8 -*-
# Version 2.1

import os
import time
import PIL.Image as Image
import numpy as np
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")


def matching(folder_path):
    # to get selected images from iPhone
    print('Images Loading...')
    img_list = [np.array(Image.open(os.path.join(os.path.abspath(folder_path), img_file)).convert(
        'L')) for img_file in os.listdir(folder_path) if img_file.endswith('.PNG')]
    height = img_list[0].shape[0]
    print('Total %d images.' % len(img_list))

    # matching each images' size which for splicing
    splice_list = [0]  # 1st image's start line
    for n in range(len(img_list) - 1):
        img_a, img_b = img_list[n: n + 2]
        m = 0
        # a_array = np.array([])
        print('Compare image %d and %d...' % ((n + 1), (n + 2)))
        for line in img_b[: int(
                height / 2)]:  # from 2st image's start line to half height
            # to save result of img_b's row compare between img_a
            a_array = np.logical_and.reduce(
                line == img_a[int(height / 2):], axis=1)
            if len(np.where(a_array)[0]) == 1:  # to find the unique row
                # np.where() could find index
                splice_list.append(np.where(a_array)[0][0] + int(height / 2))
                splice_list.append(m)
                break
            m += 1
    splice_list.append(img_list[-1].shape[0])  # last image's end line
    # [0, 1714, 132, 2191, 159, 2220, 159, 2435, 132, 2260, 160, 2190, 151, 2436]
    # for example, 1st: 0*1717, 2st: 132*2191
    return splice_list


def stitching(folder_path, splice_list):
    # stitching images
    # to get unchanged images
    img_list = [np.array(Image.open(os.path.join(os.path.abspath(folder_path), img_file)))
                for img_file in os.listdir(folder_path) if img_file.endswith('.PNG')]
    # to save the img_list's data
    img_spliced = []
    for n in range(0, len(splice_list), 2):
        img_spliced.append(img_list[int(n / 2)]
                           [splice_list[n]: splice_list[n + 1]])
    del img_list
    print('Stitching images...')
    # to concatenate the arrays
    img_array = np.concatenate([img_n for img_n in img_spliced])
    Image.fromarray(img_array).save(
        os.path.join(
            os.path.abspath(folder_path),
            'IMG_' +
            time.strftime('%Y%m%d%H%M') +
            '.PNG'))
    print('Mission Complete.')


def main():
    while True:
        folder = str(input('Please enter the folder for zip.'))
        if os.path.exists(folder):
            splice_size = matching(folder)
            if len(splice_size) == 1:
                print('The images don\'t match.')
            else:
                print('Matching Complete.')
                stitching(folder, splice_size)
            break
        else:
            print('The folder does not exist, please check.')


if __name__ == '__main__':
    main()
