# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
  print(arrA, arrB)
  merged_arr = []
  while (len(arrA) and len(arrB)):
    if (arrA[0] < arrB[0]):
      merged_arr.append(arrA.pop(0))
    else:
      merged_arr.append(arrB.pop(0))
    
  merged_arr.extend(arrA + arrB)
   
  return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 1 or len(arr) == 0:
      return arr
    else:
      mid = len(arr) // 2
      left = arr[0:mid]
      right = arr[mid:]
      return merge(merge_sort(left), merge_sort(right))

    #return arr#

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
