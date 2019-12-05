
def load_input(file, remove_lines_breaks = False, convert_to_int = False):
    '''Function to load input with optional processing.'''

    with open(file) as f:

        lines = f.readlines()

    if remove_lines_breaks:

        lines = [x.replace('\n', '') for x in lines]

    if convert_to_int:

        lines = [int(x) for x in lines]

    return lines



def load_input_sinle_list(file, sep = ',', convert_to_int = False):
    '''Function to load input which is a single row of a list, with optional processing.'''

    with open(file) as f:

        line = f.readlines()

    if len(line) > 1:

        raise ValueError(f'expecting file to have 1 line got {len(line)}')

    line = line[0].replace('\n', '')

    line = line.split(sep)

    if convert_to_int:

        line = [int(x) for x in line]

    return line



def load_input_multi_list(file, sep = ',', convert_to_int = False):
    '''Function to load input which is a multiple rows of lists, with optional processing.'''

    with open(file) as f:

        lines = f.readlines()

    for i in range(len(lines)):

        lines[i] = lines[i].replace('\n', '')

        lines[i] = lines[i].split(sep)

    if convert_to_int:

        for i in range(len(lines)):

            lines[i] = [int(x) for x in lines[i]]

    return lines