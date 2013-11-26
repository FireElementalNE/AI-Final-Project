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


def printEnemies(frontRow,backRow):
	print '-------------FRONT ROW--------------'
	for x in frontRow:
		x.printInfoLine()
	endofLine()
	print '-------------BACK ROW---------------'
	for x in backRow: 
		x.printInfoLine()

def reset(frontRow,backRow,thePlayer):
	thePlayer.currentDefence = thePlayer.defence
	for x in frontRow:
		x.currentDefence = x.defence
	for x in backRow:      
		x.currentDefence = x.defence
	return [frontRow,backRow,thePlayer]


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

def Defend(el):
	el.currentDefence = el.currentDefence * 1.5
	if el.currentHP >= (el.hitPoints * 0.9):
		el.currentHP = el.hitPoints
	else:
		el.currentHP = el.currentHP + int(el.hitPoints * 0.1)
	return el

def enemyTurn(thePlayer,frontRow,backRow):
	for x in frontRow:
		frontRowTree = trees.OrcFighterTree(x,thePlayer)
		mAction = frontRowTree.action
		if mAction == 'Attack':
			thePlayer,frontRow,backRow = Attack(x,thePlayer,frontRow,backRow,False)
	return [thePlayer,frontRow,backRow]	




