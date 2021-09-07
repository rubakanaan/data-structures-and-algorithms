from hash_table.left_join import left_join
from hash_table.hash_table import HashTable


def test_left_join():
  hashtb1=HashTable()
  hashtb1.add('fond','enamored')
  hashtb1.add('wrath','anger')
  hashtb1.add('diligent','employed')
  hashtb1.add('outift','grab')
  hashtb1.add('guide','usher')

  hashtb2=HashTable()
  hashtb2.add('fond','averse')
  hashtb2.add('wrath','delight')
  hashtb2.add('diligent','idle')
  hashtb2.add('guide','follow')
  hashtb2.add('flow','jam')

  expectd= [['fond', 'enamored', 'averse'], ['diligent', 'employed', 'idle'], ['outift', 'grab', 'NULL'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight']]
  actual= left_join(hashtb1,hashtb2)
  assert expectd == actual

def test_left_join_2():
  hashtb1=HashTable()
  hashtb1.add('fond','enamored')
  hashtb1.add('wrath','anger')
  hashtb2=HashTable()
  hashtb2.add('fond','averse')
  hashtb2.add('wrath','delight')
  hashtb2.add('diligent','idle')
  hashtb2.add('guide','follow')
  hashtb2.add('flow','jam')

  expectd= [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight']]
  actual= left_join(hashtb1,hashtb2)
  assert expectd == actual

def test_left_join_empty():
  hashtb1=HashTable()
  hashtb2=HashTable()
  expectd= []
  actual= left_join(hashtb1,hashtb2)
  assert expectd == actual
