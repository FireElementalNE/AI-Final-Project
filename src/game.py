import sys,time,functions,getpass
from random import randint
from config import *
from player import Player
from enemies import Enemies
#p1 = Player('Fighter')
#p2 = Player('Wizard')
#p3 = Player('Thief')
#e1 = Enemies('HOF',1)
#e2 = Enemies('LOF',2)
#e3 = Enemies('DEW',3)
#e4 = Enemies('DEC',4)
#e5 = Enemies('DEA',5)

playerClasses = ['Fighter', 'Wizard', 'Thief']
enemyClasses = ['HOF','LOF','DEW','DEC','DEA']
frontRowPossibilities = ['HOF','LOF']
backRowPossibilities = ['DEW','DEC','DEA']
commandPossibilities = ['Attack','Defend', 'Exit']



functions.clearScreen()
print 'Welcome to AI Battle!'
print '------------------------------------------'
print 'Please pick your player class! (pick number NOT name)'
while True:

    for i in range(len(playerClasses)):
        print '[' + str(i)+ ']:' + ' ' + playerClasses[i]
    try:
        playerClassChoice = 0#int(raw_input('>'))
        if playerClassChoice >= 0 and playerClassChoice <= len(playerClasses):
            break
        else:
            raise ValueError
    except ValueError:
        print 'Incorrect Choice! Please Try again!'

thePlayer = Player(playerClasses[i])
thePlayer.printInfo()
enemyRow1 = []
enemyRow2 = []
print 'How many enemies do you want to fight?'
while True:
    try:
        enemyCount = 5#int(raw_input('>'))
        break
    except ValueError:
        continue

frontRowCount = (enemyCount / 2) + 1
backRowCount = enemyCount - frontRowCount
functions.endofLine()
#print 'FRONT ROW COUNT: ' + str(frontRowCount) + ' BACK ROW COUNT: ' + str(backRowCount)

print 'Picking Enemies!'
functions.endofLine()
frontRow = []
backRow = []

for i in range(frontRowCount):
    tempEnemyIndex = randint(0,len(frontRowPossibilities)-1)
    frontRow.append(Enemies(frontRowPossibilities[tempEnemyIndex],i))
for i in range(backRowCount):
    tempEnemyIndex = randint(0,len(backRowPossibilities)-1)
    backRow.append(Enemies(backRowPossibilities[tempEnemyIndex],i+len(frontRow)))



sys.stdout.write('Starting Game!')
#time.sleep(1)
sys.stdout.write('.')
#time.sleep(1)
sys.stdout.write('.')
#time.sleep(1)
sys.stdout.write('.')
functions.endofLine()
functions.endofLine()
command = ''

while command.lower() not in exitStrings:
    wait = getpass.getpass('press enter key to continue...')
    allEnemies = frontRow + backRow
    frontRow,backRow,thePlayer = functions.reset(frontRow,backRow,thePlayer)
    functions.printEnemies(frontRow,backRow)
    functions.endofLine()
    thePlayer.printInfoLine()
    functions.endofLine()
    print 'Commands!'
    for i in range(len(commandPossibilities)):
        print '[' + str(i) + '] ' + commandPossibilities[i]
    try:
        command = int(raw_input('>'))
        if command >= len(commandPossibilities) or command < 0:
            raise ValueError
    except ValueError:
        functions.tryAgain()
        continue
    functions.clearScreen()
    command = commandPossibilities[command]
    if  command == 'Attack':
        print 'Attack Who?'
        for x in allEnemies:
            print '[' + str(x.enemyId) + '] ' + x.enemyType
        try:
            enemyToAttackIndex = int(raw_input('>'))
            if enemyToAttackIndex >= len(allEnemies) or enemyToAttackIndex < 0:
                raise ValueError
        except ValueError:
            functions.tryAgain()
            continue
        enemyToAttack = allEnemies[enemyToAttackIndex]
        thePlayer,frontRow,backRow = functions.Attack(thePlayer,enemyToAttack,frontRow,backRow,True)
    if command == 'Defend':
        thePlayer = functions.Defend(thePlayer)
        print 'You are Defending!'
        print 'current Stats:'
        thePlayer.printInfo('--> ')
    functions.endofLine()
    print 'Enemy Turn!'
    functions.endofLine()
    thePlayer,frontRow,backRow = functions.enemyTurn(thePlayer,frontRow,backRow)
    functions.endofLine()

    #command = 'e'

