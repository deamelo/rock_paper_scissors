# rock_paper_scissors

  Jogo PEDRA X PAPEL X TESOURA

## 🚀 Tecnologia

  Python 3.10.4 
  (https://www.python.org/)

## 🏁 Iniciando o projeto

  ***Tenha o python instalado em sua máquina e faça o clone do projeto***

    ```bash
        # Crie o python environment

            $ python -m venv .venv

        # Ative o environment

            $ source ./.venv/bin/activate

        # Para desativar a máquina virtual python (virtualenv):

            $ deactivate

        # Instale o pytest

            $ pip install pytest
    ```


## 📜 Regras

  - Dois jogadores se enfrentam -> 'player_1' e 'player_2'
  - Existem três opções de jogadas (MOVES) -> 'rock', 'paper', 'scissors'
  - As jogadas serão escolhidas de forma aleatória e podem ser repetidas ou não
  - Os jogadores terão três chances
  - Ganha o jogo quem ganhar mais jogadas, das três possíveis

## 🏆 Definição da partida

  - 'rock' empata com 'rock', ganha de 'scissors' e perde para 'paper'
  - 'paper' empata com 'paper', ganha de 'rock' e perde para 'scissors'
  - 'scissors' empata com 'scissors', ganha de 'paper' e perde para 'rock'

## 🕹️ Jogando

  ```bash
      # Para rodar o jogo

        $ python main.py
  ```

## 🚨 Testes
### **Rodando os Testes** ✅

  ```bash
      # Para rodar os testes unitários

        $ pytest -vv
  ```