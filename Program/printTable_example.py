# coding =utf-8


def printTable(a_list):
    colwidth = [0] * len(a_list)
    width = max(len(a_list[i]) for i in range(len(a_list)))
    for i in range(len(a_list)):
        colwidth[i] = max(len(a_list[i][j]) for j in range(len(a_list[i])))
    for j in range(width):
        for i in range(len(a_list)):
            try:
                print(a_list[i][j].rjust(max(i for i in colwidth)), end='')
            except IndexError:
                break
        print()

    #print(a_list, colwidth, width)



tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David', 'Sherlock'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
