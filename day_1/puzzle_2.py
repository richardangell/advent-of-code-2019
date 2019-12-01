import sys
sys.path.append('..')
import helpers



def calculate_fuel(mass):
    '''Function to calculate fuel for module given it's mass.'''

    return int(mass / 3) - 2



def calculate_module_fuel_recursive(mass):
    '''Function to calculate fuel for module given it's mass.'''

    fuel_for_module = calculate_fuel(mass)

    fuel_for_fuel = fuel_for_module

    while fuel_for_fuel > 0:

        fuel_for_fuel = calculate_fuel(fuel_for_fuel)

        if fuel_for_fuel >= 0:

            fuel_for_module += fuel_for_fuel

    return fuel_for_module



if __name__ == '__main__':

    file = "input_1.txt"

    inputs = helpers.load_input(file, remove_lines_breaks = True, convert_to_int = True)

    fuel = [calculate_module_fuel_recursive(x) for x in inputs]

    total_fuel = sum(fuel)

    print(f'total fuel required: {total_fuel}') 

