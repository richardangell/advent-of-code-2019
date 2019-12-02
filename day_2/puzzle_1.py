import sys
sys.path.append('..')
import helpers



def run_intcode_program(intcode_program):
    '''Function to run intcode program.'''

    intcode_program_run = intcode_program[:]

    pos = 0

    opcode = intcode_program_run[pos]

    while True:

        if opcode == 1:

            intcode_program_run[intcode_program_run[pos + 3]] = intcode_program_run[intcode_program_run[pos + 1]] + intcode_program_run[intcode_program_run[pos + 2]]
 
        elif opcode == 2:

            intcode_program_run[intcode_program_run[pos + 3]] = intcode_program_run[intcode_program_run[pos + 1]] * intcode_program_run[intcode_program_run[pos + 2]]

        elif opcode == 99:

            break

        else:

            raise ValueError(f'got value {opcode} for opcode in positon {pos}')
        
        pos += 4

        opcode = intcode_program_run[pos]

    return intcode_program_run



if __name__ == '__main__':

    file = "input_1.txt"

    intcode_program = helpers.load_input_sinle_list(file, convert_to_int = True)

    # "before running the program, replace position 1 with the value 12 and replace position 2 with the value 2."
    intcode_program[1] = 12
    intcode_program[2] = 2

    intcode_program_run = run_intcode_program(intcode_program)

    pos_0_value = intcode_program_run[0]

    print(f'poisiton 0 value: {pos_0_value}') 

