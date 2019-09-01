def countingSort(array):
 _min = min(array)
 _max = max(array)
 bot = _min * -1

 if _min < 0:
  size = bot + (_max + 1)
 else:
  size = _max + 1
  bot = 0
 
 # get times are a value, where 
 # the index is the value and 
 # the value is the times are in vector
 count = [0] * size
 for item in array:
  index = bot + item
  count[index] += 1
 
 # get number "distance" to get a value
 # in the list from the value with index
 for i in range(1, size):
  count[i] += count[i-1] 

 # set on list result from distance 
 # with vector count
 result = [0] * len(array)
 for item in array:
  index = bot + item
  result[count[index] - 1] = item
  count[index] -= 1
  
 return result