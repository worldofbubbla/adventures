import time
print("""

░██╗░░░░░░░██╗░█████╗░██████╗░██╗░░░░░██████╗░
░██║░░██╗░░██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗
░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░░░░██║░░██║
░░████╔═████║░██║░░██║██╔══██╗██║░░░░░██║░░██║
░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║███████╗██████╔╝
░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
""")
time.sleep(1)
print("""
░█████╗░███████╗
██╔══██╗██╔════╝
██║░░██║█████╗░░
██║░░██║██╔══╝░░
╚█████╔╝██║░░░░░
░╚════╝░╚═╝░░░░░
""")
time.sleep(1)
print("""██████╗░██╗░░░██╗██████╗░██████╗░██╗░░░░░███████╗░██████╗
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██║░░░░░██╔════╝██╔════╝
██████╦╝██║░░░██║██████╦╝██████╦╝██║░░░░░█████╗░░╚█████╗░
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██║░░░░░██╔══╝░░░╚═══██╗
██████╦╝╚██████╔╝██████╦╝██████╦╝███████╗███████╗██████╔╝
╚═════╝░░╚═════╝░╚═════╝░╚═════╝░╚══════╝╚══════╝╚═════╝░""")
time.sleep(1)
class Cat:
    def __init__(self, name):
        self.name = name
        self.bravery = 0
        self.explore = 0
        self.vac = False
        self.friends = []
        print("Welcome to the World {name}!".format(name = self.name))
    def __repr__(self):
      if len(self.friends) != 0:
        return "Your name is {name}, you have a bravery score of {bravery} and exploration score of {explore}. You're friends are the ".format(name=self.name, bravery=self.bravery, explore=self.explore) + " and the ".join(Bubbles.friends)
      else:
        return "Your name is {name}, you have a bravery score of {bravery} and exploration score of {explore}".format(name=self.name, bravery=self.bravery, explore=self.explore)
    def become_friends(self, other):
        self.friends.append(other)
    def vaccinate(self):
        self.vac = True
print("Meow! What are your owners going to call you, you handsome boy?")
cat_name = input()
Bubbles = Cat(cat_name)
print
time.sleep(1)
print("What strange looking owners you have!")
time.sleep(1)
def first_choice(go_back=0):
    print("Do you want to say \"hello\" or \"explore\" the room?")
    option_1 = input()
    if option_1 == "hello":
        Bubbles.bravery += 10
        print("Why hello! Very brave of you!")
        time.sleep(1)
        print("10 bravery points gained :)")        
    elif option_1 == "explore":
        Bubbles.bravery += 10
        print("Wow. That room really is a room!")
        time.sleep(1)
        print("10 explorer points gained :)")
    else:
        print("Sorry, that's not an option.")
        first_choice()
first_choice()
time.sleep(1)
print("Oh goodness, you're in a bag!")
time.sleep(1)
print("*darkness*")
time.sleep(3)
print("That's a big sword!")
time.sleep(1)
def second_choice():
    print("Do you want to \"run\" or be a \"good\" boy?")
    option_2 = input()
    if option_2 == "run":
        Bubbles.bravery += -5
        print("What a pussy-cat!")
        time.sleep(1)
        print("You lost 5 bravery points.")
    elif option_2 == "good":
        Bubbles.bravery += 5
        Bubbles.vaccinate()
        print("Ouch! That was a vaccine.")
        time.sleep(1)
        print("Bad news is that was sore, good news is you've gained 5 bravery points!")
    elif option_2 == "return":
        first_choice()
    else:
        print("Sorry, that's not an option.")
        second_choice()
second_choice()
time.sleep(2)
print("Broom broom! You're in a van!")
time.sleep(1)
print("mo0o0o0o0o")
time.sleep(1)
def third_choice():
    print("What was that?? Do you want to \"look\" for the sound, or go back to \"sleep\"")
    option_3 = input()
    if option_3 == "look":
        Bubbles.become_friends("Highland coo")
        print("Wow! You are now friends with a Highland coo!")
    elif option_3 == "sleep":
        Bubbles.bravery += -5
        print("Boo.")
        time.sleep(1)
        print("You lost 5 explore points")
    elif option_3 == "return":
        second_choice()
    else:
        print("Sorry, that's not an option.")
        third_choice()
third_choice()
time.sleep(2)
if Bubbles.vac == True:
    print("Those humans have parked up by some grass by the beach, good thing youre vacinated!")
    time.sleep(1)
    print("Wow! What a big bird! I think it likes you!")
    Bubbles.become_friends("Big Bird")
elif Bubbles.vac == False:
    print("Those humans have parked up by some grass by the beach, too bad youre not vacinated!")
time.sleep(2)
print("*crashhhhhh*")
time.sleep(3)
print("Wow! Thats a lot of water!")
time.sleep(1)
if Bubbles.bravery >= 15:
    print("You're a little explorer aren't you!")
    time.sleep(1)
    print("*pitter patter*")
    time.sleep(1)
    print("*arrive at the ocean*")
    time.sleep(1)
    print("You're brave! Thats a whole ocean buddy!")
else:
    print("You're not the most adventurous chap")
    time.sleep(1)
    print("Ew! The sand feels funny on my footsies! Bun that!")
time.sleep(2)
def fourth_choice():
  print("BRRrRooOmmmmmmmmmmmm.")
  time.sleep(1)
  print("OH no, the vans broken! Do you know a mechanic? Type the name if you do or say \"no\"")
  option_4 = input()
  if option_4 == "no":
    print("That's a shame, da will have to pay through the nose for this!")
  else:
    print("Thank goodness! {} will get it done!".format(option_4))
time.sleep(2)
fourth_choice()
time.sleep(2)
print("SNOWDON")
time.sleep(2)
print("That's the tallest waterfall in the UK! And you're at the top of it, how beautiful")
time.sleep(1)
print("Isn't your ma just the best!!")
time.sleep(3)
def fifth_choice():
  print("Bubbles is trying to joyride the van!!")
  print("Quick! Press entire exactly ten times to stop him")
  input()
  input()
  input()
  input()
  input()
  input()
  input()
  input()
  input()
  input()
  print("PHew!! He doesn't have a license!")
fifth_choice()
time.sleep(1)
print("What a life!")
time.sleep(1)
print(Bubbles)
time.sleep(2)
print("Until next time...")
