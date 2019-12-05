import puzzle_1



def test_1():

    wire_paths = puzzle_1.helpers.load_input_multi_list('input_test_1.txt', convert_to_int = False)

    path_a = wire_paths[0]
    path_b = wire_paths[1]
    
    path_coords_a = puzzle_1.turn_path_to_coords(path_a)
    path_coords_b = puzzle_1.turn_path_to_coords(path_b)

    assert puzzle_1.find_cross_points_and_min_distance(path_a, path_b, path_coords_a, path_coords_b) == 159


def test_2():

    wire_paths = puzzle_1.helpers.load_input_multi_list('input_test_2.txt', convert_to_int = False)

    path_a = wire_paths[0]
    path_b = wire_paths[1]
    
    path_coords_a = puzzle_1.turn_path_to_coords(path_a)
    path_coords_b = puzzle_1.turn_path_to_coords(path_b)

    assert puzzle_1.find_cross_points_and_min_distance(path_a, path_b, path_coords_a, path_coords_b) == 135




  
  
  
