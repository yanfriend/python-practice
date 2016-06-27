import imtest
print __name__
class HolyKnight(imtest.Knight):
    '''''I am great HolyKnight'''
    def __init__(self, name, hp, mp):
        imtest.Knight.__init__(self, name, hp)
        self.__mp = mp
        print 'holyknight comes'
kn = HolyKnight('cloudy', 10, 5)
print HolyKnight.__doc__
print imtest.Knight.Count
print kn.name
print kn.getHp()
print kn.__hp
