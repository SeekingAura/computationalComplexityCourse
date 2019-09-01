def bubble_sort(vector):
 n=len(vector)
 for i in range(n):
  # Check actual value with next value
  for j in range(0, n-i-1):
   # Comparision
   if(vector[j]>vector[j+1]):
    # Swapping
    vector[j], vector[j+1]=vector[j+1]\
     , vector[j]