def play_game(best_of = 1):
    wins = []
    for i in range(best_of):
        wins.append(play_single_game())
        if wins.count(1) > (best_of // 2):
            print("Player 1 wins this best of " + str(best_of) + " match!")
            return 1
        elif wins.count(2) > (best_of // 2):
            print("Player 2 wins this best of " + str(best_of) + " match!")
            return 2

def prompt_for_input():
    return input("Rock, paper, or scissors?\n")

def play_single_game():
    player1 = prompt_for_input()
    player2 = prompt_for_input()

    win_dict = {"rock": {"rock": 0, "paper": 1, "scissors": 2}, "paper": {"rock": 2, "paper": 0, "scissors": 1},
                                                                                   "scissors": {"rock": 1, "paper": 2, "scissors": 0}}
    winner = win_dict[player1][player2]
    if winner == 0:
        winner = play_single_game()
    print("Player " + str(winner) + " wins this game!")
    return winner