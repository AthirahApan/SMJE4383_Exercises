import math

class Point(object):
   def __init__(self, x_param = 0.0, y_param = 0.0):
      '''Create x and y attributes. Default are 0.0'''
      self.x = x_param
      self.y = y_param
   
   def distance (self,param_pt):
      "Distance between self and a Point"""
      x_diff = self.x - param_pt.x
      y_diff = self.y - param_pt.y
      return math.sqrt(x_diff**2 + y_diff**2)
      
   def sum (self,param_pt):
      return Point(self.x + param_pt.x, self.x + param_pt.x)    
      
   def __str__(self):
      return "({:.2f}, {:.2f})".format(self.x,self.y)  
   
