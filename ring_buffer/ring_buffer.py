#  Info ---
#  Ring buffers are a FIFO -> First in First Out system.
#  The "Ring" has a fixed size once that limit is reached it gets deleted (but were not doing that in this project)

#  --- Spec ---
#  Implement a system to add data (append) to the ring buffer
#  Implement a system to get ALL of the data from the buffers's list

#  --- Pre-Mature Plan ---
#  The list's length starts at None * capacity
#
#  So we can check to see if current equals Null
#     We remove the last peice of data
#     Insert the new peice of data
#     Set the current value to 1 for tracking of current as its the first entry
#  Else if current equals the capacity
#     Remove the first item in the ring (list)
#     Increment the counter to counter + 1
#  Else
#     If neither of those cases work we need to remove current
#     Insert the the "item"
#     Increment the counter by 1


class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #  If current is the capacity
    if self.current == self.capacity:
      #  Remove 0 index just incase, insert the item into the first index, set current to 1
      self.storage.pop(0)
      self.storage.insert(0, item)
      self.current = 1
    #  if the storages list is None
    elif self.storage[self.current] == None:
      # Remove from last peice of entered data (end of list), add new data at the current index, current + 1
      self.storage.pop(self.current)
      self.storage.insert(self.current, item)
      self.current += 1
    else:
      #  If none of those conditions are true, we remove current, insert current and increment
      self.storage.pop(self.current)
      self.storage.insert(self.current, item)
      self.current += 1

  def get(self):
    # Returns the list
    returnable = list(filter(None, self.storage))
    return returnable

#buffer = RingBuffer(7)
#print(f"1: {len(buffer.storage)}")
#print(f"2: {buffer.append('a')} - {buffer.current} - {buffer.storage}")
#print(f"3: {buffer.append('b')} - {buffer.current} - {buffer.storage}")
#print(f"4: {buffer.append('c')} - {buffer.current} - {buffer.storage}")
#print(f"5: {buffer.append('d')} - {buffer.current} - {buffer.storage}")
#print(f"6: {buffer.append('e')} - {buffer.current} - {buffer.storage}")
#print(f"7: {buffer.append('f')} - {buffer.current} - {buffer.storage}")
#print(f"8: {buffer.append('g')} - {buffer.current} - {buffer.storage}")
#print(f"9: {buffer.append('h')} - {buffer.current} - {buffer.storage}")
#print(f"10: {buffer.append('i')} - {buffer.current} - {buffer.storage}")
#print(f"11: {len(buffer.storage)}")
#print(buffer.storage)
#print(buffer.get())
