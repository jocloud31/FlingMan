# options
screen_height = 720
screen_width = 1280

# Player properties
player_acc = 1.25
player_friction = -0.18
player_gravity = 0.8
player_sprint = 1.25
player_jump_str = -19
player_x_deadzone = 0.015

# platform settings
platform_list = [(0.00, screen_height - 40.00, screen_width, 40.00),
                 (screen_width * 1 / 4, screen_height * 3 / 4, 100.00, 20.00),
                 (screen_width * 1 / 2, screen_height * 1 / 2, 100.00, 20.00),
                 (screen_width * 3 / 4, screen_height * 1 / 4, 100.00, 20.00)]

platform_tolerance = 10

# color definitions
white = [255, 255, 255]
black = [0, 0, 0,]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]

# hard settings
title = "FlingMan"
FPS = 60