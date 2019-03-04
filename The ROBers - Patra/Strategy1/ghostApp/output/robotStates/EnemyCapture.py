#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

sys.path.append('base')
sys.path.append('utilities')

from RobotStateBase import RobotStateBase
from Constants import *

class EnemyCapture(RobotStateBase):

	def __init__(self, playerType, orchRpcAPI):
		RobotStateBase.__init__(self, playerType, orchRpcAPI)

	def createResponseMessage(self):
		return{
			'player_id': self.playerType.value,
			'calls': {'min_distance_from_opponent':1},
			'depth': self.escapeRouteSearchDepth,
			'strategy':'optimal',
			'strategy_area': 4,
			'state': 'EnemyCapture'
		}
