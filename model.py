import arcade.key
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
        self.delta_x = 0.5 #actual 0.5
        self.delta_y = -0.85 #actual -0.85


    def update(self, delta):

        #Check Wall hit
        if self.x > 700 - 32:
            self.delta_x *= -1
        elif self.x < 32:
            self.delta_x *= -1
        elif self.y > 700 - 32:
            self.delta_y *= -1
        elif self.y < 32:
            self.delta_y *= -1

        self.x += self.delta_x
        self.y += self.delta_y *GRAVITY_CONSTANT


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
            for y in range(150, 350, 32):
                x += 30
                self.list.insert(len(self.list),(x,y))

            x = 256
            for y in range(150, 350, 32):
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
        self.ball = Ball(self, 350, 350, 0)



    def update(self, delta):
        self.ball.update(delta)

        #Can't do slope yet!##################################
        if self.ball.hit(self.slope, 32):
            self.ball.delta_y *= -1
            self.ball.delta_x *= -1

        if self.ball.hit(self.leftBumper, 32):
            self.ball.delta_x = (self.ball.delta_x * -1)*1.1
            self.ball.delta_y = (self.ball.delta_y * -2)
            self.score += 100

        if self.ball.hit(self.midBumper, 32):
            self.ball.delta_x = (self.ball.delta_x * -1)*1.1
            self.ball.delta_y = (self.ball.delta_y * -2)
            self.score += 200

        if self.ball.hit(self.rightBumper, 32):
            self.ball.delta_x = (self.ball.delta_x * -1)*1.1
            self.ball.delta_y = (self.ball.delta_y * -2)
            self.score += 100

        if self.ball.hit(self.leftFlipper, 67.5):
            self.ball.delta_y = self.leftFlipper.status * self.ball.delta_y

        if self.ball.hit(self.rightFlipper, 67.5):
            self.ball.delta_y = self.rightFlipper.status * self.ball.delta_x


    def on_key_press(self,key,key_modifiers):
        if key == arcade.key.SPACE:
             self.leftFlipper.switch_direction()
             self.rightFlipper.switch_direction()

        if key == arcade.key.R:
            self.ball.x = 350
            self.ball.x = 350
            self.ball.delta_x = 0.5
            self.ball.delta_y = -0.85
            self.score = 0
