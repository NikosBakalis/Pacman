#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

from Condition import Condition
from ConditionGroup import ConditionGroup

sys.path.append('robotStates')
sys.path.append('utilities')

from Constants import *

class Transition:

	def __init__(self, nextState) :
		self.condition = None
		self.conditionGroup = None
		self.nextState = nextState

	def isEligible(self):

		from EnemyImmobilization import EnemyImmobilization
		from RoundTermination import RoundTermination
		from ScoreMultiplication import ScoreMultiplication

		evaluationResult = True

		if isinstance(self.nextState, EnemyImmobilization):
			evaluationResult = self.checkEligibility(self.nextState.multiplier.value)
		elif isinstance(self.nextState, RoundTermination):
			evaluationResult = self.checkEligibility(6)
		elif isinstance(self.nextState, ScoreMultiplication):
			evaluationResult = self.checkEligibility(self.nextState.multiplier.value)

		if evaluationResult == False:
			return False

		if self.condition != None:
			return self.condition.evaluate()
		elif self.conditionGroup != None:
			return self.conditionGroup.evaluate()
		else: # the transition has no conditions
			return True

	def getNextState(self):
		return self.nextState

	def setConditionGroup(self, group):
		self.conditionGroup = group

	def setCondition(self, condition):
		self.condition = condition 

	def getPlayerBonus(self):
		return self.nextState.orchRpcAPI.available_player_bonus(self.nextState.playerType.value)

	def checkEligibility(self, bonusThreshold):
		if self.getPlayerBonus() >= bonusThreshold:
			return True
		else:
			return False

