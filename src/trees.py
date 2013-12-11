from sys import argv
from states import States
from random import randint
from player import Player
from enemies import Enemies
from config import *

# this function gets the most hurt enemy, if all of the enemies are at full hp then returns nonw
def getWorstHurt(allEnemies):
	worstHurt = None
	minHP = 100000000000.0 # start with an obnoxiously large num
	for x in allEnemies.getAllEnemies():
		if float(x.currentHP) / x.hitPoints < minHP:
			minHP = x.currentHP / x.hitPoints
			worstHurt = x # filter by lowest hp
	if minHP == 1.0: # if all are at full hp
		return None
	else: # otherwise get worrst hurt
		return worstHurt

# buff an ally! rreturns all allies that can be buffed
def BuffAlly(allEnemies):
	for x in allEnemies.getAllEnemies():
		if x.enemyType != 'Dark Elf Cleric' and x.enemyType != 'Dark Elf Wizard': # DEC and DEW cannot be buffed
			return x

class OrcFighterTree: # tree to decribe HOF and LOF actions (see figure 1)
	action = ''
	def __init__(self,of,thePlayer,enemyTeamState):
		if enemyTeamState == 'Regroup!':
			self.action = 'Defend'
		elif enemyTeamState == 'Attack!':
			if of.currentHP < (FIGHTER_HEAL_THRESHHOLD * of.hitPoints) and  of.status != 'Defending':
				self.action = 'Defend'
			else:
				self.action = 'Attack'

class ArcherTree: # tree to decribe DEA actions (see figure 2)
	action = ''
	def __init__(self,of,thePlayer,enemyTeamState):
		if enemyTeamState == 'Regroup!':
			self.action = 'Defend'
		elif enemyTeamState == 'Attack!':
			if of.currentHP < (ARCHER_HEAL_THRESHOLD * of.hitPoints) and  of.status != 'Defending':
				self.action = 'Defend'
			else:
				self.action = 'Attack'

class WizardTree: # tree to decribe DEW actions (see figure 3)
	action = ''
	def __init__(self,wizard,allEnemies,thePlayer,enemyTeamState):
		if enemyTeamState == 'Regroup!':
			self.action = ['Defend',None]
		elif enemyTeamState == 'Attack!':
			if wizard.currentMP >= FIREBALL_COST: #
				self.action = ['FireBall',None]
			elif wizard.currentMP >= ATTACK_BUFF_COST and randint(1,100) <= BUFF_PROC:
				self.action = ['AttackBuff',BuffAlly(allEnemies)]
			else:
				if wizard.currentHP < (0.70 * wizard.hitPoints):
					self.action = ['Defend',None]
				else:
					self.action = ['Attack',None]

class ClericTree: # tree to decribe DEC actions (see figure 4)
	action = ''
	def __init__(self,cleric,allEnemies,thePlayer,enemyTeamState):
		if enemyTeamState == 'Regroup!':
			self.action = ['Defend',None]
		elif enemyTeamState == 'Attack!':
			if cleric.currentMP >= HEALCOST:
				worstHurt = getWorstHurt(allEnemies)
				if worstHurt == None:
					self.action = ['Attack',None]
				else:
					if worstHurt.enemyId == cleric.enemyId:
						self.action = ['Defend',None]
					else:
						self.action = ['Heal', worstHurt]
			else:
				if cleric.currentHP < (0.70 * cleric.hitPoints):
					self.action = ['Defend',None]
				else:
					self.action = ['Attack',None]

if __name__ == "__main__": # cannot call directly
    print 'This file, ' + argv[0] + ', is only for import....'
    print 'to Play the game please run main.py:'
    print 'usage: python main.py'