from sys import exit

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        scene = self.scene_map.opening_scene()
        next_scene_name = scene.enter()

        while (True):
            if (next_scene_name == 'end'):
                print 'You are amazing. Thanks for playing.'
                exit(0)
            else:
                scene = self.scene_map.next_scene(next_scene_name)
                next_scene_name = scene.enter()

class Death(Scene):

    def enter(self):
        print 'I met a Gothon once that played it better than you :/'
        return 'end'

class CentralCorridor(Scene):

    def enter(self):
        print """
        You're in the space ship central corridor.
        There's a Gothon here! What do you do?
        1 - Tell a joke
        2 - Run!
        3 - Punch the alien cause you are a man!
        """
        answer = raw_input("> ")

        while (True):
            if (answer == "1"):
                print """
                You tell that one you heard from your granpa.
                The Gothon laugh his ass off and you run through him.
                """
                return 'laser_weapon_armory'
            elif (answer == '2'):
                print 'The Gothon shot you with his laser gun!'
                return 'death'
            elif (answer == '3'):
                print 'The Gothon ate your hand!'
                return 'death'
            else:
                print "Just type the alternative's number son"

class LaserWeaponArmory(Scene):

    def enter(self):
        print """
        You're in the laser weapon armory.
        You know there is a neutron bomb here, but it is locked with a keypad.
        What is the code
        1 - '1' because it is the number of Gothon's you've seen so far
        2 - '69' because the security guy has dirty mind
        3 - '123' because everyone is lazy around here
        """
        answer = raw_input("> ")

        while (True):
            if (answer == "1"):
                print 'Are you moron?'
                answer = raw_input("> ")
            elif (answer == '2'):
                print 'He does have a dirty mind but not that far'
                answer = raw_input("> ")
            elif (answer == '3'):
                print 'Yep. Lazy lazy lazy.'
                return 'the_bridge'
            else:
                print "Just type the alternative's number son"
                answer = raw_input("> ")

class TheBridge(Scene):

    def enter(self):
        print """
        You're at the bridge that goes to the pod's room.
        But wait! There is a gothon here!
        What do you do?
        1 - It's only one. I can take him down.
        2 - Tell another joke!
        3 - Turn on the bomb and place it!
        """
        answer = raw_input("> ")

        while (True):
            if (answer == "1"):
                print 'Gothons are two and a half meters tall with laser guns.'
                print "No, you can't take him down. You're dead :("
                return 'death'
            elif (answer == '2'):
                print "It seems this Gothon doesn't have a sense of humor."
                print "You're dead :("
                return 'death'
            elif (answer == '3'):
                print 'The Gothon ran away yelling something you do not understand.'
                return 'escape_pod'
            else:
                print "Just type the alternative's number son"

class EscapePod(Scene):

    def enter(self):
        print """
        You're at the pod's room.
        There are three pods in here.
        What do you do?
        1 - Take the red one that looks like a ferrari!
        2 - Take gray one that looks like an old nokia cell phone.
        3 - Just wear the space suit and jump out of the ship.
        """
        answer = raw_input("> ")

        while (True):
            if (answer == "1"):
                print "The pod is fast but you got caught by the explosion. You're dead :("
                return 'death'
            elif (answer == '2'):
                print "You got caught by the explosion but the pod is intact."
                print "These nokia things are undestructable."
                return 'end'
            elif (answer == '3'):
                print 'Now you are alone in the space until the oxigen ends :('
                return 'death'
            else:
                print "Just type the alternative's number son"

class Map(object):

    def __init__(self, start_scene):
        self.start_scene = start_scene
        self.scenes = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod(),
            'death': Death()
        }

    def next_scene(self, scene_name):
        return self.scenes[scene_name]

    def opening_scene(self):
        return self.scenes[self.start_scene]


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
