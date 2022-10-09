import time
#Intro message
#print("""
#
#░██╗░░░░░░░██╗░█████╗░██████╗░██╗░░░░░██████╗░
#░██║░░██╗░░██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗
#░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░░░░██║░░██║
#░░████╔═████║░██║░░██║██╔══██╗██║░░░░░██║░░██║
#░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║███████╗██████╔╝
#░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
#""")
#time.sleep(1)
#print("""
#░█████╗░███████╗
#██╔══██╗██╔════╝
#██║░░██║█████╗░░
#██║░░██║██╔══╝░░
#╚█████╔╝██║░░░░░
#░╚════╝░╚═╝░░░░░
#""")
#time.sleep(1)
#print("""
#██████╗░██╗░░░██╗██████╗░██████╗░██╗░░░░░███████╗░██████╗
#██╔══██╗██║░░░██║██╔══██╗██╔══██╗██║░░░░░██╔════╝██╔════╝
#██████╦╝██║░░░██║██████╦╝██████╦╝██║░░░░░█████╗░░╚█████╗░
#██╔══██╗██║░░░██║██╔══██╗██╔══██╗██║░░░░░██╔══╝░░░╚═══██╗
#██████╦╝╚██████╔╝██████╦╝██████╦╝███████╗███████╗██████╔╝
#╚═════╝░░╚═════╝░╚═════╝░╚═════╝░╚══════╝╚══════╝╚═════╝░""")
#time.sleep(1)
#Place class
def help_list():
    print("""
    ALL INSTRUCTIONS HERE
    eat - 
    sleep -
    go -
    energy - 
    where - 
    xp -
    items - 
    """)

class Place:
    locations = []
    def __init__(self, name, short_name, terrain, company):
        self.name = name
        self.short_name = short_name
        self.terrain = terrain
        self.company = company
        Place.locations.append(self.short_name)
    def go_to(self):
        if self == Bubbles.current_place:
            print("You are already at {}".format(self.name))
        else:
            if Bubbles.energy < 2:
                print("You don't have enough energy to go anywhere right now")
            else:
                if Bubbles.leash == True:
                    Bubbles.current_place = self
                    if self.terrain == "Beach":
                        Bubbles.beach_count += 1
                    else:
                        pass
                    Bubbles.energy += -2
                    if self not in Bubbles.places_been:
                        (Bubbles.places_been).append(self)
                        Bubbles.XP += 2
                    else:
                        pass
                    print("You are now at {}".format(self.name))
                else:
                    if "Leash" not in Bubbles.items:
                        print("You don't have a leash! You can't go there yet. Have a look around")       
                    else:
                        print("You can't change location without your leash on")
#Create Place instances
Snowdon = Place("Snowdon Mountain", "Snowdon", "Mountain", ["Ma", "Da"])
Bournemouth = Place("Bournemouth beach", "Bournemouth", "Beach", ["Ma", "Da", "Cait", "Colleen"])
Widemouth = Place("Widemouth Beach", "Widemouth", "Beach", ["Ma", "Da", "George"])
Pistyll = Place("Pistyll Waterfall", "Pistyll", "Waterfall", ["Ma", "Da"])
Van = Place("the Van", "Van", "inside", [])
Home = Place("your Home", "Home", "inside", [])
Garden = Place("the Garden", "Garden", "outside", [])
#current_place = Home
#Items class
class Items:
    def __init__(self, name, item_type):
        self.name = name
        self.type = item_type
#Cat class
class Cat:
    def __init__(self, name, gender, current_place):
        self.name = name
        self.energy = 10
        self.XP = 2
        self.max_XP: 50
        self.items = []
        self.currently_wearing = [] 
        self.gender = gender
        self.current_place = current_place
        self.places_been = [Home]
        self.miles = 0
        self.beach_count = 0 
        self.leash = False
        self.swimmer = False
        self.trunks_wet = False
        #for not repeating tasks
        self.kitchen = False
        self.garden_encounter = False
        self.jacket = False
        self.climb = False
        self.bouy = False
        self.waterfall = False
        self.dog_fight = False
        print("Welcome to the World {}!".format(self.name))
    def __repr__(self):
        return "You are {name} the Cat, you have {energy} energy and and {XP}XP".format(name=self.name, energy=self.energy, XP=self.XP)
    def sleep(self):
        if self.energy == 20:
            print("You're not tired!")
        elif self.current_place == Van or self.current_place == Home:
            self.energy = 20
            print("Zzzz")
            print("Energy levels now 20/20")
        else:
            print("You can only sleep in a safe place!")
    def eat(self):
        if self.energy < 17:
            self.energy += 3
            print("Yum! Your energy levels are {}/20".format(self.energy))
        elif self.energy == 20:
            print("You're full!")
        else:
            self.energy = 20
            print("Yum! Your energy levels are {}/20".format(self.energy))
    #Snowdon walk function
    def walk(self):
        if self.energy < 2:
            print("You need to eat something!")
        else:
            Bubbles.miles += 1
            Bubbles.energy += -2
            print("You have walked {}= out of 9 miles".format(Bubbles.miles))

