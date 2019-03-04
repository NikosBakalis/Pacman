#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

sys.path.append('base')
sys.path.append('utilities')

from RobotStateBase import RobotStateBase
from Constants import *

class CardAcquisition(RobotStateBase):

	def __init__(self, playerType, orchRpcAPI):
		RobotStateBase.__init__(self, playerType, orchRpcAPI)

	def createResponseMessage(self):
		return{
			'player_id': self.playerType.value,
			'calls': self.calls,
			'depth': self.escapeRouteSearchDepth,
			'strategy': 'avoid_opp_area',
			'strategy_area': 4,
			'state': 'CardAcquisition'
		}
