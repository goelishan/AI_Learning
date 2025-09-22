
# scanning files for phone numbers and emails

import re
import os

# Regex patterns

# Matches phone numbers anywhere in the text line
phone_pattern = r'(\+91|0)?\d{10}'

# Matches emails anywhere in the text line
email_pattern = r'[\w\.-]+@[a-zA-Z]+\.[a-zA-Z]{2,3}'



# Validator functions

def is_phone_number(number):
    return bool(re.findall(phone_pattern,number))

def is_email_address(email):
    return bool(re.findall(email_pattern,email))

# File scanner

def scan_files_for_pattern(folder_path):

    for folder_name, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith('.txt'):
                file_path=os.path.join(folder_name,filename)
                print(f'Scanning file: {file_path}')

                with open(file_path,'r',encoding='utf-8') as f:
                    for line_number,line in enumerate(f,start=1):
                        line=line.strip()

                        if is_phone_number(line):
                            print(f'Line number-{line_number},Phone - {line}')
                        elif is_email_address(line):
                            print(f'Line number-{line_number}, Email ->{line}')

                            

if __name__=='__main__':
    folder_to_scan='C:/Users/igoel/Desktop/AI_Learning/practise_code/'

    scan_files_for_pattern(folder_to_scan)

