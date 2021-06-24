import pgzrun
from random import randint
# My Constants
WIDTH = 800
HEIGHT = 480
GRAVITY = 0.1
GAP = 200
SPEED = 2
TAP_POWER = 4
TITLE = 'TAPPY PLANE!'

plane = Actor('plane1')
plane.pos = (200, 100)
plane.velocity = 0
plane.alive = True
plane.score = 0

rock_down = Actor('rock_down')
rock_down.x = 700
rock_down.bottom = randint(100, 250)
rock_up = Actor('rock_up')
rock_up.x = rock_down.x
rock_up.top = rock_down.bottom + GAP

def draw():
    screen.blit('background', pos = (0, 0))
    plane.draw()
    rock_down.draw()
    rock_up.draw()
    screen.draw.text(str(plane.score), pos = (50, 30), fontsize = 40)

def update():
    update_plane()
    update_rocks()

def update_plane():
    if not plane.alive:
        plane.image = 'plane_dead'
    elif plane.image == 'plane1':
        plane.image = 'plane2'
    elif plane.image == 'plane2':
        plane.image = 'plane3'
    else:
        plane.image = 'plane1'
    plane.velocity += GRAVITY
    plane.y += plane.velocity
    if plane.colliderect(rock_up) or plane.colliderect(rock_down):
        plane.alive = False
        clock.schedule_unique(restart_game, 1.5)
        
def update_rocks():
    rock_down.x -= SPEED
    rock_up.x -= SPEED
    if rock_down.left < 0 or rock_up.left < 0:
        reset_rocks()
        plane.score += 1

def restart_game():
    plane.score = 0
    reset_rocks()
    plane.alive = True
    plane.y = 100
    plane.velocity = 0

def reset_rocks():
    rock_down.x = 700
    rock_down.bottom = randint(100, 250)
    rock_up.x = rock_down.x
    rock_up.top = rock_down.bottom + GAP

def on_key_down(key):
    if plane.alive:
        plane.velocity = -TAP_POWER

def on_mouse_down(pos):
    print(pos)

pgzrun.go()