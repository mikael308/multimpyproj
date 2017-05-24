
from testcase import TestCase
import tools as tools
from src.game.gameobjects.player import Player

class TestPlayer(TestCase):
    """
    Test the gameobject: player\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def _run(self):
        player = Player()
        TestPlayer._test_health(player)
        
    @staticmethod
    def _test_health(player):
        player.set_health(10)
        tools.assertEquals(player.get_health(), 10, "playerhealth")

        player.mod_health(3)
        tools.assertTrue(player.get_health() == 13, "mod playerhealth")

        tools.assertTrue(player.is_alive())
        tmp_health = player.get_health()
        for i in range(0, 20):
            player.mod_health(-1)
            tools.assertEquals(player.get_health(), (tmp_health - (i+1)), "decrease playerhealth")

        tools.assertTrue(player.get_health() == (13-20))
        tools.assertTrue(not player.is_alive(), "player not alive is True")
        tools.assertFalse(player.is_alive(), "player alive is False")
        tools.assertTrue(player.is_alive(), "player is alive") # will fail, used to demonstrate failed test


