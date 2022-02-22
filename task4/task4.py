# Task4

import sys
from math import ceil

file_name1 = sys.argv[1]
num, ans = list(), 0
with open(file_name1, 'r', encoding='utf-8') as input_nums:
    for string in input_nums:
        num.append(int(string.strip()))
mediana = 0 if len(num) == 0 else ceil(sum(num) / len(num))
for i in num:
    ans += abs(i - mediana)
print(ans)
