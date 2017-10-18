import arcade
from Model import World

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

CIRCLE_RADIUS = 16

GRAVITY_CONSTANT = 0.3

BOUNCINESS = 0.9

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()




class ListSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            for x,y in self.model.list:
                super().draw()
                self.set_position(x,y)

    def draw(self):
        self.sync_with_model()









class PinBall(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.LeftFlipper = arcade.Sprite('images/LeftFlipper.png')
        self.LeftFlipper.set_position(286, 150)
        self.RightFlipper = arcade.Sprite('images/RightFlipper.png')
        self.RightFlipper.set_position(416, 150)
        ### BUILD DA WALLS ###
        self.Wall = ListSprite('images/Wall.png', model = self.world.wall)
        self.Slope = ListSprite('images/Slope.png', model = self.world.slope)

        #### Set Ball stuffs here ####
        self.Ball = ModelSprite('images/Ball.png', model = self.world.ball)


    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()

        self.LeftFlipper.draw()
        self.RightFlipper.draw()
        ### BUILD DA WALLS PT2 ###
        self.Wall.draw()
        self.Slope.draw()

        ##### Ball doesnt work yet #####
        self.Ball.draw()


def main():
    window = PinBall(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
