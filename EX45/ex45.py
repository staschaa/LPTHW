from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        return 'enter_game'

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()

class Enter(Scene):

    def enter(self):
        print "\n"
        print "You're on vacation with a couple of friends and for this nice"
        print "and sunny day you have planned a trip to a big theme park. All"
        print "of you are excited about a roller coaster ride and to win"
        print "a big price at the tombola. Besides you are looking forward to"
        print "a nice break at the food area and all in all a memorable"
        print "vacation day."
        # In the game you can navigate through the different activities at the
        # theme park while the game involes an engine that runs a map full of
        # them. Each scene will print out its own description when you enter it
        # and tell the engine what room to run next out of the Map.
        print "\n"
        print "At the entrance you have to buy the entry tickets. They are"
        print "personalized and you have to answer the salesman some personal"
        print "questions."
        print "\n"
        print "What's your name? ",
        name = raw_input("> ")
        print "How old are you?",
        age = raw_input("> ")
        print "How tall are you?",
        height = raw_input("> ")
        print "\n"
        print "Thank you %r, here is your ticket. Have a nice day!" % name
        print "\n"
        return 'action_game'
        # One other possibility: If you are under 18 years old or under 1.50
        # meters tall, you are not allowed to enter the theme park."

class Action(Scene):

    def enter(self):
        print "\n"
        print "Having all tickets, you guys are exited to have some action!"
        print "You and your friends are considering whether to ride a roller"
        print "coaster or try to win a big price at the tombola."
        print "\n"
        print "Do you prefer the roller coaster or the tombola?"
        print "\n"

        answer = raw_input("> ")

        if answer == "roller coaster":
            print "\n"
            print "You decide to ride a big looping roller coaster."
            return 'roller_coaster_game'

        elif answer == "tombola":
            print "\n"
            print "You make your way to the tombola."
            return 'tombola_game'

        else:
            print "\n"
            print "Please type in 'roller coaster' or 'tombola'."
            return 'action_game'

class Tombola(Scene):

    def enter(self):
        print "\n"
        print "Reaching the colorful blinking tombola tent you can choose"
        print "beween a blue, a green or a red tombola ticket."
        print "If you are lucky, there is the chance to win 1000 Dollar!"
        print "\n"
        print "Which color do you want to buy?"
        # Blue: you win some free drinks! Green: you loose! Red: you
        # win 1000 Dollar. Afterwards you need something to eat!"
        choice = raw_input("> ")

        if choice == "blue":
            print "\n"
            print "Luckily you won free drinks for you and your friends!"
            print "You go to the food area of the theme park to redeem your"
            print "coupons. On your way you pass the water ride which your"
            print "friends definately want to ride."
            return 'food_game'

        elif choice == "green":
            print "\n"
            print "Even though green is the color of hope you draw a BLANK!"
            print "You loose and out of the dissapointing mood you decide to"
            print "take a break at the food station. On your way you pass the"
            print "water ride which your friends definately want to ride."
            return 'food_game'

        elif choice == "red":
            print "\n"
            print "As you look at the tombola ticket, you first can't believe"
            print "your eyes ... on that litte red paper you read: FIRST"
            print "PRICE! Your friends and you freak out. You won 1000 Dollar!"
            print "To mark the occasion you all join in the idea to spend the"
            print "money on food. On your way to the food station, you pass the"
            print "water ride which your friends definately want to ride."
            return 'food_game'

        else:
            print "\n"
            print "Please type in either 'blue', 'green' or 'red'."
            return 'tombola_game'

class RollerCoaster(Scene):

    def enter(self):
        print "\n"
        print "Each train of the roller coaster has three wagons."
        print "\n"
        print "Do you and your friends want to sit in the first, second or"
        print "at the back in the third wagon?"
        # first and last wagon you will have a fun ride with a great view over
        # the park. The second wagon will have technical problems during the
        # ride and you are stucked upside down in a loop for half an hour. After
        # the problems are solved all of you want to go home."
        choice = raw_input("> ")

        if "first" in choice or "third" in choice:
            print "\n"
            print "All of you are highly overwhelmed by the great view over the"
            print "park you got during the ride. A lot of adrenaline flows"
            print "through your bodys. Everybody agrees to have a lunch break"
            print "now. On your way to the food station, you pass the water"
            print "ride which your friends definately want to ride."
            return 'food_game'


        else:
            print "\n"
            print "The belts get fasten and the ride begins. Suddenly your"
            print "wagon loses speed and you are stucked upside down in a loop"
            print "for half an hour. There are some technical problems with the"
            print "roller coaster. After the problems are solved all of you"
            print "want to go home. This vacation day is not what you expected."
            return 'end_game'

class Food(Scene):

    def enter(self):
        print "\n"
        print "Your friends are waiting in the queue for the water ride. Since"
        print "you don't want to get wet, you go and get some food for all of"
        print "you. Unfortunately you forgot what your friends wanted to eat"
        print "during the way to the food area. Now you have to guess what"
        print "their order was. At the food station you can buy either burger,"
        print "pizza, fries, waffles, candy or hot dogs."
        answer = "waffles"
        guess = raw_input("> ")
        guesses = 0

        while guess != answer and guesses < 2:
            print "\n"
            print "Nope that's not what they wanted. Try to remember what they"
            print "told you."
            guesses +=1
            guess = raw_input("> ")

        if guess == "waffles":
            print "\n"
            print "Nice! You rememer that you like to eat a big fat waffle with"
            print "a lot of chocolate sauce on it. When you finally bought the"
            print "waffles you see your friends arriving completely wet at the"
            print "food area. You bring the day to a close with a nice meal."
            print "What a fantastic day at the theme park!"
            return 'end_game'

        else:
            print "\n"
            print "You have made the wrong decision three times. As you finally"
            print "remember that you guys wanted to eat waffles, the food"
            print "station closes. No one of you get something to eat. Most of"
            print "the group is angry at you and they decide to go back to the"
            print "hotel and order food."
            return 'end_game'


class End(Scene):

    def enter(self):
        print "\n"
        print "After the happenings of the day you are going back to your"
        print "hotel."
        exit(1)


class Map(object):

    scenes = {
        'enter_game': Enter(),
        'action_game': Action(),
        'roller_coaster_game': RollerCoaster(),
        'tombola_game': Tombola(),
        'food_game': Food(),
        'end_game': End()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('enter_game')
a_game = Engine(a_map)
a_game.play()
