def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       print 'in wrapper func, before calling core func. get the control can do whatever.'
       print 'a wrapper deco is a function first, which take the core func as its first parameter.'
       print 'In wrapper func, it defines another func whose para are args, kwargs that accepts whatever core func has.'
       print '  then it does whatever before/after calling the core func.'
       print 'Finally the wrapper func returns the defined func'
       func(*args, **kwargs)
       print 'in wrapper func, after calling core func'
   return func_wrapper

@p_decorate
def get_text(name):
   print "hello, %s, text from core func." % name

get_text("John")

