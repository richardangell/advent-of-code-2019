import sys
sys.path.append('..')
import helpers



def find_orbital_transfers(orbits):
    '''Function to find create mapping for orbits (outside inwards), then find the path from santa and you 
    to the COM of the system, find the common planet and finally the number of orbital transfers between
    the planet santa and you are orbitting.
    '''

    orbits_split = [x.split(')') for x in orbits]

    orbits_split_reverse_dict = {}
    
    for p in orbits_split:

        orbits_split_reverse_dict[p[1]] = p[0]

    santa_path_to_com = find_path_to_center(orbits_split_reverse_dict, 'SAN')

    you_path_to_com = find_path_to_center(orbits_split_reverse_dict, 'YOU')

    common_planet, santa_orbital_transfers, you_orbital_transfers = find_first_common_element(santa_path_to_com, you_path_to_com)

    # remove 1 transfer for each because we are after orbtial transfers between the planets each is orbitting
    total_orbital_transfers = santa_orbital_transfers + you_orbital_transfers - 2

    return total_orbital_transfers


def find_path_to_center(orbits, p):
    '''Function to find path from given planet p to COM from orbits dict.'''

    current_planet = p

    path = [current_planet]

    while current_planet != 'COM':

        next_planet = orbits[current_planet]

        path.append(next_planet)

        current_planet = next_planet

    return path


def find_first_common_element(l1, l2):
    '''Function to find the first common element on l1 and l2 and also return it's index in l1 and l2.'''

    for i, v1 in enumerate(l1):

        for j, v2 in enumerate(l2):

            if v1 == v2:

                break

        if v1 == v2:

            break

    return v1, i, j







if __name__ == '__main__':

    file = "input_1.txt"

    orbit_map = helpers.load_input(file, remove_lines_breaks = True)
    
    total_orbits = find_orbital_transfers(orbit_map)

    print(f'total orbits; {total_orbits}')

