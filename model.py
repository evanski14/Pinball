CIRCLE_RADIUS = 16
BOUNCINESS = 0.9
GRAVITY_CONSTANT = 9.81


class LeftFlipper:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y





class RightFlipper:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y




class Ball:
    def __init__(self,world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def update(self, delta):

        delta_x = 0
        delta_y = -0.85

        self.x += delta_x
        self.y += delta_y * GRAVITY_CONSTANT



class Wall:
    def __init__(self,world,x ,y):
        self.world = world
        self.x = x
        self.y = y 



class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        #self.leftFlipper = LeftFlipper(self, 286, 150)
        #self.rightFlipper = RightFlipper(self, 416, 150)
        self.ball = Ball(self, 350, 350)

    def update(self, delta):
        self.ball.update(delta)