def going():
            print("Go where?")
            go_where = input()
            if go_where == "locations":
                print(Place.locations)
            elif go_where in Place.locations:
                if go_where != "Garden" and go_where != "Home":
                    if Bubbles.leash == False:
                        (globals()[go_where]).go_to()
                    else:
                        if Bubbles.XP < 7:
                            print("You need at least 7XP to leave KM Way!")
                        else:
                            if Bubbles.current_place != Van:
                                if go_where == "Van":
                                    if Bubbles.trunks_wet == False:
                                        (globals()[go_where]).go_to()
                                    else:
                                        print("You can't get in there with wet trunks - take them off")
                                elif Bubbles.current_place == Home and go_where == "Garden":
                                    (globals()[go_where]).go_to()
                                elif Bubbles.current_place == Garden and go_where == "Home":
                                    (globals()[go_where]).go_to()
                                else:
                                    print("You need to get there somehow!")
                            else:
                                if go_where == "Van":
                                    (globals()[go_where]).go_to()
                                else:
                                    print("Road trip...")
                                    (globals()[go_where]).go_to()
                else:
                    (globals()[go_where]).go_to()
            elif go_where == "stay":
                print("Ain't going nowhere")
            else:
                print("Try again. Check places with \"locations\" or \"stay\" where you are.")

