import sys,time,functions,getpass
from random import randint
from config import *
from player import Player
from enemies import *

playerClasses = ['Fighter', 'Thief']
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
        playerClassChoice = int(raw_input('>'))
        if playerClassChoice >= 0 and playerClassChoice <= len(playerClasses):
            break
        else:
            raise ValueError
    except ValueError:
        print 'Incorrect Choice! Please Try again!'

thePlayer = Player(playerClasses[playerClassChoice])
thePlayer.printInfo()

print 'How many enemies do you want to fight?'
while True:
    try:
        enemyCount = int(raw_input('>'))
        break
    except ValueError:
        continue

frontRowCount = (enemyCount / 2) + 1
backRowCount = enemyCount - frontRowCount
functions.endofLine()

print 'Picking Enemies!'
functions.endofLine()
frontRow = []
backRow = []

for i in range(frontRowCount):
    tempEnemyIndex = randint(0,len(frontRowPossibilities)-1)
    frontRow.append(Enemy(frontRowPossibilities[tempEnemyIndex],i))
for i in range(backRowCount):
    tempEnemyIndex = randint(0,len(backRowPossibilities)-1)
    backRow.append(Enemy(backRowPossibilities[tempEnemyIndex],i+len(frontRow)))

allEnemies = Enemies(frontRow,backRow)

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
    if len(allEnemies.getAllEnemies()) <= 0:
        print 'YOU WIN!'
        break;
    elif thePlayer.currentHP <= 0:
        print 'YOU LOST!'
        break;
    wait = getpass.getpass('press enter key to continue...')
    thePlayer = functions.resetPlayer(thePlayer)
    allEnemies.printEnemies()
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
        for x in allEnemies.getAllEnemies():
            print '[' + str(x.enemyId) + '] ' + x.enemyType
        try:
            enemyToAttackID = int(raw_input('>'))
            if not allEnemies.validId(enemyToAttackID):
                raise ValueError
        except ValueError:
            functions.tryAgain()
            continue
        enemyToAttack = allEnemies.getEnemey(enemyToAttackID)
        thePlayer,allEnemies= functions.Attack(thePlayer,enemyToAttack,allEnemies,True)
    if command == 'Defend':
        thePlayer = functions.Defend(thePlayer,True)
        print 'You are Defending!'
        print 'current Stats:'
        thePlayer.printInfo('--> ')
    allEnemies.resetEnemies()
    allEnemies.removeDeadEnemeies()
    functions.endofLine()
    functions.endofLine()
    thePlayer,allEnemies = functions.enemyTurn(thePlayer,allEnemies)
    functions.endofLine()

