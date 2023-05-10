import copy
import random


class Hat:

  # ----------- initialize: -----------
  # convert argument into contents
  def __init__(self, **args):
    self.contents = []
    for key, value in args.items():
      for _ in range(value):
        self.contents.append(key)

  # ----------- draw method: -----------
  def draw(self, balls_to_draw):
    # if drawn balls exceed content:
    if balls_to_draw > len(self.contents):
      return self.contents

    else:
      new_list = []

      # random_hat = list with shuffle contents
      random_hat = self.contents
      random.shuffle(random_hat)

      # list of drawn balls:
      new_list.append(random_hat[:balls_to_draw])

      #delete from random hat. define new self.contents.
      del random_hat[:balls_to_draw]
      self.contents = random_hat

      #return new list
      return new_list[0]

# ----------- experiment function: -----------
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  tot_achieved = 0

  for _ in range(num_experiments):
    achieved = 0
    # experience hat
    new_hat = copy.deepcopy(hat)

    # balls drawn out of the new hat.
    balls_out = new_hat.draw(num_balls_drawn)

    #chech if drawn balls == expected balls
    for key, value in expected_balls.items():    
      if balls_out.count(key) >= value:
        achieved += 1
        
    if achieved == len(expected_balls): 
      tot_achieved += 1
    else:
      tot_achieved
    
  return tot_achieved / num_experiments

