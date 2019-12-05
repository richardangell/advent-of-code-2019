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
    


def find_min_wire_distance_cross(path_a, path_b):
    '''  '''

    cross_points = set(path_a) & set(path_b)

    wire_distance_to_crosses_a = []
    wire_distance_to_crosses_b = []

    for c in cross_points:

        for i, a in enumerate(path_a):

            if a == c:

                wire_distance_to_crosses_a.append(i)

        for j, b in enumerate(path_b):

            if b == c:

                wire_distance_to_crosses_b.append(j)

    wire_distance_to_crosses = [i + j for i, j in zip(wire_distance_to_crosses_a, wire_distance_to_crosses_b)]

    # remove origin 
    wire_distance_to_crosses = [x for x in wire_distance_to_crosses if x > 0]

    return min(wire_distance_to_crosses)



if __name__ == '__main__':

    file = "input_1.txt"

    wire_paths = helpers.load_input_multi_list(file, convert_to_int = False)

    path_a = wire_paths[0]
    path_b = wire_paths[1]

    path_coords_a = trace_path_coords(path_a)
    path_coords_b = trace_path_coords(path_b)

    result = find_min_wire_distance_cross(path_coords_a, path_coords_b)

    print(f'closest cross point total wire distance: {result}') 


