import puzzle_1_b



def test_1_b():

    wire_paths = puzzle_1_b.helpers.load_input_multi_list('input_test_1.txt', convert_to_int = False)

    path_a = wire_paths[0]
    path_b = wire_paths[1]
    
    path_coords_a = puzzle_1_b.trace_path_coords(path_a)
    path_coords_b = puzzle_1_b.trace_path_coords(path_b)

    assert puzzle_1_b.find_min_manhatten_distance_cross(path_coords_a, path_coords_b) == 159


def test_2_b():

    wire_paths = puzzle_1_b.helpers.load_input_multi_list('input_test_2.txt', convert_to_int = False)

    path_a = wire_paths[0]
    path_b = wire_paths[1]
    
    path_coords_a = puzzle_1_b.trace_path_coords(path_a)
    path_coords_b = puzzle_1_b.trace_path_coords(path_b)

    assert puzzle_1_b.find_min_manhatten_distance_cross(path_coords_a, path_coords_b) == 135




  
  
  
