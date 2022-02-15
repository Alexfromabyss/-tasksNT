# Task3
import sys

def values_dict(file_name2):
   values_id, values_res = list(), list()
   with open(file_name2, 'r', encoding='utf-8') as values:
      for new_line in values:
         if 'id' in new_line:
            local_id = new_line[new_line.index(':') + 2:-2]
            values_id.append(local_id)
         if 'value' in new_line and not 'values' in new_line:
            values_res.append(new_line[new_line.index(':') + 2:-1])
   values_all = dict(zip(values_id, values_res))
   return values_all

def replace(file_name1, values_all):
   refresh_list = list()
   idx = ''
   with open(file_name1, 'r', encoding='utf-8') as tests:
      for new_line in tests:
         if 'id' in new_line:
            idx = new_line[new_line.index(':') + 2:-2]
         if new_line.find('"value":') != -1 and idx in values_all:
            new_line = new_line.replace('""', values_all[idx])
         refresh_list.append(new_line)
   return refresh_list

def write(refresh_list):
   with open('report.json', 'w', encoding='utf-8') as create:
      for i in refresh_list:
         create.write(i)
   return 0

file_name1, file_name2 = sys.argv[1], sys.argv[2]

if file_name1 != 'tests.json':
   file_name1, file_name2 = file_name2, file_name1

values_all = values_dict(file_name2)
refresh_list = replace(file_name1, values_all)
print(*refresh_list)
create_new_folder = write(refresh_list)