import pytest

import rps_functions
from rps_functions import battle
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
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


#new
def test_decider():
    pass
def test_create_entry():

    pass
# 10 cases for check_entry
def test_check_entry_no_database():

    # check for json Y/N
    File_name = "test_rps_data_not_exist.json"
    guild_id = 123456789
    author_id = 987654321
    result=rps_functions.check_entry(File_name, guild_id, author_id)
    assert result == "Database not found"

def test_check_entry():
    pass
    # check for guild_id Y/N
    # check for author id Y/N
    # check for check user number 1/2/>2
    # else raise error

def test_update_entry():
    pass
def test_delete_entry():
    pass