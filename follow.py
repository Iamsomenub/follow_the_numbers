import random
import pgzrun
from time import time

WIDTH = 400
HEIGHT = 400

dots = []
lines = []
enemy_dots = []

next_dot = 0

enemy_dot_labels = []

dot_amount = 10
enemy_dots_amount = 10

start_time = time()
elapsed_time = 0

for dot in range(dot_amount):
    actor = Actor("dot")
    actor.pos = random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20)
    dots.append(actor)

for enemy_dot in range(enemy_dots_amount):
    label = str(random.randint(1, dot_amount))
    enemy_dot_labels.append(label)
    enemy_dot = Actor("red-dot")
    enemy_dot.pos = random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20)
    enemy_dots.append(enemy_dot)


def draw():
    global elapsed_time

    screen.fill("black")
    
    number = 1
    for dot in dots:
        screen.draw.text(str(number), \
            (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number += 1
    
    j = 0
    for enemy_dot in enemy_dots:
        screen.draw.text(enemy_dot_labels[j], \
            (enemy_dot.pos[0], enemy_dot.pos[1] + 12))
        enemy_dot.draw()
        j += 1

    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))

    if next_dot < dot_amount:
        end_time = time()
        elapsed_time = round(end_time - start_time, 1)
    screen.draw.text(str(elapsed_time), (10, 10))


def on_mouse_down(pos):
    global next_dot
    global enemy_dot
    global lines

    if next_dot >= dot_amount:
        return

    if enemy_dot.collidepoint(pos):
        if enemy_dot:
            lines = []
            next_dot = []

    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot += 1
    else:
        lines = []
        next_dot = 0


def update():
    pass


pgzrun.go()