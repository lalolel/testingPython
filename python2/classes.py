class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

  def is_edible(self):
    if not self.poisonous:
      print "Yep! I'm edible."
    else:
      print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

''' Create a class called Animal in the editor. For now, in the body of your class, use the pass keyword. (pass doesn’t do anything, but it’s useful as a placeholder in areas of your code where Python expects an expression.) '''
'''     started our class definition off with an odd-looking function: __init__(). 
This function is required for classes, and it’s used to initialize the objects it creates. __init__() always takes at least one argument, self, that refers to the object being created. 
You can think of __init__() as the function that “boots up” each object the class creates. '''

class Animal(object):
  def __init__(self):
    pass
