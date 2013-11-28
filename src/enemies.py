from sys import stdout
class Enemies:
    enemyType = ''
    enemyId = ''
    hitPoints = 0
    attack = 0
    defence = 0
    dodge = 0.0
    hit = 0.0
    specials = []
    doubleSwing = 0
    state = None
    row = None
    currentDefence = 0
    currentHP = 0
    status = 'Nothing'
    magicPoints = 0
    currentMP = 0
    def __init__(self, EnemyType,ID):
        if EnemyType == 'HOF':
            self.enemyType = 'Heavy Orc Fighter'
            self.enemyId = ID
            self.hitPoints = 300
            self.attack = 20
            self.defence = 80
            self.dodge = 5
            self.hit = 60
            self.doubleSwing = 5
            self.row = 1
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
        elif EnemyType == 'LOF':
            self.enemyType = 'Light Orc Figher'
            self.enemyId = ID
            self.hitPoints = 190
            self.attack = 27
            self.defence = 60
            self.dodge = 15
            self.hit = 65
            self.doubleSwing = 15
            self.row = 1
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
        elif EnemyType == 'DEW':
            self.enemyType = 'Dark Elf Wizard'
            self.enemyId = ID
            self.hitPoints = 140
            self.attack = 45
            self.defence = 40
            self.dodge = 15
            self.hit = 65
            self.doubleSwing = 1
            self.row = 2
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
            self.magicPoints = 100
            self.currentMP = self.magicPoints
        elif EnemyType == 'DEC':
            self.enemyType = 'Dark Elf Cleric'
            self.enemyId = ID
            self.hitPoints = 140
            self.attack = 15
            self.defence = 40
            self.dodge = 15
            self.hit = 65
            self.doublewing = 5
            self.row = 2
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
            self.magicPoints = 100
            self.currentMP = self.magicPoints
        elif EnemyType == 'DEA':
            self.enemyType = 'Dark Elf Archer'
            self.enemyId = ID
            self.hitPoints = 170
            self.attack = 17
            self.defence = 50
            self.dodge = 30
            self.hit = 80
            self.doubleSwing = 20
            self.row = 2
            self.currentDefence = self.defence
            self.currentHP = self.hitPoints
    def printInfo(self):
        print 'ID         = ' + str(self.enemyId)
        print 'Name       = ' + self.enemyType
        print 'Hit Points = ' + str(self.hitPoints)
        print 'Attack     = ' + str(self.attack)
        print 'Defence    = ' + str(self.defence)
        print 'Dodge      = ' + str(self.dodge) + '%'
        print 'Hit        = ' + str(self.hit) + '%'
        print 'DoubleHit  = ' + str(self.doubleSwing) + '%'
        print 'Row        = ' + str(self.row)
        print 'C Defence  = ' + str(self.currentDefence)
        print 'C HP       = ' + str(self.currentHP)
    def printInfoLine(self):
         stdout.write('ID: ' + str(self.enemyId) + ' Type:' + str(self.enemyType) + ' HP:' + str(self.currentHP) + ' STATUS: ' + self.status + ' MP: ' + str(self.currentMP) + '\n')

