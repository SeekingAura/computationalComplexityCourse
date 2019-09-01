def swap(array, a, b):
 array[a], array[b] = array[b], array[a]

def quickSort(array, left, right):
 # set ref for integer values

 if left >= right: return
 
 pivot = int((left + right) / 2)

 l = left
 r = right

 while True:
  # Determine l and r for swaping
  while array[l] < array[pivot]: l += 1
  while array[r] > array[pivot]: r -= 1

  if l == r: break
  
  # swap(array, l, r)
  array[l], array[r] = array[r], array[l]

  if l == pivot:
   pivot = r
   l += 1
  elif r == pivot:
   pivot = l
   r -= 1
  else:
   l += 1
   r -= 1

 quickSort(array, left, pivot-1)
 quickSort(array, pivot + 1, right)