# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:01:14 2020

@author: Ramsis
"""
import tic_tac_toe_config as config

# human interface
# input a number to put a chessman
# | q | w | e |
# | a | s | d |
# | z | x | c |

class HumanPlayer:
    def __init__(self, **kwargs):
        self.symbol = None
        self.keys = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']
        self.state = None

    def reset(self):
        pass

    def set_state(self, state):
        self.state = state

    def set_symbol(self, symbol):
        self.symbol = symbol

    def act(self):
        self.state.print_state()
        key = input("Input your position:")
        data = self.keys.index(key)
        i = data // config.BOARD_COLS
        j = data % config.BOARD_COLS
        return i, j, self.symbol


