import re

def repeated_word(sentence):
  words_list=re.findall('[\w\']+',sentence)
  print(words_list)
  check_arr=[]
  for i in words_list:
    if i.lower() in check_arr:
      return i
    else :
      check_arr.append(i.lower())


if __name__=="__main__":
  print(repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))
