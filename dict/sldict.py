from dict.abstract import DictAbstract

class _Pair():
  def __init__(self, key, value):
    self.key = key # country name
    self.value = value # country object

  def __str__(self):
    return str(self.key) + ": \n" + str(self.value) + "\n\n"

class SLDict(DictAbstract):
  def __init__(self):
    self._sortedList = [] # a list of _Pair objects
    self.size = 0

  
  # Written by: Alwin
  # Description : Based on the code given in lecture.
  def _insertion_sort(self):
    for i in range(1, len(self._sortedList)):
      j = i
      while j > 0 and self._sortedList[j].key < self._sortedList[j - 1].key:
        temp = self._sortedList[j]
        self._sortedList[j] = self._sortedList[j - 1]
        self._sortedList[j - 1] = temp
        j -= 1

  # Written by: Alwin
  #Return the number of items stored in the dictionary
  def __len__(self):
    return len(self._sortedList)

  # Written by: Alwin
  #Implementing the python magic method __contains__
  #This will help to use in true or false sentences
  #e.g., if key is in dict
  def __contains__(self, key):
    # Checks the entire list for a matching key.
    for i in self._sortedList:
      if key.lower() == i.key.lower():
        return True
    # Returns False if a matching key is not found.
    return False

  # Author: Vel
  #Implementing the python magic method __getitem__
  #This function will help in using this syntax dict[key]
  def __getitem__(self, keyValue):  
    # traverse list for all key value pairs.
    for pair in self._sortedList:
      # if key is found
      if pair.key.lower() == str(keyValue).lower(): # eliminates case sensivity
        return pair.value # returns country object
    return None # otherwise, return none 
    # Implement KeyError?

  #Author: Elyas
  #Implements self[key] = value.  If key is already stored in
  #the dictionary then its value is modified.  If key is not in the map,
  #it is added.
 
  def __setitem__(self, keyVal, val):
    if self._sortedList != []:
      for pair in self._sortedList:
        #if key already exsits 
        if pair.key.lower() == keyVal.lower():
          pair.value = val # update the value
          return
    #otherwise, add a new key-value pair to the list
    pairObj = _Pair(keyVal, val)
    self._sortedList.append(pairObj)
    self.size += 1
    self._insertion_sort()

  # Loop through the dictionary, get all the values, put the values in a list, and return the list
  def values(self):
    values = []
    for pair in self._sortedList:
      values.append(pair.value)
    return values

  def __str__(self):
    l = ""
    for i in self._sortedList:
      l += str(i)
    return l
    
      
