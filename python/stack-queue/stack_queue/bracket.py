from typing import Counter
from stack_queue.stack_queue import Stack

def validate_brackets(string):
  ls=[]
  open=Stack()
  for i in string:
    if i in ["(", "{", "[" ,")", "}", "]"]:
      ls.append(i)
  print(ls)

  for i in ls:
    if i in ["(", "{", "["]:
      open.push(i)
    else:
      if open.is_empty():
        return False
      else:
        check=open.pop()
        if check =="{":
          if i != "}":
            return False
        elif check == '[':
          if i != ']':
            return False
        elif check== '(':
          if i !=')':
            return False
  return True


# if __name__ == "__main__":
#     string = "(){}[[]]"

# print(validate_brackets(string))

