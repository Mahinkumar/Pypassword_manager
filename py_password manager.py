import secrets
import string
from datetime import datetime
import time

k_length = 0
length = 0


def password_reader():
    file_object = open("password_data.txt", "r")
    print(file_object.read())
    print("")
    time.sleep(1)
    reset_function()


def code_generator():
    print("---------------------------------------------------")
    string4pass = input('''Type a hint or the website name for Tagging your password: ''')
    string_len = int(len(string4pass))

    if string_len == 0:
        print("Hint or name is mandatory, so you don't lose password in future")
        code_generator()

    else:
        n = int(input('no. of digits you want in the password:'))
        print("")
        print('select password type,')
        print('Type 1 - includes uppercase, lowercase and digits          || PRESS - 1')
        print('Type 2 - includes uppercase, lowercase, digits and symbols || PRESS - 2')
        pass_type = int(input('>>>'))

        if pass_type == 1:
            secure_pass1 = ''.join(
                secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
                for _ in range(n))
            print(f'Generated password for {string4pass} is : {secure_pass1}')
            file_object = open("password_data.txt", "a")
            file_object.writelines(f"Generated password on {datetime.now()} for {string4pass} is {secure_pass1}\r")
            file_object.close()
            print("---------------------------------------------------")

        elif pass_type == 2:
            secure_pass2 = ''.join(
                secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation)
                for _ in range(n))
            print(f'Generated password for {string4pass} is : {secure_pass2}')
            file_object = open("password_data.txt", "a")
            file_object.writelines(f"Generated password on {datetime.now()} for {string4pass} is {secure_pass2}\r")
            file_object.close()
                 
    reset_function()


def task_manager():
    print('Starting Password manager')
    time.sleep(2)
    print('What do you want to do??')
    print('Get random password                  - PRESS 1')
    print('Check recently generated password    - PRESS 2')
    Task = int(input('>>>'))

    if Task == 1:
        code_generator()

    elif Task == 2:
        password_reader()

    reset_function()


def reset_function():
    print("---------------------------------------------------")
    print('Press 1 to restart the tool or press 2 to close the tool')
    reset = int(input('>>>'))

    if reset == 1:
        print("----------------------RESTART-----------------------")
        task_manager()

    elif reset == 2:
        print("Thank you for using the tool")


task_manager()
