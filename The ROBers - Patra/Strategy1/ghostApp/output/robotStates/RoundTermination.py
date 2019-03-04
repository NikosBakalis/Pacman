#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

sys.path.append('base')
sys.path.append('utilities')

from RobotStateBase import RobotStateBase
from Constants import *

sys.path.append('networking')
from orchestrator_rpc_clients import OrchestratorAPI

class RoundTermination(RobotStateBase):

	def __init__(self, playerType, orchRpcAPI):
		RobotStateBase.__init__(self, playerType, orchRpcAPI)

	def createResponseMessage(self):
		return{
			'player_id': self.playerType.value,
			'bonus_type': 'win',
			'bonuses_number': 5
		}
