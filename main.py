from game import play


def main():
    matches = play.get_players()
    result = play.play_rounds(matches)
    pl_1 = result["player_1"]
    pl_2 = result["player_2"]

    print(f"Matches: {matches}")
    if pl_1 > pl_2:
        print(f"PLAYER 1 WIN -> Player_1: {pl_1} x Player_2: {pl_2}")
    elif pl_1 < pl_2:
        print(f"PLAYER 2 WIN -> Player_2: {pl_2} x Player_1: {pl_1}")
    else:
        print("No winner")


if __name__ == "__main__":
    main()
