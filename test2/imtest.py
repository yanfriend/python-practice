print __name__
class Knight:
    '''''I am strong Knight'''
    Count = 0
    def __init__(self, name, hp):
        Knight.Count += 1
        self.name = name
        self.__hp = hp
        print 'knight comes'
    def die(self):
        self.__hp = 0
    def getHp(self):
        return self.__hp
