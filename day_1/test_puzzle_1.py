import puzzle_1



def test_puzzle_1_fuel_calc():

    assert puzzle_1.calculate_module_fuel(12) == 2
    assert puzzle_1.calculate_module_fuel(14) == 2
    assert puzzle_1.calculate_module_fuel(1969) == 654
    assert puzzle_1.calculate_module_fuel(100756) == 33583


