# coding = utf-8

import pprint

message = str(input('Please enter the message.'))

wordscount = {}
for character in message:
    wordscount.setdefault(character, 0)
    wordscount[character] += 1

print(wordscount)
pprint.pprint(wordscount)
# print(pprint.pformat(wordscount))
# for k, v in wordscount.items():
#     print('key: ' + k + ' value: ' + str(v), end='\n')
