
from models.GameOfLife import GameOfLife
from models.patterns import *
from utils.pallets import palettes
game = GameOfLife(size=(30, 50), cell_size=20, pallet=palettes["neon"])
game.addPattern(beacon)
game.run()
