import puzzle_2



def test_1():

    orbit_map = puzzle_2.helpers.load_input('input_test_2.txt', remove_lines_breaks = True)

    result = puzzle_2.find_orbital_transfers(orbit_map)

    assert result == 4
