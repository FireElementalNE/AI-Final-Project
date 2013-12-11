from sys import argv
from enemies import Enemies
from config import *

# FSM to descibe the states of the entire enemy team
class States:
	currentState = ''
	def __init__(self,initState):
		self.currentState = initState
	def updateState(self,allEnemies): # state interactions are shown in figure 5
		maxHP = 0
		allCurrentHP = 0
		maxMP = 0
		allCurrentMP = 0
		enemyEntities = allEnemies.getAllEnemies() # update the state using all enemies
		for x in enemyEntities:
			maxHP += x.hitPoints
			allCurrentHP += x.currentHP
			maxMP += x.magicPoints
			allCurrentMP + x.currentMP
		if maxMP == 0: # prevent divide by 0
			maxMP = 1
		if maxHP == 0: # prevent divide by 0
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

if __name__ == "__main__": # cannot call directly
    print 'This file, ' + argv[0] + ', is only for import....'
    print 'to Play the game please run main.py:'
    print 'usage: python main.py'