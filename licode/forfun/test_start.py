def test_star1(*para):
    print para, type(para)

    for pp in para:
        print pp

test_star1([1,2,3])
'''
([1, 2, 3],) <type 'tuple'>
[1, 2, 3]
'''

test_star1(*[1,2,3])
'''
(1, 2, 3) <type 'tuple'>
1
2
3
'''

test_star1(*(['abc','def']))
'''
('abc', 'def') <type 'tuple'>
abc
def
'''
