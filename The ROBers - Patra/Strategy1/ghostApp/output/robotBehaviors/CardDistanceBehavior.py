#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

sys.path.append('base')
sys.path.append('utilities')

from BehaviorBase import BehaviorBase
from Constants import *


class CardDistanceBehavior(BehaviorBase):

	def __init__(self):
		BehaviorBase.__init__(self)

	def setParameters(self, importance, type, playerType):
		self.importance = importance
		self.type = type
		self.playerType = playerType

	def getCallType(self):

		if self.type == CardDistanceType.TO_CLOSEST_POINTS:
			return 'min_distance_from_closest_card'

		elif self.type == CardDistanceType.TO_HIGH_SCORE_AREA:
			return 'min_weighted_distance_from_cards'

		elif self.type == CardDistanceType.TO_MOST_POINTS:
			return 'min_distance_from_highest_card'
