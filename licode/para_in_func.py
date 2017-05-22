
def my_func(la,lb):
    la.append('la')
    lb=['lb']

la=[]
lb=[]
my_func(la,lb)
print la, lb

# la content changed; not lb
