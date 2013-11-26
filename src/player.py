class Player:
    hitPoints = 0
    attack = 0
    defence = 0
    dodge = 0.0
    hit = 0.0
    specials = []
    doubleSwing = 0
    currentDefence = 0
    def __init__(self, CharacterType):
        if CharacterType == 'Fighter':
            self.hitPoints = 150
            self.attack = 70
            self.defence = 80
            self.dodge = 5
            self.hit = 60
            self.doubleSwing = 15
            self.currentDefence = self.defence
        elif CharacterType == 'Wizard':
            self.hitPoints = 70
            self.attack = 10
            self.defence = 40
            self.dodge = 15
            self.hit = 65
            self.doubleSwing = 5
            self.currentDefence = self.defence
        elif CharacterType == 'Thief':
            self.hitPoints = 110
            self.attack = 40
            self.defence = 60
            self.dodge = 30
            self.hit = 80
            self.doubleSwing = 30
            self.currentDefence = self.defence
    def printInfo(self):
        print 'Hit Points = ' + str(self.hitPoints)
        print 'Attack     = ' + str(self.attack)
        print 'Defence    = ' + str(self.defence)
        print 'Dodge      = ' + str(self.dodge) + '%'
        print 'Hit        = ' + str(self.hit) + '%'
        print 'DoubleHit  = ' + str(self.doubleSwing) + '%'

