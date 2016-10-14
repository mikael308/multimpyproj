from test_player import TestPlayer
from test_tools import TestTools
from test_buffer import TestBuffer
from timer import Timer

def run_testcases(testcases, timer=None):
	"""
	run list of testcases
	:param testcases: list of testcases
	:param timer: a timer, if included will take interval between every test
	"""
	for testcase in testcases:
		testcase.run_test(True)
		if timer != None:
			timer.interval()
		print "  "


# included testcases in this test
testcases = [
	TestPlayer(),
	TestTools(),
	TestBuffer()]


timer = Timer()
print "________ start test all testcases"
import tools

timer.start()
run_testcases(testcases)
timer.stop()
print "________ finished test all testcases"

print "total duration: " + Timer.secondsToStr(timer.get_startstop_diff())