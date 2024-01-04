import random

MOVES = ("rock", "paper", "scissors")


def get_moves() -> list:
    moves = []

    while len(moves) < 3:
        move = random.choice(MOVES)
        moves.append(move)

    return moves


def get_players() -> tuple[list]:
    player_1 = get_moves()
    player_2 = get_moves()

    return player_1, player_2


def play_rounds(matches) -> int:
    player_1, player_2 = matches

    result = {"player_1": 0, "player_2": 0}

    for pl_1, pl_2 in zip(player_1, player_2):
        if pl_1 == pl_2:
            continue

        if pl_1 == "rock" and pl_2 == "scissors":
            result["player_1"] += 1
            continue
        if pl_1 == "paper" and pl_2 == "rock":
            result["player_1"] += 1
            continue
        if pl_1 == "scissors" and pl_2 == "paper":
            result["player_1"] += 1
            continue
        result["player_2"] += 1

    return result
