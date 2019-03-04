#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

sys.path.append('base')
sys.path.append('utilities')

from BehaviorBase import BehaviorBase
from Constants import *

class EscapeRoutesBehavior(BehaviorBase):

	def __init__(self):
		BehaviorBase.__init__(self)

	def setParameters(self, importance, searchDepth, playerType):
		self.importance = importance
		self.searchDepth = searchDepth
		self.playerType = playerType

	def getCallType(self):
		return 'escape_routes'
