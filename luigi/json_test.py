import json
args = '["foo", {"bar":["baz", null, 1.0, 2]}]'
dict = json.loads(args)

#class TaskAdd():
#    def real_fun(self, a, b):
#        return a+b

args = '{"a":1, "b":2}'
dict = json.loads(args)
print(dict)

#obj = TaskAdd();
#print(obj.real_fun( 1,2))
