def quick_sort(arr, left, right):
  if left < right:
    position = partition(arr, left, right)
    quick_sort(arr, left, position - 1)
    quick_sort(arr, position + 1, right)
  return arr

def partition(arr, left, right):
  pivot = arr[right]
  i = left - 1

  for j in range(left,right):
    if arr[j] <= pivot:
      i+=1
      swap(arr, j, i)
  swap(arr, right, i+1 )

  return i +1

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
  return arr




if __name__=="__main__":
  arr = [8,4,23,42,16,15]
  print(quick_sort(arr,0, len(arr)-1))
