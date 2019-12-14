import puzzle_2



def test_puzzle_2():

    assert puzzle_2.password_contains_duplicated_digits('112233') == True
    assert puzzle_2.password_contains_duplicated_digits('123444') == False
    assert puzzle_2.password_contains_duplicated_digits('111122') == True



  
  
  
