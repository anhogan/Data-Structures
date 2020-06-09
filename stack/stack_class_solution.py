import sys
sys.path.append('../singly_linked_list/singly_linked_list')
from singly_linked_list import LinkedList

class Stack:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def __len__(self):
    return self.size

  def push(self, value):
    self.storage.add_to_tail(value)
    self.size += 1

  def pop(self):
    if self.size == 0:
      return None
    self.size -= 1
    self.storage.remove_tail()