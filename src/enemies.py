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
    def __init__(self, EnemyType,ID):
        if EnemyType == 'HOF':
            self.enemyType = 'Heavy Orc Fighter'
            self.enemyId = ID
            self.hitPoints = 150
            self.attack = 25
            self.defence = 80
            self.dodge = 5
            self.hit = 60
            self.doubleSwing = 15
            self.row = 1
        elif EnemyType == 'LOF':
            self.enemyType = 'Light Orc Figher'
            self.enemyId = ID
            self.hitPoints = 70
            self.attack = 45
            self.defence = 60
            self.dodge = 15
            self.hit = 65
            self.doubleSwing = 5
            self.row = 1
        elif EnemyType == 'DEW':
            self.enemyType = 'Dark Elf Wizard'
            self.enemyId = ID
            self.hitPoints = 70
            self.attack = 45
            self.defence = 40
            self.dodge = 15
            self.hit = 65
            self.doubleSwing = 5
            self.row = 2
        elif EnemyType == 'DEC':
            self.enemyType = 'Dark Elf Cleric'
            self.enemyId = ID
            self.hitPoints = 70
            self.attack = 45
            self.defence = 40
            self.dodge = 15
            self.hit = 65
            self.doublewing = 5
            self.row = 2
        elif EnemyType == 'DEA':
            self.enemyType = 'Dark Elf Archer'
            self.enemyId = ID
            self.hitPoints = 110
            self.attack = 15
            self.defence = 50
            self.dodge = 30
            self.hit = 80
            self.doubleSwing = 30
            self.row = 2
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

