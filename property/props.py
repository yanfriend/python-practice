class Props(object):
   _x = 0
   @property
   def x(self):
     return self._x
   @x.setter
   def x(self, x):
     self._x = x

