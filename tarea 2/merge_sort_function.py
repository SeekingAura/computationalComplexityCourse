# k is actual evaluate part of array
def merge(array, leftPart, rightPart, k):
 l = 0; r = 0
 left = len(leftPart)
 right = len(rightPart)

 while l < left and r < right:
  # Here do a comparisions
  if leftPart[l] < rightPart[r]:
   # Swap index k with l index of leftpart
   array[k] = leftPart[l]
   l += 1
   
  else:
   # Swap index k with r index 
   # of leftpart
   array[k] = rightPart[r]
   r += 1
  k += 1

 if l < left:
  array[k:k+left-l]=leftPart[l:]
  k += left-l
 
 if r < right:
  array[k:k+right-r]=rightPart[r:]

def sort(array, left, right):

 if left >= right: return

 middle = int ((left + right )/ 2)
 
 sort(array, left, middle)
 sort(array, middle + 1, right)

 # array slice in python is [from:to]
 # where from is exactly index and to 
 # is n-1 where n is to value

 # Takes in array from left to middle
 leftPart = array[left: middle + 1]

 # Takes in array from middle+1 to right
 rightPart = array[middle + 1: right + 1]

 merge(array, leftPart, rightPart, left)