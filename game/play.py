import random

MOVES = ("rock", "paper", "scissors")


def get_moves() -> tuple:
    moves = []

    while len(moves) < 3:
        move = random.choice(MOVES)
        moves.append(move)

    print(moves)
    return moves


def get_player() -> tuple:
    player_1 = get_moves()
    player_2 = get_moves()

    return player_1, player_2


def play_round() -> str:
    player_1, player_2 = get_player()

    for pl_1, pl_2 in zip(player_1, player_2):
        if pl_1 == pl_2:
            return "draw"
        elif (
            (pl_1 == "rock" and pl_2 == "scissors")
            or (pl_1 == "paper" and pl_2 == "rock")
            or (pl_1 == "scissors" and pl_2 == "paper")
        ):
            return "player_1"

    print("player_1", player_1)
    print("player_2", player_2)

    return "player_2"


def win_game() -> str:
    score_pl_1 = 0
    score_pl_2 = 0

    winner = play_round()

    if winner == "player_1":
        score_pl_1 += 1
    elif winner == "player_2":
        score_pl_2 += 1

    if score_pl_1 > score_pl_2:
        return f"Player_1 WIN -> Player_1: {score_pl_1} x Player_2: {score_pl_2}"
    elif score_pl_1 < score_pl_2:
        return f"Player_2 WIN -> Player_2: {score_pl_2} x Player_1: {score_pl_1}"
    return "No winner"
