import sys
sys.path.append('..')
import helpers



def find_total_orbitals(orbits):
    '''Function to create a dictionary of orbits, then calculate cumulative orbits, finally return
    total number of orbitals in system.
    '''

    orbits_split = [x.split(')') for x in orbits]

    orbits_split_reverse_dict = {}
    
    for p in orbits_split:

        orbits_split_reverse_dict[p[1]] = p[0]

    planets_with_orbitals = set([x[0] for x in orbits_split])

    planets_without_orbitals = set([x[1] for x in orbits_split]) - planets_with_orbitals

    orbits_map = {}

    for p in orbits_split:

        if p[0] in orbits_map.keys():

            orbits_map[p[0]]['orbtials'].append(p[1])
            orbits_map[p[0]]['n'] += 1

        else:

            orbits_map[p[0]] = {
                'orbtials': [p[1]],
                'n': 1,
                'cumulative_n': 0
            }

    # add planets which do not have anything orbiting them
    for p in planets_without_orbitals:

        orbits_map[p] = {
            'orbtials': [],
            'n': 0,
            'cumulative_n': 0
        }

    if not len(planets_with_orbitals) + len(planets_without_orbitals) == len(orbits_map.keys()):

        raise ValueError(f'orbits_map does not have the expected number of keys; {len(planets_with_orbitals) + len(planets_without_orbitals)} got {len(orbits_map.keys())}')

    orbitals_com = count_cumulative_orbitals_recursive(orbits_map, p = 'COM')

    total_orbitals = 0

    for k, v in orbits_map.items():

        total_orbitals += v['cumulative_n']

    return total_orbitals



def count_cumulative_orbitals_recursive(orbits_map, p):

    if orbits_map[p]['n'] == 0:

        orbits_map[p]['cumulative_n'] = 0

        return orbits_map[p]['cumulative_n']

    else:   

        orbits_map[p]['cumulative_n'] = sum([(1 + count_cumulative_orbitals_recursive(orbits_map, x)) for x in orbits_map[p]['orbtials']])

        return orbits_map[p]['cumulative_n']



if __name__ == '__main__':

    file = "input_1.txt"

    orbit_map = helpers.load_input(file, remove_lines_breaks = True)
    
    total_orbits = find_total_orbitals(orbit_map)

    print(f'total orbits; {total_orbits}')

