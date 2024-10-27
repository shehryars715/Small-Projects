import random


def play():
    player = input("Rock(r), Paper(p) or Scissors(s) ").lower()
    computer = random.choice(['r','p','s'])
    if player == computer:
        print(f"Tie as computer also chose {computer}")
    elif (player=='r' and computer=='s') or (player=='s' and computer=='p') or (player=='p' and computer=='r'):
        print(f"You won because you chose {player} and computer was {computer}")
    else:
        print(f"Computer won as computer was {computer} and you were {player}")

play()
