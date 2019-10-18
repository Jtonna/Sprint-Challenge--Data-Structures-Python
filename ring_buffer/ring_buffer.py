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
    if 1+1 == 1:
      pass
    elif 1 + 1 == 2:
      pass
    else:
      pass

  def get(self):
    pass
