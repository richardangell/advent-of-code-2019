import sys
sys.path.append('..')
import helpers



def calculate_module_fuel(mass):
    '''Function to calculate fuel for module given it's mass.'''

    return int(mass / 3) - 2



if __name__ == '__main__':

    file = "input_1.txt"

    inputs = helpers.load_input(file, remove_lines_breaks = True, convert_to_int = True)

    fuel = [calculate_module_fuel(x) for x in inputs]

    total_fuel = sum(fuel)

    print(f'total fuel required: {total_fuel}') 