def explore():
            if Bubbles.current_place == Home:
                at_Home= True
                while at_Home:
                    print("Do you want to look in the \"bedroom\", \"bathroom\", or \"kitchen\"?")
                    go_home = input()
                    if go_home == "bedroom":
                        print("They've hidden the toys behind the TV! No fair.")
                    elif go_home == "bathroom":
                        print("My eyes! They sting! Let's try somewhere else")
                    elif go_home == "kitchen":
                        if Bubbles.kitchen == False:
                            print("Food! and a leash! Nice.")
                            Bubbles.eat()
                            Bubbles.items.append("Leash")
                            print("Let's try the Garden again")
                            Bubbles.kitchen = True
                            at_Home= False
                        else:
                            print("Nothing new here")
                    else: 
                        print("Not quite")
            if Bubbles.current_place == Garden:
                at_Garden = True
                while at_Garden:
                    print("Do you want to look in the \"grass\" or on the \"patio\"?")
                    go_garden = input()
                    if go_garden == "grass":
                        print("Wow! I love sitting here! What a spot.")
                    if go_garden == "patio":
                        patio = True
                        while patio:
                            if Bubbles.garden_encounter == False:
                                print("There's two cats up here! Do you want to \"fight\" or \"sniff\" their bum?")
                                fight_sniff = input()
                                if fight_sniff == "fight":
                                    Bubbles.energy += -6
                                    Bubbles.XP += +5
                                    print("That was hard! You've asserted your dominance and gained XP!")
                                    print("You have {xp}XP".format(xp=Bubbles.XP))
                                    print("You have {}/20 energy".format(Bubbles.energy))
                                    Bubbles.garden_encounter = True
                                    patio = False
                                    at_Garden = False
                                elif fight_sniff == "sniff":
                                    Bubbles.energy += -2
                                    Bubbles.XP += +5
                                    print("Ummm")
                                    print("I guess it worked? You've made two friends and gained XP!")
                                    print("You have {xp}XP".format(xp=Bubbles.XP))
                                    print("You have {}/20 energy".format(Bubbles.energy))
                                    Bubbles.garden_encounter = True
                                    patio = False
                                    at_Garden = False
                                else:
                                    print("Not quite")
                            else:
                                print("Nothing new here")
                                patio = False
                        at_Garden = False
            if Bubbles.current_place == Van:
                if Bubbles.jacket == False:
                    in_Van = True
                    while in_Van:
                        print("They don't like you looking around here too much!")
                        print("*Takes da's 1000 down himilayan North Face jacket*")
                        Bubbles.items.append("Jacket")
                        Bubbles.jacket = True
                        in_Van = False
                else:
                    print("Nothing new here")
            if Bubbles.current_place == Snowdon:
                if Bubbles.climb == False:
                    at_Snowdon = True
                    while at_Snowdon:
                        print("Wow that's a 9 mile \"walk\"")
                        if "Jacket" in Bubbles.currently_wearing:
                            print("Good thing you are wearing your jacket! Lets get going")
                            print("Lets get \"walk\"ing, or \"eat\" something")
                            while Bubbles.miles < 9:
                                start_walking = input()
                                if start_walking == "walk":
                                    if Bubbles.miles < 9:
                                        Bubbles.walk()
                                    if Bubbles.miles == 9:
                                        print("Wow! What a view!!")
                                        print("Someone left their... swimming trunks up here??")
                                        Bubbles.items.append("Trunks")
                                        Bubbles.XP += 5
                                        print("You have {xp}XP".format(xp=Bubbles.XP))
                                        Bubbles.climb = True
                                        at_Snowdon = False
                                elif start_walking == "eat":
                                    Bubbles.eat()
                                else:
                                    print("Not quite")
                        else:
                            print("You'll need to be wearing something warm to go up there!")
                else:
                    print("You've aleady climbed this")
            if Bubbles.current_place == Bournemouth:
                if Bubbles.bouy == False:
                    at_Bournemouth = True
                    while at_Bournemouth:
                        if Bubbles.beach_count < 2:
                            print("It's your first time at the beach! The sand is too scary to leave the bag!")
                            at_Bournemouth = False
                        else:
                            if "Trunks" in Bubbles.currently_wearing:
                                print("The water looks lovely! Lets go for a \"swim\"")
                                swim = input()
                                if swim == "swim" and Bubbles.energy >= 5:
                                    print("You're a better swimmer than your ma! You reached the bouy!")
                                    Bubbles.energy += -5
                                    Bubbles.XP += 5
                                    Bubbles.swimmer = True
                                    Bubbles.trunks_wet = True
                                    Bubbles.bouy = True
                                    print("You have {}/20 energy".format(Bubbles.energy))
                                    print("You have {xp}XP".format(xp=Bubbles.XP))
                                    at_Bournemouth = False
                                elif swim == "swim" and Bubbles.energy < 5:
                                    print("You won't be able to get far with {}/20 energy".format(Bubbles.energy))
                                    at_Bournemouth = False
                            else:
                                print("You can't swim without a pair of trunks!")
                                at_Bournemouth = False
                else:
                    print("You've already swum to the bouy")
                    at_Bournemouth = False
            if Bubbles.current_place == Widemouth:
                at_Widemouth = True
                while at_Widemouth:
                    if Bubbles.beach_count < 2:
                        print("It's your first time at the beach! The sand is too scary to leave the bag!")
                        at_Widemouth = False
                    else:
                        if Bubbles.dog_fight == False:
                            print("You are a lot more confident on the sand this time!")
                            print("A ratty looking dog runs up to you!")
                            if Bubbles.XP > 20:
                                print("Me-ow! You showed him who's boss!")
                                print("Now \"climb\" on that rock to assert your dominance!")
                                climb_rock = input()
                                if climb_rock == "climb":
                                    print("ItS tHe CiRcLe Of LiFe!!")
                                    Bubbles.XP += 5
                                    print(("You have {xp}XP".format(xp=Bubbles.XP)))
                                    Bubbles.dog_fight = True
                                    at_Widemouth = False
                            else:
                                print("Not enough XP to fight it, you run back in the bag")
                        else:
                            print("You're already the Lion King")
                            at_Widemouth = False
            if Bubbles.current_place == Pistyll:
                if Bubbles.waterfall == False:
                    at_Pistyll = True
                    while at_Pistyll:
                        print("It's so high up here! But you're stuck on one side of the river")
                        print("You can \"swim\" to the other side for a better view!")
                        go_swim = input()
                        if go_swim == "swim":
                            if Bubbles.swimmer == False:
                                print("You should probably practice swimming somewhere else first")
                                at_Pistyll = False
                            else:
                                if "Trunks" in Bubbles.currently_wearing:
                                    print("Good thing you've got your trunks on!")
                                    print("Splash splash")
                                    print("What a beautiful sight")
                                    Bubbles.waterfall = True
                                    at_Pistyll = False
                                else:
                                    print("You need your trunks!")
                                    at_Pistyll = False
                        else:
                            print("Not quite")
                            at_Pistyll = False
                else:
                    print("You've already been up here")
                pass

