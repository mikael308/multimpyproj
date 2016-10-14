import sys
import os
from timer import Timer

sys.path.append(os.getcwd())


class TestCase:
	"""
	Testcase used in testsuite\n
	to implement testcase\n
	define everything needed to be tested in function _run(self)\n
	use module test.tools to assert values\n
	\n
	to run testcase: see function run_test(self)\n

	:author: Mikael Holmbom
	:version: 1.0
	"""

	# the name of this testcase
	__name = ""

	def __init__(self, name):
		self.__name = name

	def _run(self):
		"""
		defines all testing for this testcase\n
		"""
		raise NotImplementedError("test not implemented")

	def run_test(self, print_elapse_time=False):
		"""
		run this testcase\n
		prints out the result\n
		"""
		if print_elapse_time:
			timer = Timer()
		try:
			if print_elapse_time:
				timer.start()
			self._run()
			if print_elapse_time:
				timer.stop()
			TestCase._print_success("+ ["+self.__name +"] test PASSED")

		except Exception as e:
			s = "- ["+self.__name +"] test FAILED"
			s = s+ e.message
			TestCase._print_fail(s)
		if print_elapse_time:
			print "test " + str(self.__name) + " duration " + Timer.secondsToStr(timer.get_elapsed()) + "s"
			
	@staticmethod
	def _print_fail(message):
		print('\x1b[6;30;41m' + message + '\x1b[0m')

	@staticmethod
	def _print_success(message):
		print('\x1b[6;30;42m' + message + '\x1b[0m')