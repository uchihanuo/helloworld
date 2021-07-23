# coding = utf-8

print('Please input number\' range of you wander.')
max_num = int(input())
num_list = list(range(1, max_num + 1))
prime_list = []
i = 1
while i < max_num:
    for num in num_list:
        if num % i == 0 and num / i != 1:
