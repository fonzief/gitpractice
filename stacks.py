##########################node class########
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

  def get_next_node(self):
    return self.next_node

  def get_value(self):
    return self.value

#########################################





class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit

  def has_space(self):
    if self.limit > self.size:
      return True

  def is_empty(self):
    if self.size == 0:
      return True

  def push(self, value):
    item = Node(value)
    if self.size < self.limit:
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1


  def pop(self):
    if not self.size.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
	    return self.top_item.get_value()
    else:
      print("Nothing to see here!")


  
