# Task2

import sys

file_name1, file_name2 = sys.argv[1], sys.argv[2]

with open(file_name1, 'r', encoding='utf-8') as in1, open(file_name2, 'r', encoding='utf-8') as in2:
   center = list(map(float, in1.readline().split()))
   center_point_x, center_point_y = center[0], center[1]
   center.clear()
   radius = int(in1.readline())
   for line in in2:
      line = list(map(float, line.split()))
      list_point_x, list_point_y = line[0], line[1]
      if (list_point_x - center_point_x) ** 2 + (list_point_y - center_point_y) ** 2 < radius ** 2:
         print(1)
      elif (list_point_x - center_point_x) ** 2 + (list_point_y - center_point_y) ** 2 == radius ** 2:
         print(0)
      else:
         print(2)