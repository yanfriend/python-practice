x = open('chinese.txt').read()
print len(x)

y = x.decode('utf-8')
print len(y)

z = y.encode('utf-8')
print z==x

"""
Once you're done processing your Unicode strings, if you want to write them out to a file or database, first convert them back to a sequence of bytes (the str type) using the encode method
"""
