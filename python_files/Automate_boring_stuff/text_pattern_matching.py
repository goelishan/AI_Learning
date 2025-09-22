
# # validate if given string is a valid Indian Phone numbers

import re

# vaidate phone number
def validate_phone(number_list):

    pattern=r'^(\+91|0)?\d{10}$'

    for num in number_list:
        if re.match(pattern,num):
            print(f'{num} is Valid!')
        else:
            print(f'{num} is not valid')


# Validate email address 

def validate_email(email_list):

    pattern=r'^[\w\.-]+@[a-zA-Z]+\.[a-zA-Z]{2,3}$'

    for email in email_list:
        if re.match(pattern,email):
            print(f'{email} is a valid email address.')
        else:
            print(f'{email} is not a valid email address')



# Validate Indian Pan Cards

def validate_pan_card(pan_list):

    pattern=r'^[A-Z]{5}[0-9]{4}[A-Z]$'

    for pan in pan_list:
        if re.match(pattern,pan):
            print(f'{pan} is a valid pan card number')
        else:
            print(f'{pan} is not a valid pan card number')


# ------------Main---------------------------------------------------------------------

if __name__=='__main__':
    phone_numbers = [
        "9876543210", "09876543210", "+919876543210", 
        "987654321", "12345", "99123456789"
    ]
    
    emails = [
        "user123@gmail.com", "first.last@yahoo.in", "hello_world-99@outlook.org",
        "user@123.com", "@gmail.com", "username@.com"
    ]
    
    pans = [
        "ABCDE1234F", "PQRST6789Z", "AAAAA0000A", "abcde1234f"
    ]
    
    validate_phone(phone_numbers)
    print("\n")
    validate_email(emails)
    print("\n")
    validate_pan_card(pans)