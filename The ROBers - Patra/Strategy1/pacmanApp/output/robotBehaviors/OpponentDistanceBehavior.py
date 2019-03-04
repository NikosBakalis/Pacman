#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

sys.path.append('base')
sys.path.append('utilities')

from BehaviorBase import BehaviorBase
from Constants import *

class OpponentDistanceBehavior(BehaviorBase):

	def __init__(self):
		BehaviorBase.__init__(self)

	def setParameters(self, importance, type, playerType):
		self.importance = importance
		self.type = type
		self.playerType = playerType

	def getCallType(self):

		if self.type == OpponentDistanceType.MAX:
			return 'max_distance_from_opponent'

		elif self.type == OpponentDistanceType.MIN:
			return 'min_distance_from_opponent'

