import arcade
from model import World

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle

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
        self.background = arcade.Sprite('images/background.jpg')
        self.background.set_position(350, 350)

        self.LeftFlipper = ModelSprite('images/LeftFlipper.png', model = self.world.leftFlipper)
        self.RightFlipper = ModelSprite('images/RightFlipper.png', model = self.world.rightFlipper)

        self.LeftBumper = ModelSprite('images/Bumper.png', model = self.world.leftBumper)
        self.RightBumper = ModelSprite('images/Bumper.png', model = self.world.rightBumper)
        self.MidBumper = ModelSprite('images/Bumper.png', model = self.world.midBumper)
        ### BUILD DA WALLS ###
        self.Wall = ListSprite('images/Wall.png', model = self.world.wall)
        self.Slope = ListSprite('images/Slope.png', model = self.world.slope)

        #### Set Ball stuffs here ####
        self.Ball = ModelSprite('images/Ball.png', model = self.world.ball)

    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()
        self.background.draw()

        self.LeftFlipper.draw()
        self.RightFlipper.draw()

        self.LeftBumper.draw()
        self.RightBumper.draw()
        self.MidBumper.draw()
        ### BUILD DA WALLS PT2 ###
        self.Wall.draw()
        self.Slope.draw()

        self.Ball.draw()

        arcade.draw_text(str(self.world.score),  600, 30, arcade.color.WHITE, 20)

    def on_key_press(self,key,key_modifiers):
        self.world.on_key_press(key, key_modifiers)



def main():
    window = PinBall(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()
