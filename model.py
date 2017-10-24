import arcade.key
import arcade.sound
from random import randint



BLOCK_SIZE = 70
GRAVITY_CONSTANT = 9.81
FLIPDOWN = 0
FLIPUP = 1


class Model:
    def __init__(self, world, x, y, angle):
        self.world =  world
        self.x = x
        self.y = y
        self.angle = 0


class LeftFlipper(Model):
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.direction = FLIPDOWN
        self.angle = -30
        self.status = -1/2

    def switch_direction(self):
        if self.direction == FLIPDOWN:
            self.angle = 45
            self.direction = FLIPUP
            self.status = -1.5
        else:
            self.angle = -30
            self.direction = FLIPDOWN
            self.status = -1/2



class RightFlipper:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.direction = FLIPDOWN
        self.angle = 30
        self.status = -1/2

    def switch_direction(self):
        if self.direction == FLIPDOWN:
            self.angle = -45
            self.direction = FLIPUP
            self.status = -1.5
        else:
            self.angle = 30
            self.direction = FLIPDOWN
            self.status = -1/2




class LeftBumper:
    def __init__(self,world, x,y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

class RightBumper:
    def __init__(self,world, x,y, angle ):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

class MidBumper:
    def __init__(self, world, x, y, angle):
        self. world = world
        self.x = x
        self.y = y
        self.angle = 0




class Ball:
    def __init__(self,world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
        self.delta_x = 1.5 #actual 2
        self.delta_y = -0.85 #actual -0.85


    def update(self, delta):
        deadSound = arcade.sound.load_sound('sounds/dead.mp3')


        #Initiate gravity
        self.x += self.delta_x
        self.y += self.delta_y *GRAVITY_CONSTANT

        if 0.8 >self.delta_y > -0.8:
            self.delta_y = -0.85

        if self.delta_y > 2:
            self.delta_y *= 0.25
        elif self.delta_x < -2:
            self.delta_y *= 0.25

        if self.delta_x > 3:
            self.delta_x = 2
        elif self.delta_x < -3:
            self.delta_X = -2
        elif self.delta_x == 0:
            self.delta_x = 2

        #Check Wall hit
        if self.x > 700 - 32:
            self.delta_x *= randint(-2,-1)
        elif self.x < 32:
            self.delta_x *= randint(-2,-1)
        elif self.y > 700 - 32:
            self.delta_y *= randint(-2,-1)
        elif self.y < 32:
            arcade.sound.play_sound(deadSound)
            self.x = 750
            self.y = 750


        #Check slope hit
        if(self.x < 240) or (self.x > 462):
            if self.y < 160+16:
                self.delta_y *= -1
                self.delta_x *= randint(-1,1)




    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)
        #return (self.x > other.x - hit_size) and (self.y > other.y - hit_size)







class Wall:
    def __init__(self,world):
        self.world = world
        self.x = 0
        self.y = 0
        self.list = []
        self.createmap()

    def createmap(self):
        y = 700
        for x in range(70, self.world.width, BLOCK_SIZE):
            self.list.insert(len(self.list),(x,y))

        x = 0
        for y in range(70, self.world.height, BLOCK_SIZE):
            self.list.insert(len(self.list),(x,y))

        x = 700
        for y in range(70, self.world.height, BLOCK_SIZE):
            self.list.insert(len(self.list),(x,y))




class Slope:
    def __init__(self,world):
        self.world = world
        self.x = 0
        self.y = 0
        self.list = []
        self.createmap()

    def createmap(self):
            x = 446
            for y in range(150, 160, 1):  #Actual 150, 350, 32
                x += 30
                self.list.insert(len(self.list),(x,y))

            x = 256
            for y in range(150, 160, 1):
                x -= 30
                self.list.insert(len(self.list),(x,y))





class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score = 0

        self.wall = Wall(self)
        self.slope = Slope(self)
        #SET UP THE FUCKING ANGLE FFS PLS
        self.leftFlipper = LeftFlipper(self, 286, 150, -90)
        self.rightFlipper = RightFlipper(self, 416, 150, -90)
        self.leftBumper = LeftBumper(self, 175, 450, 0)
        self.rightBumper = RightBumper(self, 525, 450, 0)
        self.midBumper = MidBumper(self, 350, 550, 0)
        self.ball = Ball(self, 350, 400, 0)

        #backgroundSound = arcade.sound.load_sound('sounds/test.mp3')
        #arcade.sound.play_sound(backgroundSound)



    def update(self, delta):
        hitSound = arcade.sound.load_sound('sounds/hit.mp3')
        flipSound = arcade.sound.load_sound('sounds/flipper.mp3')
        self.ball.update(delta)


        if self.ball.hit(self.leftBumper, 32):
            self.ball.delta_x = (self.ball.delta_x * randint(-1,1))*randint(1,3)
            self.ball.delta_y = (self.ball.delta_y * -2)
            self.score += 100
            arcade.sound.play_sound(hitSound)

        if self.ball.hit(self.midBumper, 32):
            self.ball.delta_x = (self.ball.delta_x * randint(-1,1))*randint(1,3)
            self.ball.delta_y = (self.ball.delta_y * -2)
            self.score += 200
            arcade.sound.play_sound(hitSound)

        if self.ball.hit(self.rightBumper, 32):
            self.ball.delta_x = (self.ball.delta_x * randint(-1,1))*randint(1,3)
            self.ball.delta_y = (self.ball.delta_y * -2)
            self.score += 100
            arcade.sound.play_sound(hitSound)

        if self.ball.hit(self.leftFlipper, 33.75): #67.5 is the biggest hit box
            self.ball.delta_y = self.leftFlipper.status * self.ball.delta_y
            arcade.sound.play_sound(flipSound)

        if self.ball.hit(self.rightFlipper, 33.75):
            self.ball.delta_y = self.rightFlipper.status * self.ball.delta_y
            arcade.sound.play_sound(flipSound)


    def on_key_press(self,key,key_modifiers):
        resetSound = arcade.sound.load_sound('sounds/rewind.mp3')
        if key == arcade.key.SPACE:
             self.leftFlipper.switch_direction()
             self.rightFlipper.switch_direction()

        if key == arcade.key.R:
            arcade.sound.play_sound(resetSound)
            self.ball.x = 350
            self.ball.y = 400
            self.ball.delta_x = 1.5
            self.ball.delta_y = -0.85
            self.score = 0
