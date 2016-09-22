"""

functions to help make tests in testcase modules\n

:author: Mikael Holmbom
:version: 1.0
"""
import traceback


def assertTrue(test_val, testtag=""):
	"""
	test the assertion: value is True
	if this assertion is False a exception is raised\n
	:param test_val: value to test\n
	:param testtag: tag used for exception message\n
	"""
	if not test_val:
		raise Exception("["+ str(testtag) + "]: test not passed : { " +  str(test_val) + " is not True }")


def assertFalse(test_val, testtag=""):
	"""
	test the assertion: value is False\n
	if this assertion is False a exception is raised\n
	:param test_val: the value to test\n
	:param testtag: tag used for exception message\n
	"""
	if test_val:
		raise Exception("["+ str(testtag) + "]: test not passed : { " +  str(test_val) + " is not False }")


def assertEquals(a, b, testtag=""):
	"""
	test the assertion: a equals b\n
	if this assertion is False a exception is raised\n
	:param a: value 1
	:param b: value 2
	:param testtag: tag used for exception message\n
	"""
	if a != b:
		raise Exception("["+ str(testtag) + "]: test not passed : { " +  str(a) + " != "+str(b)+" }")