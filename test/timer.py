from time import clock
import math


class Timer:
	"""
	timer used for measure time durations in tests

	typical use-case:
		timer = Timer()
		timer.start()
		loop:
			# timeconsuming process
			timer.interval()

		timer.stop()
		# get results
		for i in timer.get_intervals():
			print Timer.secondsToStr(i)	
		print Timer.secondsToStr(timer.get_startstop_diff())

	:author: Mikael Holmbom
	:version: 1.0
	"""

	__start = None
	__stop = None
	__intervals = []

	def __init__(self):
		pass

	@staticmethod
	def __timestamp():
		"""
		get a timestamp
		"""
		return clock()

	def start(self):
		"""
		start this 
		:return: starttime
		"""
		self.__start = Timer.__timestamp()
		return self.get_start()

	def stop(self):
		"""
		stop this timer
		:return: stoptime
		"""
		self.__stop = Timer.__timestamp()
		return self.get_stop()

	def interval(self):
		"""
		make a interval stop
		:return: added interval
		"""
		i = Timer.__timestamp()
		self.__intervals.append(i)
		return i

	def get_start(self):
		"""
		get this starttime
		:return: starttime
		"""
		return self.__start

	def get_stop(self):
		"""
		get this stoptime
		:return: stoptime
		"""
		return self.__stop

	def is_running(self):
		"""
		determine if this timer is running
		:return: True if this timer is running
		"""
		return self.get_start() != None and self.get_stop() == None

	def is_started(self):
		"""
		determine if this timer has been started started
		:return: True if this timer is started
		"""
		return self.get_start() != None

	def is_stopped(self):
		"""
		determine if this timer is stopped
		:return: True if this timer is stopped
		"""
		return  self.get_start() != None

	def get_intervals(self):
		"""
		get this intervals
		:return: intervals as list
		"""
		return self.__intervals

	def reset(self):
		"""
		reset this timer timestamps
		:return: None
		"""
		self.__start = None
		self.__stop = None
		self.__intervals = None

	def get_startstop_diff(self):
		"""
		get the difference between start and stop\n
		if start or stop is not set: None is returned
		"""
		if self.get_start() == None or self.get_stop() == None:
			return None

		return self.get_stop() - self.get_start()

	def get_elapsed(self):
		"""
		get the elapsed time from start\n
		if start is not set: None is returned
		"""
		if self.get_start() == None:
			return None

		return Timer.__timestamp() - self.get_start()

	@staticmethod
	def secondsToStr(t):
		"""
		translates timestamp to string
		:return: time t as string
		"""
		h = math.floor(t / (60*60))
		m = math.floor(t / 60)
		s = math.floor(t % 60)
		ms = (t % 1.0) * 1000

		return "%02dh %02dm %02ds %dms" % (h, m, s, ms)
