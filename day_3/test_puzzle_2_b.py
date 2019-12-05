import puzzle_1
import puzzle_2_b



def test_1():

    wire_paths = puzzle_1.helpers.load_input_multi_list('input_test_1.txt', convert_to_int = False)

    path_a = wire_paths[0]
    path_b = wire_paths[1]
    
    path_coords_a = puzzle_2_b.trace_path_coords(path_a)
    path_coords_b = puzzle_2_b.trace_path_coords(path_b)

    assert puzzle_2_b.find_min_wire_distance_cross(path_coords_a, path_coords_b) == 610


def test_2():

    wire_paths = puzzle_1.helpers.load_input_multi_list('input_test_2.txt', convert_to_int = False)

    path_a = wire_paths[0]
    path_b = wire_paths[1]
    
    path_coords_a = puzzle_2_b.trace_path_coords(path_a)
    path_coords_b = puzzle_2_b.trace_path_coords(path_b)

    assert puzzle_2_b.find_min_wire_distance_cross(path_coords_a, path_coords_b) == 410




  
  
  
