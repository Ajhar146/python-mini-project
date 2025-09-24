import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the Number of Players(2-4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4.")
    else:
        print("Invalid, try again")

max_score = 20
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for player_idx in range(players):
        print("\nplayer",player_idx+1,"turn has started!\n")
        current_score = 0

        while True:
            is_roll = input("You want to Roll? (Y): ")
            if is_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Your score for this turn is lost.")
                players_scores[player_idx]+=current_score
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)
                print("Your score is:", current_score)

        
        print(f"\nYour turn has ended. Your total score is now: {players_scores[player_idx]}")     
            
    
winner_score = max(players_scores)
winner_index = players_scores.index(winner_score)
print("Player Number", winner_index+1, "is the winner with a score of:", winner_score)