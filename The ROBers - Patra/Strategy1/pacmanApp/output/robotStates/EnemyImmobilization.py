#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

sys.path.append('base')
sys.path.append('utilities')

from RobotStateBase import RobotStateBase
from Constants import *

sys.path.append('networking')
from orchestrator_rpc_clients import OrchestratorAPI

class EnemyImmobilization(RobotStateBase):

	def __init__(self, playerType, multiplier, orchRpcAPI):
		RobotStateBase.__init__(self, playerType, orchRpcAPI)
		self.multiplier = multiplier

	def createResponseMessage(self):
		return{
			'player_id': self.playerType.value,
			'bonus_type': 'immobilization',
			'bonuses_number': self.multiplier.value
		}
