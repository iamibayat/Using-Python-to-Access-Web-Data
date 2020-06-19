import re

file_handle = open("regex_sum_535663.txt", 'r')

sum = 0
for line in file_handle:
    line = line.rstrip()
    digits = re.findall('[0-9]+', line)
    for each_digit in digits:
        sum += int(each_digit)

print(sum)
