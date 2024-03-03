import pytest

from rps_functions import battle

def test_module_and_function_name():
    from rps_functions import battle
    assert True

def test_empty_players():
    player1 = {}
    player2 = {}
    with pytest.raises(ValueError):
        battle(player1,player2)
def test_outcome_results():
    from rps_functions import battle
    player1 = {"choice": "null", "discord_id": 123456, "username": "Cherub Fish"}
    player2 = {"choice": "null", "discord_id": 654321, "username": "Jawfish"}
    choices = ["rock", "paper", "scissors"]
    for x in choices:
        player1["choice"] = x
        for y in choices:
            player2["choice"] = y
            outcome = battle(player1, player2)
            if x == y:
                assert outcome is None  # tie cases
            if x == "rock":
                if y == "paper":
                    assert outcome == player2
                if y == "scissors":
                    assert outcome == player1
            if x == "paper":
                if y == "scissors":
                    assert outcome == player2
                if y == "rock":
                    assert outcome == player1
            if x == "scissors":
                if y == "rock":
                    assert outcome == player2
                if y == "paper":
                    assert outcome == player1




