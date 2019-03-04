#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

sys.path.append('utilities')
from Constants import OperatorType, PlayerType
from Constants import GameVariableType

sys.path.append('networking')
from orchestrator_rpc_clients import OrchestratorAPI

sys.path.append('datatype')
from GameVariable import GameVariable

class Condition:

	def __init__(self, operator, playerType, orchRpcAPI):
		self.operator = operator
		self.playerType = playerType
		self.orchRpcAPI = orchRpcAPI

		if self.playerType == PlayerType.PACMAN:
			self.opponentType = PlayerType.GHOST
		else:
			self.opponentType = PlayerType.PACMAN

	def evaluate(self):
		#refresh the operands values if needed
		self.evaluateOperands()

		if self.operator == OperatorType.EQUAL:
			return self.leftOpValue == self.rightOpValue
		elif self.operator == OperatorType.NOT_EQUAL:
			return self.leftOpValue != self.rightOpValue
		elif self.operator == OperatorType.GREATER:
			return self.leftOpValue > self.rightOpValue
		elif self.operator == OperatorType.GREATER_OR_EQUAL:
			return self.leftOpValue >= self.rightOpValue
		elif self.operator == OperatorType.LOWER:
			return self.leftOpValue < self.rightOpValue
		else: #it is lower or equal (<=) operator
			return self.leftOpValue <= self.rightOpValue

	def setOperands(self, leftOp, rightOp):
		self.leftOp = leftOp
		self.rightOp = rightOp

	def evaluateOperands(self):
		if isinstance(self.leftOp, GameVariable):
			self.leftOpValue = self.evaluateOperand(self.leftOp)
			print '>> (', self.leftOp.type, ')', self.leftOpValue,
		else:
			self.leftOpValue = self.leftOp
			print '>> ', self.leftOpValue,

		print self.operator,

		if isinstance(self.rightOp, GameVariable):
			self.rightOpValue = self.evaluateOperand(self.rightOp)
			print self.rightOpValue, '(', self.rightOp.type, ')'
		else:
			self.rightOpValue = self.rightOp
			print self.rightOpValue

	def evaluateOperand(self, operand):

		if operand.type == GameVariableType.TIME:
			return self.orchRpcAPI.remaining_time()
		elif operand.type == GameVariableType.MY_POINTS:
			return self.orchRpcAPI.player_score(self.playerType.value)
		elif operand.type == GameVariableType.OPP_POINTS:
			return self.orchRpcAPI.player_score(self.opponentType.value)
		elif operand.type == GameVariableType.MY_BONUS:
			return self.orchRpcAPI.available_player_bonus(self.playerType.value)
		elif operand.type == GameVariableType.UNTAKEN_POINT_CARDS:
			return self.orchRpcAPI.uncaptured_cards()
		elif operand.type == GameVariableType.UNTAKEN_POINTS:
			return self.orchRpcAPI.uncaptured_cards_points()
		elif operand.type == GameVariableType.UNTAKEN_BONUS:
			return self.orchRpcAPI.uncaptured_bonuses()
		elif operand.type == GameVariableType.UNTAKEN_BONUS_CARDS:
			return self.orchRpcAPI.uncaptured_bonuses()
		elif operand.type == GameVariableType.DIST_TO_OPP:
			return self.orchRpcAPI.distance_from_opponent()
		elif operand.type == GameVariableType.DIST_TO_CLOSEST_POINTS:
			return self.orchRpcAPI.distance_from_closest_card(self.playerType.value)
		elif operand.type == GameVariableType.DIST_TO_CLOSEST_BONUS:
			return self.orchRpcAPI.distance_from_closest_bonus(self.playerType.value)
		elif operand.type == GameVariableType.DIST_TO_MOST_POINTS:
			return self.orchRpcAPI.distance_from_highest_card(self.playerType.value)
		else: #it is opponent bonus type
			return self.orchRpcAPI.available_player_bonus(self.opponentType.value)
