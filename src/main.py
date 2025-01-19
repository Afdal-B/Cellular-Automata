
from models.GameOfLife import GameOfLife
from models.patterns import *
from utils.pallets import palettes
game = GameOfLife(size=(80, 140), cell_size=8, pallet=palettes["fire_and_ice"])
game.addPattern(pulsar)
game.run()
