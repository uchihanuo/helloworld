#! python3
# -*- coding: utf-8 -*-


import os, csv, argparse, shelve
import matplotlib.pyplot as plt
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")


# CAN_MATRIX_DICT = {0: 56, 1: 57, 2: 58, 3: 59, 4: 60, 5: 61, 6: 62, 7: 63,
#                    8: 48, 9: 49, 10: 50, 11: 51, 12: 52, 13: 53, 14: 54, 15: 55,
#                    16: 40, 17: 41, 18: 42, 19: 43, 20: 44, 21: 45, 22: 46, 23: 47,
#                    24: 32, 25: 33, 26: 34, 27: 35, 28: 36, 29: 37, 30: 38, 31: 39,
#                    32: 24, 33: 25, 34: 26, 35: 27, 36: 28, 37: 29, 38: 30, 39: 31,
#                    40: 16, 41: 17, 42: 18, 43: 19, 44: 20, 45: 21, 46: 22, 47: 23,
#                    48: 8, 49: 9, 50: 10, 51: 11, 52: 12, 53: 13, 54: 14, 55: 15,
#                    56: 0, 57: 1, 58: 2, 59: 3, 60: 4, 61: 5, 62: 6, 63: 7}

CAN_MATRIX_DICT = {0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, 7: 0,
                   8: 15, 9: 14, 10: 13, 11: 12, 12: 11, 13: 10, 14: 9, 15: 8,
                   16: 23, 17: 22, 18: 21, 19: 20, 20: 19, 21: 18, 22: 17, 23: 16,
                   24: 31, 25: 30, 26: 29, 27: 28, 28: 27, 29: 26, 30: 25, 31: 24,
                   32: 39, 33: 38, 34: 37, 35: 36, 36: 35, 37: 34, 38: 33, 39: 32,
                   40: 47, 41: 46, 42: 45, 43: 44, 44: 43, 45: 42, 46: 41, 47: 40,
                   48: 55, 49: 54, 50: 53, 51: 52, 52: 51, 53: 50, 54: 49, 55: 48,
                   56: 63, 57: 62, 58: 61, 59: 60, 60: 59, 61: 58, 62: 57, 63: 56}


# splitting data to each csv file by ID
def splitdata(filename):
    os.makedirs('CAN_Message', exist_ok=True)
    with open(filename) as CSV_file:
        csv_list = list(csv.reader(CSV_file))
        message = []
        all_id = []
        for row in csv_list:
            # [[row], [...], [...]]
            a_list = row[0].split()
            # [2] is ID, [5] is length, [6: x] is data low to high
            message.append([a_list[2], a_list[5]])
            message[-1] += a_list[6: int(a_list[5]) + 6]
            # to find all id
            if a_list[2] not in all_id:
                all_id.append(a_list[2])
        # to create a can id file
        with open(os.path.join('.', 'CAN_Message', 'Message_id.csv'), 'w', newline='') as id_csv:
            id_writer = csv.writer(id_csv)
            for can_id in all_id:
                id_writer.writerow([can_id])
    # to create csv file for every each id
    for can_id in all_id:
        os.makedirs('CAN_Message' + os.path.sep + 'CAN_' + can_id, exist_ok=True)
        id_list = []
        for i in message:
            # [0] is id, [1] is length, [2: x] is data
            if can_id == i[0]:
                id_list.append(i[2: int(i[1]) + 2])
        # with open('.' + os.path.sep + 'CAN_Message' + os.path.sep + 'CAN_' + can_id + os.path.sep + 'CAN_' + can_id + '.csv', 'w', newline='') as message_csv:
        with open(os.path.join('.', 'CAN_Message', ('CAN_' + can_id), ('CAN_' + can_id + '.csv')), 'w', newline='') as message_csv:
            csv_writer = csv.writer(message_csv)
            for row in id_list:
                csv_writer.writerow(row)
        print('CAN_' + can_id + '.csv converted done.')


