#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

sys.path.append('base')
sys.path.append('utilities')

from BehaviorBase import BehaviorBase
from Constants import *

class BonusDistanceBehavior(BehaviorBase):

	def __init__(self):
		BehaviorBase.__init__(self)

	def setParameters(self, importance, type, playerType):
		self.importance = importance
		self.type = type
		self.playerType = playerType

	def getCallType(self):

		if self.type == BonusDistanceType.TO_CLOSEST_BONUS:
			return 'min_distance_from_closest_bonus'

		elif self.type == BonusDistanceType.TO_HIGH_BONUS_AREA:
			return 'min_weighted_distance_from_bonuses'
