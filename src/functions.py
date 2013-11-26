import sys,os,random,time
from config import *
from player import Player
from enemies import Enemies


def changeRow(row,enemy):
	for i in range(len(row)):
		if row[i].enemyId == enemy.enemyId:
			row[i] = enemy
	return row

def Attack(attacker,defender):
	lowerBound = int(attacker.attack * 0.7)
	upperBound = int(attacker.attack * 1.5)
	#print '==================' + str(upperBound) + ' ' + str(lowerBound)
	baseDamage = random.randint(lowerBound,upperBound)
	#print '==================' + str(baseDamage)
	print defender.currentDefence
	armorReduction = (((150 - defender.currentDefence) / 100.0) * 0.7)
	#print '==================' + str(armorReduction)
	trueDamage = int(baseDamage * armorReduction)
	#print '==================' + str(trueDamage)
	defender.hitPoints = defender.hitPoints - trueDamage
	return [defender,trueDamage]

def Defend(el):
	el.currentDefence = el.currentDefence * 1.5
	return el

