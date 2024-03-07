import interactions
import json
def battle(player1,player2):
    choice = ['rock','paper','scissors']
    p1_choice = "choice" in player1.keys()
    p2_choice = "choice" in player2.keys()
    p1 = player1.get("choice", None)
    p2 = player2.get("choice", None)
    if not p1_choice:
        raise ValueError("p1 error")
    if not p2_choice:
        raise ValueError("p2 error")
    if p1 == "rock":
        if p2 =="scissors":
            return player1
        elif p2 =="paper":
            return player2
        elif p2 =="rock":
            return None
    elif p1 == "paper":
        if p2 =="rock":
            return player1
        elif p2 =="scissors":
            return player2
        elif p2 =="paper":
            return None
    elif p1 == "scissors":
        if p2 =="paper":
            return player1
        elif p2 =="rock":
            return player2
        elif p2 =="scissors":
            return None
    else:
        raise ValueError()



if __name__ == "__main__":
    player1 = {"choice": "rock", "discord_id": 123456, "username": "Cherub Fish"}
    player2 = {"choice": "paper", "discord_id": 654321, "username": "Jawfish"}
    try:
        result = battle(player1, player2)
    except ValueError:
        print("choice")
    print(result)
