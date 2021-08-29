def insertion_sort(arr):

  for i in range(1,len(arr)):
    j = i - 1
    temp = arr[i]

    while j >= 0 and temp < arr[j]:
      arr[j + 1]= arr[j]
      j = j - 1
      arr[j + 1] = temp
  return arr






if __name__=="__main__":
  arr=[5,12,7,5,5,7]
  print(insertion_sort(arr))
