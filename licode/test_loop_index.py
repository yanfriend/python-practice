

for i in range(10):
    print i,

print ''
print i  # print 9.


def test_print():
    for i in range(10):
        print i,

    print ''
    print i  # print 9.


test_print()

# conclusion: don't use index to measure
