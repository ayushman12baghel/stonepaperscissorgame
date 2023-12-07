import random
x=input("Do you want to play (yes or no): ")
def game():
  user=input("Choose between rock, paper and scissor: ")
  user=user.lower()
  l=["rock","paper","scissor"]
  comp=random.choice(l)
  print("\n You chose %a and Computer chose %a"%(user,comp))
  if comp==user:
    print("Tie")
  elif comp=="rock" and user=="paper":
    print("You won")
  elif comp=="paper" and user=="scissor":
    print("You won")
  elif comp=="scissor" and user=="rock":
    print("You won")
  else:
    print("You lost")
for i in x:
  
  if x=="yes":
    game()
    x=input("Do you want to play (yes or no): ")
  elif x=="no":
   print("thanks for answering")