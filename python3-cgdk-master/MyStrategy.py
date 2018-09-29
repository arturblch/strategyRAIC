from model.ActionType import ActionType
from model.Game import Game
from model.Move import Move
from model.Player import Player
from model.World import World

from lib.ActionManager import ActionManager
from lib.Controler import Controler


class MyStrategy:
    def __init__(self):
        self.me = None
        self.world = None
        self.game = None

        self.actionMgr = ActionManager()
        self.ctrl = Controler(self)


    def move(self, me: Player, world: World, game: Game, move: Move):
        if world.tick_index == 0:
            move.action = ActionType.CLEAR_AND_SELECT
            move.right = world.width
            move.bottom = world.height

        if world.tick_index == 1:
            move.action = ActionType.MOVE
            move.x = world.width / 2.0
            move.y = world.height / 2.0
