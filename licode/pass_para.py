

def pass_test(ret, path):
    ret.append(path)

ret=[]
path=[1,2]

pass_test(ret, path)
print ret

path.pop()
print ret  # here ret is affected. path passed by ref

##################################

print 'test by value'
ret=[]
pass_test(ret, path+[3]) # here, passed by value
print ret
path.pop()
print path
print ret

