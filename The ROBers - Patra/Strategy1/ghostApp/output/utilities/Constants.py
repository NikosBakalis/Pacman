#!/usr/bin/python2
# -*- coding: utf-8 -*-

from enum import Enum

class ImportanceType(Enum):

	LOW = 1
	NORMAL = 2
	HIGH = 4

class OperatorType(Enum):

	EQUAL = 0
	NOT_EQUAL = 1
	GREATER = 2
	GREATER_OR_EQUAL = 3
	LOWER = 4
	LOWER_OR_EQUAL = 5

class BooleanEvaluationType(Enum):

	AND = 0
	OR = 1
	XOR = 2
	NOT = 3

class PlayerType(Enum):

	PACMAN = 0
	GHOST = 1

class OpponentDistanceType(Enum):

	MAX = 0
	MIN = 1

class BonusDistanceType(Enum):

	TO_CLOSEST_BONUS = 1
	TO_HIGH_BONUS_AREA = 2

class CardDistanceType(Enum):

	TO_CLOSEST_POINTS = 1
	TO_HIGH_SCORE_AREA = 2
	TO_MOST_POINTS = 4

class GameVariableType(Enum):

	TIME = 0
	MY_POINTS = 1
	OPP_POINTS = 2
	MY_BONUS = 3
	OPP_BONUS = 4
	UNTAKEN_POINT_CARDS = 5
	UNTAKEN_POINTS = 6
	UNTAKEN_BONUS = 7
	DIST_TO_OPP = 8
	DIST_TO_CLOSEST_POINTS = 9
	DIST_TO_CLOSEST_BONUS = 10
	DIST_TO_MOST_POINTS = 11
	UNTAKEN_BONUS_CARDS = 12

class RobotStateType(Enum):

	INITIAL = 0
	INTERNAL = 1
	FINAL = 2

class ScoreMultiplicationOptions(Enum):

	DOUBLE_POINTS = 2 #2 bonuses required to double the points
	TRIPLE_POINTS = 3 #3 bonuses required to triple the points
	QUADRUPLE_POINTS = 4 #4 bonuses required to multiply the points by 4
	QUINTUPLE_POINTS = 5 #5 bonuses required to multiply the points by 5


class ImmobilizationOptions(Enum):

	FIVE_SECONDS = 1 #1 bonus required to immobilize the opponent for 5 seconds
	TEN_SECONDS = 2 #2 bonuses required to immobilize the opponent for 10 seconds
	FIFTEEN_SECONDS = 3 #3 bonuses required to immobilize the opponent for 15 seconds
	TWENTY_SECONDS = 4 #4 bonuses required to immobilize the opponent for 20 seconds
	TWENTY_FIVE_SECONDS = 5 #5 bonuses required to immobilize the opponent for 25 seconds

