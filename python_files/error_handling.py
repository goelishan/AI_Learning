
# def open_file(filename):
#     try:
#         with open(filename,'r') as f:
#             for data in f:
#                 print(data.strip())
#     except FileNotFoundError:
#         print('Error! file not found.')
#     except PermissionError:
#         print('There is permission issue on this file')
#     except Exception as e:
#         print(f'Unexpected error - {e}')
#     finally:
#         print('Open file method is accessible')



# open_file('C:/Users/igoel/Desktop/AI_Learning/practise_code/students_1.txt')
# # ---------------------------------------------------------------------------------------------------------------------------------

# Write a function read_marks(filename) that:
# Opens a CSV file (marks.csv) that has columns:
# Name,Math,Science,English
# Reads each row and prints the student name + total marks.
# Handle errors gracefully:
# If the file doesn’t exist → print "File not found"
# If the file is empty → print "File is empty"
# If the file has bad data (like text in marks) → print "Invalid data in file"
# Always print "Finished reading file" at the end (using finally).

import csv

def read_marks(filename):
    try:
        total_marks=0
        with open(filename,'r') as f:
            reader=csv.DictReader(f)

            rows=list(reader)
            if not rows:
                print('File is empty.')
            
            for row in rows:
                try:
                    total_marks=int(row['Math'])+int(row['Science'])+int(row['English'])
                    print(f'{row['Name']} -> Total Marks - {total_marks}')
                except ValueError:
                    print('Invalid data in file')
                    return
    except FileNotFoundError:
        print('File not found')
    finally:
        print('End of program.')


read_marks('C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/marks.csv')