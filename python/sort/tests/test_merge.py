from sort.merge_sort import merge_sort

def test_merge_sort1():
  expected= [4, 8, 15, 16, 23, 42]
  arr=[8,4,23,42,16,15]
  actual=merge_sort(arr)
  assert actual==expected

def test_merge_sort2():
  expected= [-2, 5, 8, 12, 18, 20]
  arr=[20,18,12,8,5,-2]
  actual=merge_sort(arr)
  assert actual==expected


def test_merge_sort3():
  expected= [5, 5, 5, 7, 7, 12]
  arr=[5,12,7,5,5,7]
  actual=merge_sort(arr)
  assert actual==expected

def test_merge_sort4():
  expected= [2,3,5,7,11,13]
  arr=[2,3,5,7,13,11]
  actual=merge_sort(arr)
  assert actual==expected