# to graph image for each id by bits
def graphdata(message_id):
    with open(os.path.join('.', 'CAN_Message', 'Message_id.csv')) as CSV_file:
        id_file = list(csv.reader(CSV_file))
        id_list = []
        for i in id_file:
            id_list.append(i[0])
        target_list = []
        # to chose the target id or convert all id
        if message_id in id_list:
            target_list.append(message_id)
        elif message_id.lower() == 'all':
            target_list = id_list.copy()
        else:
            print('The enter command or ID NOT in the list.')
        for target_id in target_list:
            print(target_id)
            # to load the id message
            # with open('.' + os.path.sep + 'CAN_Message' + os.path.sep + 'CAN_' + str(target_id) + os.path.sep + 'CAN_' + str(target_id) + '.csv') as message_can:
            with open(os.path.join('.', 'CAN_Message', ('CAN_' + str(target_id)), ('CAN_' + str(target_id) + '.csv'))) as message_can:
                message_list = list(csv.reader(message_can))
                bin_list = []
                for rows in message_list:
                    a_str = ''
                    for data16 in rows:
                        # hex convert to bin
                        bin_str = '%08d' % int(bin(int(data16, 16))[2:])
                        # to reverse the bin str like the can matrix low bit on left
                        # a_str += ''.join((lambda x: list(x)[::-1])(bin_str))
                        a_str += bin_str
                    # to reverse the bin str high bit on left
                    # a_str = ''.join((lambda x: list(x)[::-1])(a_str))
                    bin_list.append(a_str)
                message_len = len(bin_list[0])
                for i in range(message_len):
                    j = i + 1
                    # to control the bits length, max is 16 bits
                    while j - i <= 15 and j <= message_len:
                        a_list = []
                        bits_name = 'ID_' + str(target_id) + '_bits_' + str(CAN_MATRIX_DICT[j - 1]) + '_' + str(CAN_MATRIX_DICT[i])
                        for bits in bin_list:
                            a_list.append(int(bits[i: j], 2))
                        # plt.figure(figsize=(10.5, 4.5), dpi=100)
                        plt.plot(a_list)
                        plt.grid()
                        plt.title(bits_name)
                        plt.savefig(os.path.join('.', 'CAN_Message', ('CAN_' + str(target_id)), (bits_name + '.png')))
                        plt.close()
                        print(bits_name + '.png saved.')
                        j += 1


# to graph image for each id by bits
def graphdata_speed(message_id):
    with open(os.path.join('.', 'CAN_Message', 'Message_id.csv')) as CSV_file:
        id_file = list(csv.reader(CSV_file))
        id_list = []
        for i in id_file:
            id_list.append(i[0])
        target_list = []
        # to chose the target id or convert all id
        if message_id in id_list:
            target_list.append(message_id)
        elif message_id.lower() == 'all':
            target_list = id_list.copy()
        else:
            print('The enter command or ID NOT in the list.')
        for target_id in target_list:
            # to load the id message
            # with open('.' + os.path.sep + 'CAN_Message' + os.path.sep + 'CAN_' + str(target_id) + os.path.sep + 'CAN_' + str(target_id) + '.csv') as message_can:
            with open(os.path.join('.', 'CAN_Message', ('CAN_' + str(target_id)), ('CAN_' + str(target_id) + '.csv'))) as message_can:
                message_list = list(csv.reader(message_can))
                bin_list = []
                for rows in message_list:
                    a_str = ''
                    for data16 in rows:
                        # hex convert to bin
                        bin_str = '%08d' % int(bin(int(data16, 16))[2:])
                        # to reverse the bin str like the can matrix low bit on left
                        # a_str += ''.join((lambda x: list(x)[::-1])(bin_str))
                        a_str += bin_str
                    # to reverse the bin str high bit on left
                    # a_str = ''.join((lambda x: list(x)[::-1])(a_str))
                    bin_list.append(a_str)
                message_len = len(bin_list[0])
                # to save can data in shelve file
                with shelve.open(os.path.join('.', 'CAN_Message', 'message_info'), writeback=True) as can_data:
                    for bits in bin_list:
                        for i in range(message_len):
                            j = i + 1
                            # to control the bits length, max is 16 bits
                            while j - i <= 15 and j <= message_len:
                                bits_name = 'ID_' + str(target_id) + '_bits_' + str(CAN_MATRIX_DICT[j - 1]) + '_' + str(CAN_MATRIX_DICT[i])
                                print(bits_name + ' data has saved.')
                                if bits_name not in list(can_data.keys()):
                                    can_data[bits_name] = []
                                    can_data[bits_name].append(int(bits[i: j], 2))
                                else:
                                    can_data[bits_name].append(int(bits[i: j], 2))
                                j += 1
                # to open can data file and graph data
                with shelve.open(os.path.join('.', 'CAN_Message', 'message_info')) as can_data:
                    for data_name in list(can_data.keys()):
                        plt.figure(figsize=(10.5, 4.5), dpi=100)
                        plt.plot(can_data[data_name])
                        plt.grid()
                        plt.title(data_name)
                        plt.savefig(os.path.join('.', 'CAN_Message', ('CAN_' + str(target_id)), (data_name + '.png')))
                        plt.close()
                        print(data_name + '.png has saved.')


def main():
    parser = argparse.ArgumentParser(description='For CAN message crack.')
    parser.add_argument('--splitdata', action='store_true', required=False)
    parser.add_argument('--graphdata', action='store_true', required=False)
    parser.add_argument('--graphdata_speed', action='store_true', required=False)
    args = parser.parse_args()
    if args.splitdata:
        splitdata(input("Please enter the CSV file's name, like 'Trace.csv'."))
    elif args.graphdata:
        graphdata(input("Please enter the ID's name, like '37B', or 'all' for all ID."))
    elif args.graphdata_speed:
        graphdata_speed(input("Please enter the ID's name, like '37B', or 'all' for all ID."))
    else:
        print("Running with argument, '--splitdata' or '--graphdata', '--graphdata_speed'.")


if __name__ == '__main__':
    main()
