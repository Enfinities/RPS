from rps_functions import battle

def test_module_and_function_name():
    from rps_functions import battle
    assert True

def test_players_are_dicts():
    from rps_functions import battle
    player1 = {"name":"name", "option1":"rock", "option1":"paper", "option1":"scissors"}
    player2 = {"name":"name", "option1":"rock", "option1":"paper", "option1":"scissors"}
    assert isinstance(player1, dict)

