import sys
sys.path.append('..')
import helpers



def trace_path_coords(path):
    '''Function to iterate through path and produce a list of coords the path touches.'''

    coords = [(0, 0)]

    for i, p in enumerate(path):

        direction = p[0]

        step_size = int(p[1:])

        if direction == 'R':

            for x in range(step_size):
                
                coords.append((coords[len(coords)-1][0] + 1, coords[len(coords)-1][1]))

        elif direction == 'L':

            for x in range(step_size):

                coords.append((coords[len(coords)-1][0] - 1, coords[len(coords)-1][1]))

        elif direction == 'U':

            for x in range(step_size):

                coords.append((coords[len(coords)-1][0], coords[len(coords)-1][1] + 1))

        elif direction == 'D': 
            
            for x in range(step_size):

                coords.append((coords[len(coords)-1][0], coords[len(coords)-1][1] - 1))

        else:

            raise ValueError(f'unexpected first character in path {p}')
    
    return coords
    


def find_min_manhatten_distance_cross(path_a, path_b):
    '''Function to find coords passed by both wires and return the min manhattan distance for these
    cross points.
    '''

    cross_points = set(path_a) & set(path_b)

    # remove origin
    cross_points = [x for x in cross_points if x[0] != 0 and x[1] != 0]

    result = find_min_manhattan_distances(cross_points)

    return result



def manhattan_distance(a, b):
    '''Function to calculate manhattan distance between 2 coordinates.'''

    return abs(a[0] - b[0]) + abs(a[1] - b[1])



def find_min_manhattan_distances(cross_points):
    '''Function to find the min manhattan distance from origin for all coordinates supplied.'''

    manhattan_distances = []

    for cross_point in cross_points:

        m_dist = manhattan_distance((0, 0), cross_point)

        manhattan_distances.append(m_dist)

    result = min(manhattan_distances)

    return result


# using NW's idea
if __name__ == '__main__':

    file = "input_1.txt"

    wire_paths = helpers.load_input_multi_list(file, convert_to_int = False)

    path_a = wire_paths[0]
    path_b = wire_paths[1]

    path_coords_a = trace_path_coords(path_a)
    path_coords_b = trace_path_coords(path_b)

    result = find_min_manhatten_distance_cross(path_coords_a, path_coords_b)

    print(f'closest cross point manhattan distance: {result}') 


