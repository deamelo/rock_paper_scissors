from main import Jogador, avaliar_jogada, POSSIBILIDADES


def test_possibilidades():
    assert POSSIBILIDADES == ("pedra", "papel", "tesoura")


def test_jogador():
    assert Jogador


def test_jogador_comeca_com_o_placar_zerado():
    jogador = Jogador()
    assert jogador.placar == 0


def test_jogador_comeca_sem_rodadas():
    jogador = Jogador()
    assert jogador.rodadas == None


def test_jogador_nova_rodada():
    jogador = Jogador()
    jogador.nova_rodada()
    assert len(jogador.rodadas) == 1
    assert jogador.rodadas[0] in POSSIBILIDADES


def test_jogador_nova_rodada_com_jogada():
    jogador = Jogador()
    jogador.nova_rodada("pedra")
    assert len(jogador.rodadas) == 1
    assert jogador.rodadas[0] == "pedra"


def test_jogador_avaliar_jogada_empate():
    jogador_1 = Jogador()
    jogador_2 = Jogador()
    jogador_1.nova_rodada("papel")
    jogador_2.nova_rodada("papel")
    avaliar_jogada(jogador_1, jogador_2)
    assert jogador_1.placar == 0
    assert jogador_2.placar == 0


def test_jogador_avaliar_jogada_vitoria_papel_vs_pedra():
    jogador_1 = Jogador()
    jogador_2 = Jogador()
    jogador_1.nova_rodada("papel")
    jogador_2.nova_rodada("pedra")
    avaliar_jogada(jogador_1, jogador_2)
    assert jogador_1.placar == 1
    assert jogador_2.placar == 0


def test_jogador_avaliar_jogada_vitoria_pedra_vs_tesoura():
    jogador_1 = Jogador()
    jogador_2 = Jogador()
    jogador_1.nova_rodada("tesoura")
    jogador_2.nova_rodada("pedra")
    avaliar_jogada(jogador_1, jogador_2)
    assert jogador_1.placar == 0
    assert jogador_2.placar == 1


def test_jogador_avaliar_jogada_vitoria_tesoura_vs_papel():
    jogador_1 = Jogador()
    jogador_2 = Jogador()
    jogador_1.nova_rodada("tesoura")
    jogador_2.nova_rodada("papel")
    avaliar_jogada(jogador_1, jogador_2)
    assert jogador_1.placar == 1
    assert jogador_2.placar == 0


def test_jogador_ganha_duas_rodadas():
    jogador_1 = Jogador()
    jogador_2 = Jogador()
    jogador_1.nova_rodada("tesoura")
    jogador_2.nova_rodada("pedra")
    avaliar_jogada(jogador_1, jogador_2)
    assert jogador_1.placar == 0
    assert jogador_2.placar == 1

    jogador_1.nova_rodada("pedra")
    jogador_2.nova_rodada("papel")
    avaliar_jogada(jogador_1, jogador_2)
    assert jogador_1.placar == 0
    assert jogador_2.placar == 2


def test_jogador_empata():
    jogador_1 = Jogador()
    jogador_2 = Jogador()
    jogador_1.nova_rodada("tesoura")
    jogador_2.nova_rodada("pedra")
    avaliar_jogada(jogador_1, jogador_2)
    assert jogador_1.placar == 0
    assert jogador_2.placar == 1

    jogador_1.nova_rodada("tesoura")
    jogador_2.nova_rodada("papel")
    avaliar_jogada(jogador_1, jogador_2)
    assert jogador_1.placar == 1
    assert jogador_2.placar == 1
