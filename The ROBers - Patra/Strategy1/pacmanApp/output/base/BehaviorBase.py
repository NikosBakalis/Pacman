#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import abc

sys.path.append('base')

class BehaviorBase:

	def __init__(self):
		pass

	@abc.abstractmethod
	def setParameters(self):
		pass

	@abc.abstractmethod
	def getCallType(self):
		pass

	def getImportance(self):
		return self.importance.value
