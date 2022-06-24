import random
rock= """
         ___
------' (___)
        (____)
        (____)
        (____)
------._(___)
    """
    
paper="""
      _____
-----'  ____)__
         ______)
         _______)
         ______)
---.________) 
  """
         
scissors="""
      _____
-----'(____)___
          ______)
          _______)
        (___)
---.___(___) 
"""       

# print(rock)
# print(paper)
# print(scissors)



list=[rock,paper,scissors]
user=int(input("what do you choose ? type 0 Rock,1 for Paper or 2 for Scissors.\n"))
print("swari")
print(list[user])
choice=random.randint(0,2)
print(" sayjal ")
print(list[choice])

if user==0 and choice==2:
    print("you are  wins!")
elif choice==0 and user :
    print("you lose")
elif choice > user:
    print(" you are lose")
elif user > choice:
    print("you win")
elif choice==user:
    print("it's a draw")
else:
    print("you type an invalid number, you loss!")