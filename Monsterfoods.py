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

my_monster = Monster('Spooky Snack')
my_monster.speak()
my_monster.eat('food')