def wearing():
            print("What item?")
            what_item = input()
            if what_item not in Bubbles.items:
                print("You don't own that!")
            else:
                if what_item in Bubbles.currently_wearing:
                    Bubbles.currently_wearing.remove(what_item)
                    if what_item == "Leash":
                        Bubbles.leash = False
                    if what_item == "Trunks":
                        Bubbles.trunks_wet = False
                    else:
                        pass
                    print("You've taken it off")
                else:
                    if len(Bubbles.currently_wearing) >= 2:
                        print("You can only wear two items at a time, take something off to put this on")
                    else:
                        Bubbles.currently_wearing.append(what_item)
                        if what_item == "Leash":
                            Bubbles.leash = True
                        else:
                            pass
                        print("That looks good on you!")
            wearing = False

print("Choose a gender: F or M or Other")

gendering = True
while gendering:
    gender = input()
    gender_phrase = {"M":"handsome boy", "F":"pretty girl", "Other":"gorgeous thing"}
    if gender in gender_phrase.keys():
        print("Meow! What are your owners going to call you, you {}?".format(gender_phrase[gender]))
        Bubbles = Cat(input(), gender, Home)
        gendering = False
    else:
        print("Please select from the available options")

print("That car journey home really drained your energy!")
intro = False
while intro:
    intro_eat = True
    while intro_eat:
        print("You can type \"eat\" at any point to gain 3 energy points! Try it now")
        first_eat = input()
        if first_eat == "eat":
            Bubbles.eat()
            intro_eat = False
        elif first_eat == "skip":
            intro = False
        else:
            print("Not quite")    
    intro_sleep = True
    while intro_sleep:
        print("If you are in a safe location, you can type \"sleep\" to regain full health. Try it now, while you're at home")
        first_sleep = input()
        if first_sleep == "sleep":
            Bubbles.sleep()
            intro_sleep = False
        else:
            print("Not quite")
    intro_location_list = True
    while intro_location_list:
        print("You can change location. To see available locations, type \"locations\"")
        loc_list = input()
        if loc_list == "locations":
            print(Place.locations)
            intro_location_list = False
        else:
            print("Not quite")
    intro_location_change = True
    while intro_location_change:
        print("Lets try go to the garden. Type \"go\"")
        first_loc_change = input()
        if first_loc_change == "go":
            intro_location_change = False
            intro_loc_select= True
            while intro_loc_select:
                print("Now type \"Garden\"")
                first_loc_select = input()
                if first_loc_select == "Garden":
                    (globals()[first_loc_select]).go_to()
                    print("Ah, well")
                    print("Note: you lose 2 energy points when you move, however when going to a new place you gain 2XP")
                    intro_loc_select = False
                else:
                    print("Not quite")
        else:
            print("Not quite")
        print("Lets get started")
        print("type \"help\" at any point to get instructions")
        intro = False
doing_stuff = True
#for sake of speed:
#Bubbles = Cat("Bubbles", "M", Home)
Bubbles.items.append("Leash")
Bubbles.items.append("Jacket")
Bubbles.items.append("Trunks")
Bubbles.currently_wearing.append("Leash")
Bubbles.currently_wearing.append("Jacket")
Bubbles.leash = True
Bubbles.XP = 20
while doing_stuff:
    if Bubbles.kitchen == True and Bubbles.garden_encounter == True and Bubbles.bouy == True and Bubbles.dog_fight == True and Bubbles.climb == True and Bubbles.waterfall == True and Bubbles.jacket == True:
        print("That's all for now folks!")
        doing_stuff = False
    else:
        doing = input()
        if doing == "eat":
            Bubbles.eat()
        elif doing == "sleep":
            Bubbles.sleep()
        elif doing == "go":
            going() 
        elif doing == "explore":
            explore()
        elif doing == "wear":
            wearing()
        elif doing == "energy":
            print("You have {}/20 energy".format(Bubbles.energy))
        elif doing == "where":
            print("You are currently at {}".format((Bubbles.current_place).name))
        elif doing == "xp":
            print("You have {xp}XP".format(xp=Bubbles.XP))
        elif doing == "items":
            print(Bubbles.items)
            print("Type \"wear\" to put on or take off items")
        elif doing == "help":
            help_list()

        
#double check the XP for fighting at widemouth is realistic
#add winner text
#help list better
#clean up intro