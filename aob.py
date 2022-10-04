import time
class Cat:
    def __init__(self, name):
        self.name = name
        self.bravery = 0
        self.explore = 0
        self.vac = False
        self.friends = []
    def become_friends(self, other):
        self.friends.append(other)
    def vaccinate(self):
        self.vac = True

print("Meow! What are your owners going to call you, you handsome boy?")
cat_name = input()
Bubbles = Cat(cat_name)
print("""Welcome to the World {name}!
What strange looking owners you have!""".format(name = Bubbles.name))
time.sleep(1)
def first_choice(go_back=0):
    print("Do you want to say \"hello\" or \"explore\" the room?")
    option_1 = input()
    if option_1 == "hello":
        Bubbles.bravery += 10
        print("Why hello! Very brave of you!")
        print("10 bravery points gained :)")        
    elif option_1 == "explore":
        Bubbles.explore += 10
        print("Wow. That room really is a room!")
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
def second_choice():
    print("Do you want to \"run\" or be a \"good\" boy?")
    option_2 = input()
    if option_2 == "run":
        Bubbles.bravery += -5
        print("What a pussy-cat!")
        print("You lost 5 bravery points.")
    elif option_2 == "good":
        Bubbles.bravery += 5
        Bubbles.vaccinate()
        print("Ouch! That was a vaccine.")
        print("Bad news is that was sore, good news is you've gained 5 bravery points!")
    elif option_2 == "return":
        first_choice()
    else:
        print("Sorry, that's not an option.")
        second_choice()
second_choice()
print("Broom broom! You're in a van!")
print("mo0o0o0o0o")
def third_choice():
    print("What was that?? Do you want to \"look\" for the sound, or go back to \"sleep\"")
    option_3 = input()
    if option_3 == "look":
        Bubbles.become_friends("Highland coo")
        print("Wow! You are now friends with a Highland coo!")
    elif option_3 == "sleep":
        Bubbles.explore += -5
        print("Boo.")
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
    print("Wow! What a big bird! I think it likes you!")
    Bubbles.become_friends("Big Bird")
elif Bubbles.vac == False:
    print("Those humans have parked up by some grass by the beach, too bad youre not vacinated!")
time.sleep(2)
print("*crashhhhhh*")
time.sleep(2)
print("Wow! Thats a lot of water!")
if Bubbles.bravery >10:
    print("You're brave! Thats a whole ocean buddy!")
else:
    print("Ew! The sand feels funny on my footsies! Bun that!")




