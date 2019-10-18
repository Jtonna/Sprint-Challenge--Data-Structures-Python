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
    remove_current = self.storage.pop(self.current)
    insert_in_current_with_item = self.storage.insert(self.current, item)

    #  If current is none do thing
    if self.storage[self.current] == None:
      # Remove from last peice of entered data (end of list), add new data at the current index, current + 1
      remove_current()
      insert_in_current_with_item()
      self.current += 1
    #  If current is the capacity 
    elif self.current == self.capacity:
      #  Remove 0 index just incase, insert the item into the first index, set current to 1
      self.storage.pop(0)
      self.storage.insert(0, item)
      self.current = 1
    else:
      #  If none of those conditions are true, we remove current, insert current and increment
      remove_current()
      insert_in_current_with_item()
      self.current += 1

  def get(self):
    # Returns the list
    returnable = list(filter(None, self.storage))
