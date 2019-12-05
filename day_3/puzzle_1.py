import sys
sys.path.append('..')
import helpers



def turn_path_to_coords(path):
    '''Function to iterate through path and produce a list of coords the path touches.'''

    coords = [(0, 0)]

    for i, p in enumerate(path):

        direction = p[0]

        step_size = int(p[1:])

        if direction == 'R':

            coords.append((coords[i][0] + step_size, coords[i][1]))

        elif direction == 'L':

            coords.append((coords[i][0] - step_size, coords[i][1]))

        elif direction == 'U':

            coords.append((coords[i][0], coords[i][1] + step_size))

        elif direction == 'D': 

            coords.append((coords[i][0], coords[i][1] - step_size))

        else:

            raise ValueError(f'unexpected first character in path {p}')
    
    return coords



def manhattan_distance(a, b):
    '''Function to calculate manhattan distance between 2 coordinates.'''

    return abs(a[0] - b[0]) + abs(a[1] - b[1])



def wires_cross(dir_a, start_a, end_a, dir_b, start_b, end_b):
    '''Function to find the point at which 2 wire sections cross.'''

    only_possible_x = None
    only_possible_y = None

    if dir_a[0] in ['R', 'L']:

        # assume that wires can't run along top of each other
        if dir_b[0] in ['R', 'L']: 

            return False, (None, None)

        else:

            only_possible_y = start_a[1]

            y_range = [start_b[1], end_b[1]]
            
    elif dir_a[0] in ['U', 'D']:

        if dir_b[0] in ['U', 'D']: 

            return False, (None, None)

        else:

            only_possible_x = start_a[0]

            x_range = [start_b[0], end_b[0]]

    if dir_b[0] in ['R', 'L']:

        only_possible_y = start_b[1]

        y_range = [start_a[1], end_a[1]]

    elif dir_b[0] in ['U', 'D']:

        only_possible_x = start_b[0]
        
        x_range = [start_b[0], end_b[0]]

    if only_possible_x is None:

        print(dir_a, start_a, end_a, dir_b, start_b, end_b)

        raise ValueError('only_possible_x not found when wires are perpendicular')

    if only_possible_y is None:

        raise ValueError('only_possible_y not found when wires are perpendicular')

    x_range.sort()
    y_range.sort()
    
    # assume intersection means that lines are no overlapping
    if (only_possible_x > x_range[0]) and (only_possible_x < x_range[1]):

        if (only_possible_y > y_range[0]) and (only_possible_y < y_range[1]):

            return True, (only_possible_x, only_possible_y)

    return False, (None, None)


def find_all_cross_points(path_a, path_b, path_coords_a, path_coords_b):
    '''Function to find all cross points between full path of 2 lines.'''

    cross_points = []

    i = -1

    for line_direction_a, line_start_coord_a, line_end_coord_a in zip(path_a, path_coords_a[:-1], path_coords_a[1:]):

        i += 1

        j = -1

        for line_direction_b, line_start_coord_b, line_end_coord_b in zip(path_b, path_coords_b[:-1], path_coords_b[1:]):

            j += 1

            wire_sections_cross, cross_coords = wires_cross(
                line_direction_a, 
                line_start_coord_a, 
                line_end_coord_a, 
                line_direction_b, 
                line_start_coord_b, 
                line_end_coord_b
            )
            
            if wire_sections_cross:

                cross_points.append(cross_coords)

    return cross_points


def find_min_manhattan_distances(cross_points):
    '''Function to find the min manhattan distance from origin for all coordinates supplied.'''

    manhattan_distances = []

    for cross_point in cross_points:

        m_dist = manhattan_distance((0, 0), cross_point)

        manhattan_distances.append(m_dist)

    result = min(manhattan_distances)

    return result



def find_cross_points_and_min_distance(path_a, path_b, path_coords_a, path_coords_b):
    '''Function to combine find_all_cross_points and find_min_manhattan_distances functions.'''

    cross_points = find_all_cross_points(path_a, path_b, path_coords_a, path_coords_b)

    result = find_min_manhattan_distances(cross_points)

    return result



if __name__ == '__main__':

    file = "input_1.txt"

    wire_paths = helpers.load_input_multi_list(file, convert_to_int = False)

    path_a = wire_paths[0]
    path_b = wire_paths[1]
    
    path_coords_a = turn_path_to_coords(path_a)
    path_coords_b = turn_path_to_coords(path_b)

    result = find_cross_points_and_min_distance(path_a, path_b, path_coords_a, path_coords_b)
    
    print(f'closest cross point manhattan distance: {result}') 
