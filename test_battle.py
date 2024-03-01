from rps_functions import battle

def test_module_and_function_name():
    from rps_functions import battle
    assert True

def test_players_are_dicts():
    from rps_functions import battle
    player1 = {}
    player2 = {}
    assert(player1, dict)

