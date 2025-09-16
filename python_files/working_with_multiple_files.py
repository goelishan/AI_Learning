# import os

# # list all files in current directory
# files=os.listdir('.')
# print(files)

# # list only csv files
# csv_files=[f for f in os.listdir('.') if f.endswith('.csv')]
# print(csv_files)

# create new directory
# os.makedirs('backup',exist_ok=True)

# remove directory only if empty
# os.rmdir('backup')
# -----------------------------------------------------------------------------------------------------------------------
# reading multiple files in a folder.

# import os
# import csv

# folder='data'

# for filename in os.listdir(folder):
#     if filename.endswith('.csv'):
#         path=os.path.join(folder,filename)
#         with open(path,'r') as f:
#             reader=csv.DictReader(f)
#             rows=list(reader)
#             print(f'{filename} -> {len(rows)} rows')


# --------------------------------------------------------------------------------------------------------------------------

# writing in multiple files

# for i in range(3):
#     with open(f'file_{i}.txt','w') as f:
#         f.write(f'This is file number {i}\n')


# ---------------------------------------------------------------------------------------------------------------------------
# segregate files into separate folder according to the file type

import os
import shutil

# folder containing files

my_folder='C:/Users/igoel/Desktop/AI_Learning/practise_code'

file_types={
    '.csv':'csv_files',
    '.json':'json_files',
    '.py':'python_files'
}

# check target folder exists
for folder in file_types.values():
    os.makedirs(os.path.join(my_folder,folder),exist_ok=True)

# move files in respective folder
for filename in os.listdir(my_folder):
    file_path=os.path.join(my_folder,filename)

    # skip directories
    if os.path.isdir(file_path):
        continue

    # check file extension

    ext=os.path.splitext(filename)[1]
    if ext in file_types:
        target_folder=os.path.join(my_folder,file_types[ext])
        shutil.move(file_path,os.path.join(target_folder,filename))

        print(f'Moved {filename} to {target_folder}')