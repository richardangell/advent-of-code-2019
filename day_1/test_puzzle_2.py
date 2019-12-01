import puzzle_2



def test_puzzle_2_fuel_calc():

    assert puzzle_2.calculate_module_fuel_recursive(12) == 2
    assert puzzle_2.calculate_module_fuel_recursive(14) == 2
    assert puzzle_2.calculate_module_fuel_recursive(1969) == 966
    assert puzzle_2.calculate_module_fuel_recursive(100756) == 50346


