#  Info ---
#  Ring buffers are a FIFO -> First in First Out system.
#  The "Ring" has a fixed size once that limit is reached it gets deleted (but were not doing that in this project)

#  Spec ---
#  Implement a system to add data (append) to the ring buffer
#  Implement a system to get ALL of the data from the buffers's list

#  Pre-Mature plan ---
#  


class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    pass

  def get(self):
    pass
