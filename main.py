from game import Game
from menu import Menu
from board import Board





#"""
#easy
size = (15, 10)
prob = 0.15
screenSize = 400, 800
time = 100

#"""

"""
#medium

"""

"""
#hard

"""

menu = Menu(screenSize)
size, prob, screenSize, time = menu.run()
board = Board(size, prob)
game = Game(board, screenSize, time)
game.run()
