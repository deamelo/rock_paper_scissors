import game


def main():
    game.get_moves()
    matches = game.get_player()
    game.play_round()
    result_game = game.win_game()

    print(f"Matches: {matches}")
    print(f"Game Result: {result_game}")


if __name__ == "__main__":
    main()
