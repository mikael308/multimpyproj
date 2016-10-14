import sys, os
path = os.getcwd()
sys.path.append(path)
from src.buffer import Buffer
from testcase import TestCase
import tools as tools
from src.game.gameobjects.player import Player
from random import randint


class TestBuffer(TestCase):
    """
    Test the gameobject: buffer\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def __init__(self):
        TestCase.__init__(self, "buffer")

    def _run(self):

		for j in range(0, 3):
			for i in range(1, 500):
				buf = Buffer(i)
				self._test_add(buf)
				self._test_delete(buf)

    @staticmethod
    def _test_add(buf):
    	cap = buf.get_capacity()
    	tools.assertEquals(buf.get_size(), 0, "buf add size START incr")
    	tools.assertTrue(buf.is_empty(), "buf is empty at start")
    	for i in range(1, cap+1):
    		elem = randint(0, i * 10000)
    		tools.assertTrue(buf.add(elem), "buf add element ,adding elem [" + str(elem) + "] to capacity {" + str(buf.get_size()) + "/"+str(buf.get_capacity()) + "}")
    		tools.assertEquals(buf.get_size(), i, "buf add size incr")

    	tools.assertTrue(buf.is_full(), "buf is full after adding")

    	for i in range(1, cap+1):
    		tools.assertFalse(buf.add(randint(0, 1000)), "add to full buf")
    		tools.assertEquals(buf.get_size(), cap, "buf size is capacity after adding cap amount of elements")
    
    @staticmethod
    def _test_delete(buf):
    	tools.assertTrue(buf.clear())
    	tools.assertTrue(buf.is_empty(), "buf is empty after clear")

    	for i in range(1, randint(2, 2+buf.get_capacity())):
    		buf.add(randint(0, i*40))

    	for i in range(0, buf.get_capacity()):
    		buf.deleteAt(i)
    	tools.assertTrue(buf.is_empty(), "buf empty after deleteAt")

