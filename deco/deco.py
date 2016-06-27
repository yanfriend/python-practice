def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       print 'in wrapper func, before calling core func. get the control can do whatever.'
       print 'a wrapper deco is a function first'
       func(*args, **kwargs)
       print 'in wrapper func, after calling core func'
   return func_wrapper

@p_decorate
def get_text(name):
   print "hello, %s, text from core func." % name

get_text("John")

