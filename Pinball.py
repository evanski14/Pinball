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
        self.LWall1 = arcade.Sprite('images/Wall.png')
        self.LWall1.set_position(1,625)
        self.LWall2 = arcade.Sprite('images/Wall.png')
        self.LWall2.set_position(1,475)
        self.LWall3 = arcade.Sprite('images/Wall.png')
        self.LWall3.set_position(1,325)

        self.RWall1 = arcade.Sprite('images/Wall.png')
        self.RWall1.set_position(700,625)
        self.RWall2 = arcade.Sprite('images/Wall.png')
        self.RWall2.set_position(700,475)
        self.RWall3 = arcade.Sprite('images/Wall.png')
        self.RWall3.set_position(700,325)

        self.UWall1 = arcade.Sprite('images/Wall.png')
        self.UWall1.set_position(550,700)
        self.UWall2 = arcade.Sprite('images/Wall.png')
        self.UWall2.set_position(400,700)
        self.UWall3 = arcade.Sprite('images/Wall.png')
        self.UWall3.set_position(250,700)
        self.UWall4 = arcade.Sprite('images/Wall.png')
        self.UWall4.set_position(100,700)

        self.Corner1 = arcade.Sprite('images/Corner.png')
        self.Corner1.set_position(700,700)
        self.Corner2 = arcade.Sprite('images/Corner.png')
        self.Corner2.set_position(0,700)
        #### Set Ball stuffs here ####
        self.Ball = ModelSprite('images/Ball.png', model = self.world.ball)


    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()

        self.LeftFlipper.draw()
        self.RightFlipper.draw()
        ### BUILD DA WALLS PT2 ###
        self.LWall1.draw()
        self.LWall2.draw()
        self.LWall3.draw()

        self.RWall1.draw()
        self.RWall2.draw()
        self.RWall3.draw()

        self.UWall1.draw()
        self.UWall2.draw()
        self.UWall3.draw()
        self.UWall4.draw()

        self.Corner1.draw()
        self.Corner2.draw()
        ##### Ball doesnt work yet #####
        self.Ball.draw()


def main():
    window = PinBall(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
