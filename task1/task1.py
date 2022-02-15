# Task1

import sys
n, m = int(sys.argv[1]), int(sys.argv[2])
m = m - 1
array, ans_array = list(range(1, n + 1)), list()
left, right = array[0], array[0]
while True:
   left = right if left + m <= len(array) else (left + m) - len(array)
   right = right + m if right + m <= len(array) else (right + m) - len(array)
   ans_array.append(left)
   if right == array[0]:
      break
print(*ans_array, sep='')