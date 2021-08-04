def isPalindrome(lnl):
    current=lnl.head

    ls=[]
    while current !=None:

        print(current.value)
        ls.append(current.value)
        current=current.next

    if ls[:]==ls[::-1]:
      return True
    else:
      return False
