from player import Player
from enemies import Enemies
from config import *

#HEALCOST = 35
#HEALAMOUNT = 0.20

def getWorstHurt(frontRow,backRow):
	worstHurt = None
	minHP = 100000000000.0
	for x in frontRow+backRow:
		#print str(x.enemyId) + ' ' + str(x.currentHP) + ' ' + str(x.hitPoints)
		if x.currentHP / x.hitPoints < minHP:
			minHP = x.currentHP / x.hitPoints
			worstHurt = x
	#print str(worstHurt.enemyId) + '============================'
	return worstHurt

class OrcFighterTree:
	action = ''
	def __init__(self,of,thePlayer):
		if of.currentHP < (0.7 * of.hitPoints) and  of.status != 'Defending':
			self.action = 'Defend'
		else:
			self.action = 'Attack'

class ArcherTree:
	action = ''
	def __init__(self,of,thePlayer):
		if of.currentHP < (0.75 * of.hitPoints) and  of.status != 'Defending':
			self.action = 'Defend'
		else:
			self.action = 'Attack'

class ClericTree:
	action = ''
	def __init__(self,cleric,frontRow,backRow,thePlayer):
		if cleric.currentMP >= HEALCOST:
			worstHurt = getWorstHurt(frontRow,backRow)
			if worstHurt.enemyId == cleric.enemyId:
				self.action = ['Defend',None]
			else:
				self.action = ['Heal', worstHurt]
		else:
			if cleric.currentHP < (0.70 * cleric.hitPoints):
				self.action = ['Defend',None]
			else:
				self.action = ['Attack',None]




