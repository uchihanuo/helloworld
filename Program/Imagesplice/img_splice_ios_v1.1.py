#! python3
# -*- coding: utf-8 -*-

import time
import appex
import PIL.Image as Image
import numpy as np


def matching(img_data):
    # to get selected images from iPhone
    print('Images Loading...')
    img_list = [np.array(img_file.convert('L')) for img_file in img_data]
    height = img_list[0].shape[0]
    print('Total %d images.' % len(img_list))

    # matching each images' size which for splicing
    # 1st image's start line
    splice_list = [0]
    for n in range(len(img_list) - 1):
        img_a = img_list[n]
        img_b = img_list[n + 1]
        m = 0
        # a_array = np.array([])
        print('Compare image %d and %d...' % ((n + 1), (n + 2)))
        # from 2st image's start line to half height
        for line in img_b[: int(height / 2)]:
            # to save result of img_b's row compare between img_a
            a_array = np.logical_and.reduce(line == img_a[int(height / 2):], axis=1)
            # to find the unique row
            if len(np.where(a_array)[0]) == 1:
                # np.where() could find index
                splice_list.append(np.where(a_array)[0][0] + int(height / 2))
                splice_list.append(m)
                break
            m += 1
    # last image's end line
    splice_list.append(img_list[0].shape[-1])
    # [0, 1714, 132, 2191, 159, 2220, 159, 2435, 132, 2260, 160, 2190, 151, 2436]
    # for example, 1st: 0*1717, 2st: 132*2191
    return splice_list


def stitching(img_data, splice_list):
    # stitching images
    # to get unchanged images
    img_list = [np.array(img_file) for img_file in img_data]
    # to save the img_list's data
    img_size = []
    for n in range(0, len(splice_list), 2):
        img_size.append(img_list[int(n / 2)][splice_list[n]: splice_list[n + 1]])
    del img_list
    print('Stitching images...')
    # to concatenate the arrays
    img = np.concatenate([img_n for img_n in img_size])
    img_result = Image.fromarray(img)
    img_result.save('IMG_' + time.strftime('%Y%m%d%H%M') + '.PNG')
    img_result.show()
    print('Mission Complete.')


def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    else:
        img_pil = appex.get_images(image_type='pil')
        splice_size = matching(img_pil)
        if len(splice_size) == 1:
            print('The images don\'t match.')
        else:
            print('Matching Complete.')
            stitching(img_pil, splice_size)


if __name__ == '__main__':
    main()
