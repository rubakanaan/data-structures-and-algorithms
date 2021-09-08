from hash_table.hash_table import HashTable


def left_join(hashtb1,hashtb2):
  result=[]
  keys=hashtb1.__dict__().keys()
  for key in keys :
    if hashtb2.contains(key):
      result.append([key,hashtb1.get(key),hashtb2.get(key)])
    else:
      result.append([key,hashtb1.get(key),'NULL'])
  return result

if __name__ == "__main__":
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
  print(left_join(hashtb1,hashtb2))
