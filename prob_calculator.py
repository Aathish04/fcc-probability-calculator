import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self,**kwargs):
    self.contents=[]
    for ball in kwargs:
      for i in range(kwargs[ball]):
        self.contents.append(ball)
  
  def draw(self,num):
    if num >= len(self.contents):
      drawn=self.contents
      self.contents=[]
    else:
      drawn=random.sample(self.contents,k=num)
      for ball in drawn:
        if ball in self.contents:
          self.contents.remove(ball)
    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success=0
  e_balls=[]
  for ball in expected_balls:
      for i in range(expected_balls[ball]):
        e_balls.append(ball)
  
  for i in range(num_experiments):
    a=copy.deepcopy(hat)
    drawn=a.draw(num_balls_drawn)
    for e_ball in e_balls:
      if not(drawn.count(e_ball) >= e_balls.count(e_ball)):
        break
    else:
      success+=1
  return success/num_experiments
