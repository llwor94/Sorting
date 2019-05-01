# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr) - 1 
  index = 0
  while True:
    index = (high - low) // 2 
    if arr[index] == target:
      return index
    elif arr[index] > target:
      high = index
    elif arr[index] < target:
      low = index
  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2
  
  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

  if arr[middle] == target:
    return middle

  if arr[middle] > target:
    return binary_search_recursive(arr, target, low, middle)
  elif arr[middle] < target:
    return binary_search_recursive(arr, target, middle, high)
  else:
    return -1
