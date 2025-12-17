import self


class Stack:
  """  pass keyword   you have to add pass in an empty class otherwise you get the error"""

  def __init__(self):    """init is constructor used for creating object of class Stack"""
    self.items = [];     """the items properties of the object that we are creating, self refers to specific instance of the class"""

  def push(self, item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()