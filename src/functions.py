import sys,os,random,time,trees
from random import randint
from config import *
from player import Player
from enemies import Enemies


def endofLine():
    sys.stdout.write('\n')

def clearScreen():
    command = ''
    if myOS == 'Windows':
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)

def tryAgain():
    clearScreen()
    print 'please try again'

def updateEnemey(enemy,row):
	for i in range(len(row)):
		if row[i] == enemy.enemyId:
			row[i] == enemy
	return row

def validId(frontRow,backRow,mId):
	for x in frontRow:
		if x.enemyId == mId:
			return True
	for x in backRow:
		if x.enemyId == mId:
			return True
	return False

def getEnemey(frontRow,backRow,mId):
	for x in frontRow:
		if x.enemyId == mId:
			return x
	for x in backRow:
		if x.enemyId == mId:
			return x

def printEnemies(frontRow,backRow):
	print '-------------FRONT ROW--------------'
	for x in frontRow:
		x.printInfoLine()
	endofLine()
	print '-------------BACK ROW---------------'
	for x in backRow: 
		x.printInfoLine()

def resetEnemies(frontRow,backRow):
	for x in frontRow:
		x.currentDefence = x.defence
		#x.status = 'Nothing'
	for x in backRow:      
		x.currentDefence = x.defence
		#x.status = 'Nothing'
	return [frontRow,backRow]

def resetPlayer(thePlayer):
	thePlayer.currentDefence = thePlayer.defence
	return thePlayer


def removeDeadEnemeies(row):
	return filter(lambda x: x.currentHP > 0, row)

def changeRow(row,enemy):
	for i in range(len(row)):
		if row[i].enemyId == enemy.enemyId:
			row[i] = enemy
	return row

def AttackEnemy(attacker,defender):
	lowerBound = int(attacker.attack * 0.7)
	upperBound = int(attacker.attack * 1.5)
	baseDamage = randint(lowerBound,upperBound)
	armorReduction = (((150 - defender.currentDefence) / 100.0) * 0.7)
	trueDamage = int(baseDamage * armorReduction)
	defender.currentHP = defender.currentHP - trueDamage
	return [defender,trueDamage]


def Attack(attacker,defender,frontRow,backRow,playerAttack):
	if playerAttack:
		doubleAttack = randint(1,100) <= attacker.doubleSwing
		dodge = randint(1,100) <= defender.dodge
		if dodge:
			print 'You attacked ' + defender.enemyType + ' and Missed!!'
		else:
			enemyAfterAttack,dmgDone = AttackEnemy(attacker,defender)
			print 'You attacked ' + enemyAfterAttack.enemyType + ' and dealt ' + str(dmgDone) + ' damage!'
			if defender.row == 1:
				frontRow = changeRow(frontRow,enemyAfterAttack)
			else:
				backRow = changeRow(backRow,enemyAfterAttack)
		if doubleAttack:
			print 'Double Swing!!!'
			dodge = randint(1,100) <= defender.dodge
			if dodge:
				print 'You attacked ' + defender.enemyType + ' and Missed!!'
			else:
				doubleAttackChance = randint(1,100)
				doubleAttack = doubleAttackChance <= attacker.doubleSwing
				enemyAfterAttack,dmgDone = AttackEnemy(attacker,defender)
				print 'You attacked ' + enemyAfterAttack.enemyType + ' and dealt ' + str(dmgDone) + ' damage!'
				if defender.row == 1:
				    frontRow = changeRow(frontRow,enemyAfterAttack)
				else:
					backRow = changeRow(backRow,enemyAfterAttack)
		return [attacker,frontRow,backRow]
	else:
		playerAfterAttack = defender
		doubleAttack = randint(1,100) <= attacker.doubleSwing
		dodge = randint(1,100) <= defender.dodge
		if dodge:
			print attacker.enemyType + ' attacked You and Missed!!'
		else:
			playerAfterAttack,dmgDone = AttackEnemy(attacker,defender)
			print attacker.enemyType + ' Attacked you for ' + str(dmgDone) + ' damage!'
		if doubleAttack:
			print 'Enemy Double Swing!!!'
			dodge = randint(1,100) <= defender.dodge
			if dodge:
				print attacker.enemyType + ' attacked You and Missed!!'
			else:
				playerAfterAttack,dmgDone = AttackEnemy(attacker,defender)
				print attacker.enemyType + ' Attacked you for ' + str(dmgDone) + ' damage!'
		return [playerAfterAttack,frontRow,backRow]

def Defend(el,playerDefend):
	printString = ''
	healAmount = 0
	defenceBonus = 0
	healingBonus = 0
	if playerDefend:
		printString = 'You'
		defenceBonus = 1.5
		healingBonus = 0.1
	else:
		printString = el.enemyType
		defenceBonus = 1.2
		healingBonus = 0.06
	el.currentDefence = el.currentDefence * defenceBonus
	if el.currentHP >= (el.hitPoints * 1 - healingBonus):
		healAmount = el.hitPoints - el.currentHP
		el.currentHP = el.hitPoints
	else:
		healAmount = int(el.hitPoints * healingBonus)
		el.currentHP = el.currentHP + int(el.hitPoints * healingBonus)

	print printString + ' Defended! New Armor: ' + str(el.currentDefence * defenceBonus) + '! Healed for ' + str(healAmount) + '!'
	return el

def enemyTurn(thePlayer,frontRow,backRow):
	for x in frontRow:
		frontRowTree = trees.OrcFighterTree(x,thePlayer)
		mAction = frontRowTree.action
		print x.enemyType + ' ' + mAction
		#print x.printInfo()
		if mAction == 'Attack':
			thePlayer,frontRow,backRow = Attack(x,thePlayer,frontRow,backRow,False)
			x.status = 'Attacking'
			frontRow = updateEnemey(x,frontRow)
		elif mAction == 'Defend':
			x.status = 'Defending'
			x = Defend(x,False)
			frontRow = updateEnemey(x,frontRow)

	print '==================' + frontRow[0].status
	return [thePlayer,frontRow,backRow]	




