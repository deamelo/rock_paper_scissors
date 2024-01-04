from random import choice


PEDRA = "pedra"
PAPEL = "papel"
TESOURA = "tesoura"
POSSIBILIDADES = (PEDRA, PAPEL, TESOURA)


class Jogador:
    placar = 0
    rodadas = None

    def nova_rodada(self, jogada=None):
        if self.rodadas is None:
            self.rodadas = []

        if jogada is not None:
            self.rodadas.append(jogada)
        else:
            self.rodadas.append(self.sortear_jogada())

    @staticmethod
    def sortear_jogada():
        return choice(POSSIBILIDADES)


def avaliar_jogada(jogador_1: Jogador, jogador_2: Jogador) -> None:
    if jogador_1.rodadas[-1] == jogador_2.rodadas[-1]:
        return

    if jogador_1.rodadas[-1] == PEDRA and jogador_2.rodadas[-1] == TESOURA:
        jogador_1.placar += 1
        return

    if jogador_1.rodadas[-1] == PAPEL and jogador_2.rodadas[-1] == PEDRA:
        jogador_1.placar += 1
        return

    if jogador_1.rodadas[-1] == TESOURA and jogador_2.rodadas[-1] == PAPEL:
        jogador_1.placar += 1
        return

    jogador_2.placar += 1


def main():
    jogador_1 = Jogador()
    jogador_2 = Jogador()

    for i in range(1, 4):
        print(f"Rodada {i} -> ", end=" ")

        jogador_1.nova_rodada()
        jogador_2.nova_rodada()
        avaliar_jogada(jogador_1, jogador_2)

        print(f"Jogador 1: {jogador_1.rodadas[-1]} vs "
              f"Jogador 2: {jogador_2.rodadas[-1]}")

        print(f"Placar: {jogador_1.placar} x {jogador_2.placar}")

    print(f"\nPlacar final: [Jogador 1] {jogador_1.placar} x "
          f"{jogador_2.placar} [Jogador 2]")


if __name__ == "__main__":
    main()
