#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

sys.path.append('utilities')
from Constants import BooleanEvaluationType, PlayerType

from Condition import Condition

class ConditionGroup:

	def __init__(self, evaluationType, playerType):
		self.evaluationType = evaluationType
		self.playerType = playerType
		self.conditions = None
		self.conditionGroups = None

	def setConditions(self, conditions):
		self.conditions = conditions

	def setConditionGroups(self, conditionGroups):
		self.conditionGroups = conditionGroups

	def evaluate(self):
		
		if self.evaluationType == BooleanEvaluationType.AND:
			return self.booleanAndEvaluation()
		elif self.evaluationType == BooleanEvaluationType.OR:
			return self.booleanOrEvaluation()
		elif self.evaluationType == BooleanEvaluationType.XOR:
			return self.booleanXorEvaluation()
		else: #It is a Boolean NOT
			return self.booleanNotEvaluation()

	def booleanAndEvaluation(self):

		evaluationResult = True

		if self.conditions != None:
			for condition in self.conditions:
				evaluationResult = evaluationResult and condition.evaluate()
				if evaluationResult == False:
					return False

		if self.conditionGroups != None:
			for conditionGroup in self.conditionGroups:
				evaluationResult = evaluationResult and conditionGroup.evaluate()
				if evaluationResult == False:
					return False

		return evaluationResult

	def booleanOrEvaluation(self):

		evaluationResult = False

		if self.conditions != None:
			for condition in self.conditions:
				evaluationResult = evaluationResult or condition.evaluate()
				if evaluationResult == True:
					return True

		if self.conditionGroups != None:
			for conditionGroup in self.conditionGroups:
				evaluationResult = evaluationResult or conditionGroup.evaluate()
				if evaluationResult == True:
					return True

		return evaluationResult

	def booleanXorEvaluation(self):
		if self.conditions == None: #then the XOR is between two groups
			return self.conditionGroups[0].evaluate() != self.conditionGroups[1].evaluate()
		elif self.conditionGroups == None: #then the XOR is between two conditions
			return self.conditions[0].evaluate() != self.conditions[1].evaluate()
		else: #then the XOR is between one condition and one condition group
			return self.conditionGroups[0].evaluate() != self.conditions[1].evaluate()

	def booleanNotEvaluation(self):
		if self.conditions <> None:
			return not self.conditions[0].evaluate()
		else: #the group comprises only of one other group
			return not self.conditionGroups[0].evaluate()
