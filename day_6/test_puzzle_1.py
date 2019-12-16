import puzzle_1



def test_1():

    orbit_map = puzzle_1.helpers.load_input('input_test_1.txt', remove_lines_breaks = True)

    result = puzzle_1.find_total_orbitals(orbit_map)

    assert result == 42
