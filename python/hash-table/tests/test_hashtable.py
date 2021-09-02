from hash_table.hash_table import HashTable



def test_add_and_get():
  hash=HashTable()
  hash.add('1','Ruba')
  assert hash.get('1') == 'Ruba'

def test_get_empty():
  hash=HashTable()
  assert hash.get('1') == None

def test_contains():
  hash=HashTable()
  hash.add('1','Ruba')
  assert hash.contains('1') == True



def test_not_contains():
  hash=HashTable()
  assert hash.contains('1') == False

def test_hash():
  hash=HashTable(10)
  actual= hash.hash('hi')
  expected= 5
  assert actual == expected
