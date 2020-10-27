#######################################################################
# Copyright (C)                                                       #
# 2016 - 2018 Shangtong Zhang(zhangshangtong.cpp@gmail.com)           #
# 2016 Jan Hakenberg(jan.hakenberg@gmail.com)                         #
# 2016 Tian Jun(tianjun.cpp@gmail.com)                                #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################


#adjust tic_tac_toe_config.py

import tic_tac_toe_Judger as JudgerMod
import tic_tac_toe_Player as PlayerMod 
import tic_tac_toe_HumanPlayer as HumanPlayerMod


def train(epochs, print_every_n=200):
    player1 = PlayerMod.Player(epsilon=0.1)
    player2 = PlayerMod.Player(epsilon=0.1)
    judger = JudgerMod.Judger(player1, player2)
    player1_win = 0.0
    player2_win = 0.0
    for i in range(1, epochs + 1):
        winner = judger.play(print_state=False)
        if winner == 1:
            player1_win += 1
        if winner == -1:
            player2_win += 1
        if i % print_every_n == 0:
            print('Epoch %d, player 1 winrate: %.02f, player 2 winrate: %.02f' % (i, player1_win / i, player2_win / i))
        player1.backup()
        player2.backup()
        judger.reset()
    player1.save_policy()
    player2.save_policy()


def compete(turns):
    player1 = PlayerMod.Player(epsilon=0)
    player2 = PlayerMod.Player(epsilon=0)
    judger = JudgerMod.Judger(player1, player2)
    player1.load_policy()
    player2.load_policy()
    player1_win = 0.0
    player2_win = 0.0
    for _ in range(turns):
        winner = judger.play()
        if winner == 1:
            player1_win += 1
        if winner == -1:
            player2_win += 1
        judger.reset()
    print('%d turns, player 1 win %.02f, player 2 win %.02f' % (turns, player1_win / turns, player2_win / turns))

# The game is a zero sum game. If both players are playing with an optimal strategy, every game will end in a tie.
# So we test whether the AI can guarantee at least a tie if it goes second.

# human interface
# input a number to put a chessman
# | q | w | e |
# | a | s | d |
# | z | x | c |

def play():
    while True:
        player1 = HumanPlayerMod.HumanPlayer()
        player2 = PlayerMod.Player(epsilon=0.5)
        judger = JudgerMod.Judger(player1, player2)
        player2.load_policy()
        winner = judger.play()
        if winner == player2.symbol:
            print("You lose!")
        elif winner == player1.symbol:
            print("You win!")
        else:
            print("It is a tie!")


if __name__ == '__main__':
    train(epochs=int(3e4))
    compete(int(1e3))
    play()

