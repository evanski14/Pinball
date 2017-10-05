import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

CIRCLE_RADIUS = 20

GRAVITY_CONSTANT = 0.3

BOUNCINESS = 0.9

NO_FLIPPER = 0
FLIPPER_UP = 1


def __init__(self, width, height, resizable):
    super(). __init__(width, height, resizable= resizable)
    self.sprite_list = arcade.SpriteList()

    self.left_flipper_list = arcade.SpriteList()
    self.right_flipper_list = arcade.Spritelist()
    self.left_flipper_state = NO_FLIPPER
    self.right_flipper_state = NO_FLIPPER

    self.time = 0

def draw(delta_time):

    arcade.start_render()

    arcade.draw_circle_filled(draw.x, draw.y, CIRCLE_RADIUS, arcade.color.WHITE)

    draw.x += draw.delta_x
    draw.y += draw.delta_y

    draw.delta_y -= GRAVITY_CONSTANT

    #Hitting check!
    #LEFT AND RIGHT
    if draw.x < CIRCLE_RADIUS and draw.delta_x < 0 :
        draw.delta_x *= -BOUNCINESS
    elif draw.x > SCREEN_WIDTH - CIRCLE_RADIUS and draw.delta_x > 0:
        draw.delta_x *= -BOUNCINESS

    #TOP AND BOTTOM
    if draw.y < CIRCLE_RADIUS and draw.delta_y < 0:
        if draw.delta_y * -1 > GRAVITY_CONSTANT *15:
            draw.delta_y *= -BOUNCINESS
        else:
            draw.delta_y *= -BOUNCINESS / 2





draw.x = CIRCLE_RADIUS
draw.y = SCREEN_HEIGHT - CIRCLE_RADIUS
draw.delta_x = 2
draw.delta_y = 0


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "PinBall")
    arcade.set_background_color(arcade.color.BLACK)

    arcade.schedule(draw, 1/80)

    arcade.run()

    arcade.close_window()

if __name__ == "__main__":
    main()
