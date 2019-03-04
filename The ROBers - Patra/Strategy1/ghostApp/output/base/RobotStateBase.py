#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import abc

sys.path.append('logic')

from Transition import Transition

sys.path.append('networking')
from orchestrator_rpc_clients import OrchestratorAPI

sys.path.append('robotBehaviors')
from EscapeRoutesBehavior import EscapeRoutesBehavior

class RobotStateBase:

	def __init__(self, playerType, orchRpcAPI):
		self.bPlayedOnce = False
		self.playerType = playerType
		self.orchRpcAPI = orchRpcAPI

	def setTransitions(self, transitions):
		self.transitions = transitions

	def setBehaviors(self, behaviors):
		self.behaviors = behaviors

	def execute(self):
		self.bPlayedOnce = True

		#create calls dictionary
		self.createCallsDictionary()

		#initialize escape routes depth
		self.setEscapeRouteSearchDepth()

		#create response message
		responseMessage = self.createResponseMessage()
		return responseMessage

	def setEscapeRouteSearchDepth(self):
		self.escapeRouteSearchDepth = 0

		for behavior in self.behaviors:
			if isinstance(behavior, EscapeRoutesBehavior):
				self.escapeRouteSearchDepth = behavior.searchDepth

	def createCallsDictionary(self):
		self.calls = {}

		for behavior in self.behaviors:
			self.calls[behavior.getCallType()] = behavior.getImportance()

	@abc.abstractmethod
	def createResponseMessage(self):
		pass

	def checkForEligibleTransition(self):
		for transition in self.transitions:
			if transition.isEligible() == True:
				self.eligibleTransition = transition
				return True

		return False

	def everExecuted(self):
		return self.bPlayedOnce

	def setEverExecuted(self, bEverExecuted):
		self.bPlayedOnce = bEverExecuted 		

	def getNextEligibleTransition(self):
		return self.eligibleTransition.getNextState()
