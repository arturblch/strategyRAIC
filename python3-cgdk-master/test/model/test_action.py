import pytest
from model.Action import Action

from pysc2.lib.actions import FUNCTIONS, _Functions

class _Command:
    def __init__(self, function):
        self.function = function

class TestAction:
    def test_equal(self):
        act1 = Action()
        act2 = Action()
        act3 = Action()
        
        act1.addCommand(FUNCTIONS.select_point("select", [1, 2]))
        act2.addCommand(FUNCTIONS.Train_SCV_quick("now"))
        act3.addCommand(FUNCTIONS.select_point("select", [3, 4]))

        assert act1 != act2
        assert act1 == act3

    
    @pytest.mark.parametrize("test_com, expected_id", [
        ("Command_1", None),
        (FUNCTIONS.Train_SCV_quick("now"), 490),
    ])
    def test_add_command(self, test_com, expected_id):
        act = Action()

        act.addCommand(test_com)

        assert act.commands == [test_com]
        assert act.ids == [expected_id]

    def test_reset(self):
        act = Action()

        act.addCommand("Command_1")
        act.addCommand("Command_2")

        assert act.next() == "Command_1"
        assert act.next() == "Command_2"

        act.reset()
        assert act.next() == "Command_1"

    def test_repr(self):
        act = Action("abc")
        act.addCommand(FUNCTIONS.select_point("select", [1, 2]))

        assert act.__repr__() == "Action<group=abc, ids={}>".format([_Functions['select_point']])
