import sys
import tools
from test_player import TestPlayer
from test_tools import TestTools
from test_buffer import TestBuffer
from timer import Timer

class Settings:
	showTime=False
	showTotalTime=False

def run_testcases(testcases):
	"""
	run list of testcases
	:param testcases: list of testcases
	:param timer: a timer, if included will take interval between every test
	"""
	for testcase in testcases:
		testcase.run_test(Settings.showTime)
		print ""

def parseFlag(arg):
	"""
	parse arg flag for settings
	"""
	for c in arg:
		if c ==  "t":
			Settings.showTime=True
		elif c == "T":
			Settings.showTotalTime=True

def printHelp():
	"""
	print help for user
	"""
	print "Wrong input"
	print "usage: [-tT] testcase"
	print " flag t: show testcase time duration"
	print " flag T: show total time duration"
	print "ex: -t Player"



################################
# HANDLE INPUT

if(len(sys.argv) <2):
	printHelp()
	exit()

if sys.argv[1] == "--help":
	printHelp()
	exit()

# add testcases
testcases = []
for arg in sys.argv[1:]:
	if arg[0]=="-":
		parseFlag(arg[1:])
	else:
		testcases.append(eval("Test"+arg+"()"))

# if no testcases was added to suite
if not testcases:
	printHelp()
	exit()


################################
# RUN TESTS

print "________ start test all testcases"

timer=None
if Settings.showTotalTime:
	timer = Timer()
	timer.start()

run_testcases(testcases)

if Settings.showTotalTime:
	timer.stop()

print "________ finished test all testcases"

if Settings.showTotalTime:
	print "total duration: " + Timer.secondsToStr(timer.get_startstop_diff())
