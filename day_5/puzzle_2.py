import sys
sys.path.append('..')
import helpers



def run_intcode_program(intcode_program, input_value):
    '''Function to run intcode program.'''

    intcode_program_run = intcode_program[:]

    pos = 0

    opcode, mode_param_1, mode_param_2, mode_param_3 = get_parameter_modes(intcode_program_run[pos])

    while True:

        if opcode == 1:

            if mode_param_1 == 0:
                
                param_1 = intcode_program_run[intcode_program_run[pos + 1]]

            elif mode_param_1 == 1:

                param_1 = intcode_program_run[pos + 1]

            else:

                raise ValueError(f'got mode_param_1 value {mode_param_1} in position {pos}')

            if mode_param_2 == 0:
                
                param_2 = intcode_program_run[intcode_program_run[pos + 2]]

            elif mode_param_2 == 1:

                param_2 = intcode_program_run[pos + 2]

            else:

                raise ValueError(f'got mode_param_2 value {mode_param_2} in position {pos}')
            
            print(f'opcode: {opcode} mode_param_1: {mode_param_1} param_1: {param_1} mode_param_2: {mode_param_2} param_2: {param_2} pos: {pos} param_3 pos: {intcode_program_run[pos + 3]}')

            intcode_program_run[intcode_program_run[pos + 3]] = param_1 + param_2

            pos += 4

        elif opcode == 2:   

            if mode_param_1 == 0:
                
                param_1 = intcode_program_run[intcode_program_run[pos + 1]]

            elif mode_param_1 == 1:

                param_1 = intcode_program_run[pos + 1]

            else:

                raise ValueError(f'got mode_param_1 value {mode_param_1} in position {pos}')

            if mode_param_2 == 0:
                
                param_2 = intcode_program_run[intcode_program_run[pos + 2]]

            elif mode_param_2 == 1:

                param_2 = intcode_program_run[pos + 2]

            else:

                raise ValueError(f'got mode_param_2 value {mode_param_2} in position {pos}')
            
            print(f'opcode: {opcode} mode_param_1: {mode_param_1} param_1: {param_1} mode_param_2: {mode_param_2} param_2: {param_2} pos: {pos} param_3 pos: {intcode_program_run[pos + 3]}')

            intcode_program_run[intcode_program_run[pos + 3]] = param_1 * param_2

            pos += 4

        elif opcode == 3:

            print(f'opcode: {opcode} pos: {pos}')

            intcode_program_run[intcode_program_run[pos + 1]] = input_value

            pos += 2

        elif opcode == 4:
            
            print(f'opcode: {opcode} pos: {pos}')

            debug_value = intcode_program_run[intcode_program_run[pos + 1]]

            pos += 2

            print(f'------ debug output: {debug_value} ------')

        elif opcode == 5:

            if mode_param_1 == 0:
                
                param_1 = intcode_program_run[intcode_program_run[pos + 1]]

            elif mode_param_1 == 1:

                param_1 = intcode_program_run[pos + 1]

            else:

                raise ValueError(f'got mode_param_1 value {mode_param_1} in position {pos}')

            if mode_param_2 == 0:
                
                param_2 = intcode_program_run[intcode_program_run[pos + 2]]

            elif mode_param_2 == 1:

                param_2 = intcode_program_run[pos + 2]

            else:

                raise ValueError(f'got mode_param_2 value {mode_param_2} in position {pos}')
            
            print(f'opcode: {opcode} mode_param_1: {mode_param_1} param_1: {param_1} mode_param_2: {mode_param_2} param_2: {param_2} pos: {pos}')

            if param_1 != 0:

                pos = param_2

            else:

                pos += 3

        elif opcode == 6:

            if mode_param_1 == 0:
                
                param_1 = intcode_program_run[intcode_program_run[pos + 1]]

            elif mode_param_1 == 1:

                param_1 = intcode_program_run[pos + 1]

            else:

                raise ValueError(f'got mode_param_1 value {mode_param_1} in position {pos}')

            if mode_param_2 == 0:
                
                param_2 = intcode_program_run[intcode_program_run[pos + 2]]

            elif mode_param_2 == 1:

                param_2 = intcode_program_run[pos + 2]

            else:

                raise ValueError(f'got mode_param_2 value {mode_param_2} in position {pos}')
            
            print(f'opcode: {opcode} mode_param_1: {mode_param_1} param_1: {param_1} mode_param_2: {mode_param_2} param_2: {param_2} pos: {pos}')

            if param_1 == 0:

                pos = param_2

            else:

                pos += 3

        elif opcode == 7:

            if mode_param_1 == 0:
                
                param_1 = intcode_program_run[intcode_program_run[pos + 1]]

            elif mode_param_1 == 1:

                param_1 = intcode_program_run[pos + 1]

            else:

                raise ValueError(f'got mode_param_1 value {mode_param_1} in position {pos}')

            if mode_param_2 == 0:
                
                param_2 = intcode_program_run[intcode_program_run[pos + 2]]

            elif mode_param_2 == 1:

                param_2 = intcode_program_run[pos + 2]

            else:

                raise ValueError(f'got mode_param_2 value {mode_param_2} in position {pos}')

            if param_1 < param_2:

                intcode_program_run[intcode_program_run[pos + 3]] = 1

            else:

                intcode_program_run[intcode_program_run[pos + 3]] = 0

            print(f'opcode: {opcode} mode_param_1: {mode_param_1} param_1: {param_1} mode_param_2: {mode_param_2} param_2: {param_2} pos: {pos}')

            pos += 4

        elif opcode == 8:

            if mode_param_1 == 0:
                
                param_1 = intcode_program_run[intcode_program_run[pos + 1]]

            elif mode_param_1 == 1:

                param_1 = intcode_program_run[pos + 1]

            else:

                raise ValueError(f'got mode_param_1 value {mode_param_1} in position {pos}')

            if mode_param_2 == 0:
                
                param_2 = intcode_program_run[intcode_program_run[pos + 2]]

            elif mode_param_2 == 1:

                param_2 = intcode_program_run[pos + 2]

            else:

                raise ValueError(f'got mode_param_2 value {mode_param_2} in position {pos}')

            if param_1 == param_2:

                intcode_program_run[intcode_program_run[pos + 3]] = 1

            else:

                intcode_program_run[intcode_program_run[pos + 3]] = 0

            print(f'opcode: {opcode} mode_param_1: {mode_param_1} param_1: {param_1} mode_param_2: {mode_param_2} param_2: {param_2} pos: {pos}')

            pos += 4

        elif opcode == 99:

            break

        else:

            raise ValueError(f'got value {opcode} for opcode in positon {pos}')

        opcode, mode_param_1, mode_param_2, mode_param_3 = get_parameter_modes(intcode_program_run[pos])

    return debug_value






def get_parameter_modes(opcode):
    '''Get opcode and parameter nodes from initial opcode value.'''

    opcode = str(opcode)

    len_opcode = len(opcode)

    # fill in any missing values with 0
    opcode_full = ((5 - len_opcode) * '0') + opcode

    if not len(opcode_full) == 5:

        raise ValueError(f'expecting opcode_full length 5 but got {opcode_full}')

    return int(opcode_full[3:]), int(opcode_full[2]), int(opcode_full[1]), int(opcode_full[0])







if __name__ == '__main__':

    file = "input_1.txt"

    intcode_program = helpers.load_input_sinle_list(file, convert_to_int = True)

    intcode_program_run = run_intcode_program(intcode_program, input_value = 5)

    print(f'result: {intcode_program_run}')