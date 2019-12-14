import sys



def password_contains_duplicated_digits(string_value):
    '''Checks if any adjacent digits are duplciated but don't appear more than twice.'''

    counts = [0] * 10

    string_value_split = list(string_value)

    for x in string_value:

        for i, d in enumerate(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):

            if x == d:

                counts[i] = counts[i] + 1

    return any([x == 2 for x in counts])



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



