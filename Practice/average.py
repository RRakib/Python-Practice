input_list = [int(x) for x in (input('Enter 1st number: ').split())]
result = 0
for nums in input_list:
    result = result + nums
print('Result is: ', result / len(input_list))