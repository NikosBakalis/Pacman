#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

sys.path.append('base')
sys.path.append('utilities')

from RobotStateBase import RobotStateBase
from Constants import *

class BonusAcquisition(RobotStateBase):

	def __init__(self, playerType, orchRpcAPI):
		RobotStateBase.__init__(self, playerType, orchRpcAPI)
		self.bPlayedOnce = True

	def createResponseMessage(self):
		return{
			'player_id': self.playerType.value,
			'calls': self.calls,
			'depth': self.escapeRouteSearchDepth,
			'strategy': 'avoid_opp_area',
			'strategy_area': 4,
			'state': 'BonusAcquisition'
		}
