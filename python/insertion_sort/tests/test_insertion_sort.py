from insertion_sort import __version__
from insertion_sort.insertion_sort import insertion_sort

def test_version():
    assert __version__ == '0.1.0'


def test_insertion_sort1():
  expected= [4, 8, 15, 16, 23, 42]
  arr=[8,4,23,42,16,15]
  actual=insertion_sort(arr)
  assert actual==expected

def test_insertion_sort2():
  expected= [-2, 5, 8, 12, 18, 20]
  arr=[20,18,12,8,5,-2]
  actual=insertion_sort(arr)
  assert actual==expected


def test_insertion_sort3():
  expected= [5, 5, 5, 7, 7, 12]
  arr=[5,12,7,5,5,7]
  actual=insertion_sort(arr)
  assert actual==expected

def test_insertion_sort4():
  expected= [2,3,5,7,11,13]
  arr=[2,3,5,7,13,11]
  actual=insertion_sort(arr)
  assert actual==expected
