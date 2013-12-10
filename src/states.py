from enemies import Enemies
from config import *

class States:
	currentState = ''
	def __init__(self,initState):
		self.currentState = initState

	def updateState(self,allEnemies):
		maxHP = 0
		allCurrentHP = 0
		maxMP = 0
		allCurrentMP = 0
		enemyEntities = allEnemies.getAllEnemies()
		for x in enemyEntities:
			maxHP += x.hitPoints
			allCurrentHP += x.currentHP
			maxMP += x.magicPoints
			allCurrentMP + x.currentMP
		if maxMP == 0:
			maxMP = 1
		if maxHP == 0:
			maxHP = 1
		percentageHP = (float(allCurrentHP) / maxHP) * 100
		percentageMP = (float(allCurrentMP) / maxMP) * 100
		if self.currentState == 'Attack!':
			if percentageHP < 70 and percentageMP < 30:
				self.currentState = 'Regroup!'
			else:
				self.currentState = 'Attack!'
		elif self.currentState == 'Regroup!':
			self.currentState = 'Attack!'