#Create superclass
# Set up class attribute, same
#set up instance attribute, different
#define method for speaking behavior, then eating behavior
#create an instance of MonsterFood
#call methods on new instances

class Monster(object):
    eats = 'food'
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name+ ' speaks')
    def eat(self, meal):
        if meal == self.eats:
            print('Yum!')
        else:
            print('Blech!')

my_monster = Monster('Spooky Snack')# Create superclass
# Set up class attribute, same
# set up instance attribute, different
# define method for speaking behavior, then eating behavior
# create an instance of MonsterFood
# call methods on new instances


class Monster(object):
    eats = 'food'

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' speaks')

    def eat(self, meal):
        if meal == self.eats:
            print('Yum!')
        else:
            print('Blech!')

#my_monster = Monster('Spooky Snack')
# my_monster.speak()
# my_monster.eat('food')

# set up a subclass of Monster and define its method


class FrankenBurger(Monster):
    eats = 'hamburger patties'

    def speak(self):
        print('My names is ' + self.name + 'Burger')

#my_frankenburger = FrankenBurger('Veggiesaurus')
# my_frankenburger.speak()
# my_frankenburger.eat('pickles')

# set up second monster


class CrummyMummy(Monster):
    eats = 'chocolate chips'

    def speak(self):
        print('My name is ' + self.name + 'Mummy')

#my_crummymummy = CrummyMummy('Chippy')
# my_crummymummy.speak()
# my_crummymummy.eat('cookies')

# set up third monster


class WereWatermelon(Monster):
    eats = 'watermelon juice'

    def speak(self):
        print('My name is Were ' + self.name)

#my_werewatermelon = WereWatermelon('Melons')
# my_werewatermelon.speak()
# my_werewatermelon.eat('juice')


monster_selection = input(
    'What kind of monster do you want to create? Select: frankenburger, crummymummy, or werewatermelon.')
monster_name = input('What do you want to name your monster?')
monster_meal = input('What will you feed your monster?')

if monster_selection == 'freankenburger':
    monster_type - FrankenBurger
elif monster_selection == 'crummymummy':
    monster_type = CrummyMummy
elif monster_selection == 'werewatermelon':
    monster_type = WereWatermelon
else:
    monster_type = Monster

my_monster = monster_type(monster_name)
my_monster.speak()
my_monster.eat(monster_meal)

my_monster.speak()
my_monster.eat('food')
