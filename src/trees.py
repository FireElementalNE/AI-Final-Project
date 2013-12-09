from states import States
from random import randint
from player import Player
from enemies import Enemies
from config import *

def getWorstHurt(allEnemies):
	worstHurt = None
	minHP = 100000000000.0
	for x in allEnemies.getAllEnemies():
		if x.currentHP / x.hitPoints < minHP:
			minHP = x.currentHP / x.hitPoints
			worstHurt = x
	return worstHurt

def BuffAlly(allEnemies):
	for x in allEnemies.getAllEnemies():
		if x.enemyType != 'Dark Elf Cleric' and x.enemyType != 'Dark Elf Wizard':
			return x

class OrcFighterTree:
	action = ''
	def __init__(self,of,thePlayer,enemyTeamState):
		if enemyTeamState == 'Regroup!':
			self.action = 'Defend'
		elif enemyTeamState == 'Attack!':
			if of.currentHP < (FIGHTER_HEAL_THRESHHOLD * of.hitPoints) and  of.status != 'Defending':
				self.action = 'Defend'
			else:
				self.action = 'Attack'

class ArcherTree:
	action = ''
	def __init__(self,of,thePlayer,enemyTeamState):
		if enemyTeamState == 'Regroup!':
			self.action = 'Defend'
		elif enemyTeamState == 'Attack!':
			if of.currentHP < (ARCHER_HEAL_THRESHOLD * of.hitPoints) and  of.status != 'Defending':
				self.action = 'Defend'
			else:
				self.action = 'Attack'
		else:
			print 'wait waht?'  + enemyTeamState

class ClericTree:
	action = ''
	def __init__(self,cleric,allEnemies,thePlayer,enemyTeamState):
		if enemyTeamState == 'Regroup!':
			self.action = ['Defend',None]
		elif enemyTeamState == 'Attack!':
			if cleric.currentMP >= HEALCOST:
				worstHurt = getWorstHurt(allEnemies)
				if worstHurt.enemyId == cleric.enemyId:
					self.action = ['Defend',None]
				else:
					self.action = ['Heal', worstHurt]
			else:
				if cleric.currentHP < (0.70 * cleric.hitPoints):
					self.action = ['Defend',None]
				else:
					self.action = ['Attack',None]
		else:
			print 'wait waht?' + str(enemyTeamState)


class WizardTree:
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
		else:
			print 'wait waht?'  + enemyTeamState





