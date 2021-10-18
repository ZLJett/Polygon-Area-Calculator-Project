"""Rectangle and Square classes module

This Module contains a Rectangle class and Square class that is a child of the Rectangle class. These classes 
allow the user to create and manipulate rectangle and square objects and find further information on these objects,
such as the perimeter, area, or diagonal of the object. This module further provides a visual representation of the object as
well as the ability to see how many of one of these objects fits in another.     

Classes:
    Rectangle 
    Square
"""

import math


class Rectangle:
  """
  A class that represents a Rectangle.
  
  Attributes:
      width (int): The width of the Rectangle.
      height (int): The height of the Rectangle.
  """

  def __init__(self, width, height):
    """ Constructs all the necessary attributes for the Rectangle object.     
    
    Parameters:
        width (int): The width of the Rectangle.
        height (int): The height of the Rectangle.
    """
    self.width = width
    self.height = height

  def set_width(self, new_width):
    """Sets width of the shape."""
    self.width = new_width

  def set_height(self, new_height):
    """Sets height of the shape."""
    self.height = new_height

  def get_area(self):
    """Returns the area of the shape"""
    return self.width * self.height

  def get_perimeter(self):
    """Returns the perimeter of the shape"""
    return (self.width * 2) + (self.height * 2)

  def get_diagonal(self):
    """Returns the length of the diagonal of the shape"""
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    """Returns a string that represents the shape using lines of "*"."""
    if self.width >= 50 or self.height >= 50:
      return "Too big for picture."
    line = "*" * self.width + "\n"
    full_shape = line * self.height
    return full_shape
  
  def get_amount_inside(self, other_shape):
    """
    Finds the number of times a shape could fit inside this shape.
    
    Parameters:
        other_shape (Rectangle object): A Rectangle object or a child class thereof.

    Returns:
        num_fits_inside (int): Returns the number of times the passed in shape could fit inside the shape (with no rotations).
    """
    # Here trunc takes care of rounding down.
    amount_in_height = math.trunc(self.height / other_shape.height)
    amount_in_width = math.trunc(self.width / other_shape.width)
    num_fits_inside = amount_in_height * amount_in_width
    return num_fits_inside
  
  def __str__(self):
    """Returns a string that tells you the shape and its dimensions"""
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"


class Square(Rectangle):
  """
  This is a child class of the Rectangle class that represents a Square.

  Attributes:
      width (int): The width of the Square.
      height (int): The height of the Square.
  """

  def __init__(self, sides):
    """Constructs all the necessary attributes for the Square object.       
    
    Parameter:
        sides (int): The height and width of the Rectangle.
    """
    super().__init__(sides, sides)
   
  def set_side(self, new_sides):
    """Sets sides of the shape."""
    self.width = new_sides
    self.height = new_sides

  def set_width(self, new_width):
    """Sets width and height of the shape."""
    self.width = new_width
    self.height = new_width

  def set_height(self, new_height):
    """Sets height and width of the shape."""
    self.height = new_height
    self.width = new_height

  def __str__(self):
    """Returns a string that tells you the shape and its dimensions"""
    return "Square(side=" + str(self.width) + ")"




