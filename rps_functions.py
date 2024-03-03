choice = ["rock", "paper", "scissors"]

def battle(player1,player2):
    choice = ['rock','paper','scissors']

    if player1["choice"] == "rock":
        if player2["choice"] =="scissors":
            return player1
        elif player2["choice"] =="paper":
            return player2
        elif player2["choice"] =="rock":
            return None
    elif player1["choice"] == "paper":
        if player2["choice"] =="rock":
            return player1
        elif player2["choice"] =="scissors":
            return player2
        elif player2["choice"] =="paper":
            return None
    elif player1["choice"] == "scissors":
        if player2["choice"] =="paper":
            return player1
        elif player2["choice"] =="rock":
            return player2
        elif player2["choice"] =="scissors":
            return None
    else:
        raise ValueError()

#print(battle(player1=str,player2=str))

if __name__ == "__main__":
    player1 = {"choice": "rock", "discord_id": 123456, "username": "Cherub Fish"}
    player2 = {"choice": "paper", "discord_id": 654321, "username": "Jawfish"}
    result = battle(player1, player2)
    print(result)
