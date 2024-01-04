from game.play import MOVES, get_moves, get_players, play_rounds


def test_moves():
    assert MOVES == ("rock", "paper", "scissors")


def test_len_get_moves():
    assert len(get_moves()) == 3


def test_len_get_players():
    assert len(get_players()) == 2


def test_play_round_draw():
    matches = (["rock", "scissors", "paper"], ["scissors", "rock", "paper"])
    expected_result = {"player_1": 1, "player_2": 1}
    assert play_rounds(matches) == expected_result


def test_play_round_equal_draw():
    matches = (["rock", "scissors", "paper"], ["rock", "scissors", "paper"])
    expected_result = {"player_1": 0, "player_2": 0}
    assert play_rounds(matches) == expected_result


def test_play_round_player_1_win():
    matches = (["rock", "paper", "scissors"], ["scissors", "rock", "paper"])
    expected_result = {"player_1": 3, "player_2": 0}
    assert play_rounds(matches) == expected_result


def test_play_round_player_2_win():
    matches = (["scissors", "rock", "paper"], ["rock", "paper", "scissors"])
    expected_result = {"player_1": 0, "player_2": 3}
    assert play_rounds(matches) == expected_result
