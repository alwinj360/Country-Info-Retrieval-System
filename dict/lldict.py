from dict.abstract import DictAbstract

class _LLNode():
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

  # Edited by: Alwin
  # Typecasted self.key and self.value as strings.
  # Added two empty lines to be printed after each country's data.
  def __str__(self):
    return str(self.key) + ": " + str(self.value)

# Implementing a dictionary using linked lists (LL).
class LLDict(DictAbstract):

  # Constructing an empty LL
  def __init__(self):
    self.head = None
    self.size = 0

  def __len__(self):
    return self.size

  #Implementing the python magic method __contains__
  #This will help to use in true or false sentences
  #e.g., if key is in dict
  def __contains__(self, key):
    #otherwise return true
    return self._find(self.head, key) is not None

  # Written by Vel
  def _find(self, node, key):
    #internal helper function that locates the node with the matching key
    #base case
    if node is None:
      return None
    #if matching key is found, return node
    # lower() disables input case-sensitivity
    if node.key.lower() == key.lower():
      return node
    #otherwise, keep searching down the list
    else:
      return self._find(node.next, key)

  #Written By: Elyas Ehsan
  #Implementing the python magic method __getitem__
  #This function will help in using this syntax dict[key]
  def __getitem__(self, key):  
   #this will search through the linked list and return the value corresponding to the given key. if key is not found, it will raise a 'KeyError'
    current = self.head
    while current is not None:
      if current.key.lower() == key.lower():
        return current.value
      current = current.next
    raise KeyError("Key not found in dictionary")

  
  # Written by:  Alwin 
  # Description: Implements self[key] = value.  If key is already stored in
  # the dictionary then its value is modified.  If key is not in the map,
  # it is added.
  def __setitem__(self, key, value):
    # If the linked list (LL) is empty, the node is added as the head of the LL.
    if self.head == None:
      self.head = _LLNode(key, value)
      self.size += 1
    # Else, the node is inserted at the end of the LL
    else:
      self._insert(self.head, key, value)

  # Internal helper function for the setitem function.
  # Used to insert a key-value pair into the dictionary.
  def _insert(self, node, key, value):

    # If a matching key is found, then update the value.
    if node.key.lower() == key.lower():
      node.value = value

    # Else-if node is null, a new key-value pair is inserted.
    elif node.next == None:
      node.next = _LLNode(key, value)
      self.size += 1
      
    # If not, look in the next node.
    else:
      self._insert(node.next, key, value)

  def print_dict(self):
    if self.head is not None:
      self._print_dict(self.head)
      
  def _print_dict(self, node):
    if node is not None:
      print(node)
      self._print_dict(node.next)


  # Written by: Vel
  # Edited by: Alwin
    # Modified the function to only return a list of the country objects
    # instead of nodes that contain country objects
  def values(self):
    list = []
    curr = self.head
    while curr is not None:
      list.append(curr.value)
      curr = curr.next
    return list

  
  def __str__(self):
    curr =  self.head
    strg = ""
    while curr is not None:
      if curr.next == None:
        strg += str(curr)
        return strg
      strg += str(curr) + " -> "
      curr = curr.next
    return strg
