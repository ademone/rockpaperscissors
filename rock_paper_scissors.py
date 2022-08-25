import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

allchoices = [rock, paper, scissors]
userinput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
#print(allchoices[0])
if userinput == 0:
    print("You selected Rock \n" + allchoices[0])
elif userinput == 1:
    print("You selected Paper \n" +allchoices[1])
else:
    print("You selected Scissors \n" +allchoices[2])

comprandselect = random.randint(0, 2)
if comprandselect == 0:
    print("Computer selected Rock \n" + allchoices[0])
elif comprandselect == 1:
    print("Computer selected Paper \n" + allchoices[1])
else:
    print("Computer selected Scissors \n" +allchoices[2])

if userinput == comprandselect:
    print("It's a draw")
elif userinput == 0 and comprandselect == 2:
    print("You won")
elif userinput == 1 and comprandselect == 0:
    print("You won")
elif userinput == 2 and comprandselect == 1:
    print("You won")
else:
    print("You lost")