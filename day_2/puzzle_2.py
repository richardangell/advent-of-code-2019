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

    for noun in range(100):

        for verb in range(100):

            intcode_program[1] = noun
            intcode_program[2] = verb

            intcode_program_run = run_intcode_program(intcode_program)

            print(noun, verb, intcode_program_run[0])

            if intcode_program_run[0] == 19690720:
                
                break

        if intcode_program_run[0] == 19690720:
            
            break

    print(f'100  * noun {noun} + verb {verb}: {(100 * noun) + verb}') 

