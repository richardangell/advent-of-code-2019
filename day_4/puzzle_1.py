import sys



def password_contains_duplicated_digits(string_value):
    '''Checks if any adjacent digits are the same.'''

    duplicated_digits_to_check = [
        '00',
        '11',
        '22',
        '33',
        '44',
        '55',
        '66',
        '77',
        '88',
        '99'
    ]

    for dd in duplicated_digits_to_check:

        if dd in string_value:

            return True

    return False



def password_increasing(string_value):
    '''Checks if the digits in a password are monotonically increasing.'''

    if (int(string_value[0]) <= int(string_value[1])) & \
        (int(string_value[1]) <= int(string_value[2])) & \
        (int(string_value[2]) <= int(string_value[3])) & \
        (int(string_value[3]) <= int(string_value[4])) & \
        (int(string_value[4]) <= int(string_value[5])):

        return True

    else:

        return False


def is_valid_password(string_value):
    '''Checks if password is monotonically increasing and has duplciated digits.'''

    return password_contains_duplicated_digits(string_value) & password_increasing(string_value)



if __name__ == '__main__':

    input_range = (231832, 767346)

    count_valid_passwords = 0

    for i in range(input_range[0], input_range[1] + 1):

        if is_valid_password(str(i)):

            count_valid_passwords += 1

    print(f'valid passwords; {count_valid_passwords}')



