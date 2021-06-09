import random
import pgzrun
from time import time

WIDTH = 400
HEIGHT = 400
dots = []
lines = []
traps = []

next_dot = 0

trap_labels = []

dot_amount = 5
number_of_traps = 0

start_time = time()
elapsed_time = 0

level = 1

def setup():
    global dots
    global traps
    dots = []
    traps = []
    for dot in range(dot_amount):
        actor = Actor("dot")
        actor.pos = random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20)
        dots.append(actor)

    for trap in range(number_of_traps):
        label = str(random.randint(1, dot_amount))
        trap_labels.append(label)
        r = Actor("dot")
        r.pos = random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20)
        traps.append(r)

def draw():
    global elapsed_time

    screen.fill("black")
    
    number = 1
    for dot in dots:
        screen.draw.text(str(number), \
            (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number += 1

    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))

    j = 0
    for trap in traps:
        screen.draw.text(trap_labels[j], \
            (trap.pos[0], trap.pos[1] + 12))
        trap.draw()
        j += 1


    if next_dot < dot_amount:
        end_time = time()
        elapsed_time = round(end_time - start_time, 1)
    screen.draw.text(str(elapsed_time), (10, 30))
    screen.draw.text(str(f"level: {level}"), (10, 10))


def start_next_level():
    global level
    global dot_amount
    global next_dot
    global lines
    global start_time
    global number_of_traps

    level += 1
    dot_amount += 2
    next_dot = 0
    lines = []
    start_time = time()
    number_of_traps += 1
    setup()


def on_mouse_down(pos):
    global next_dot
    global lines

    if next_dot >= dot_amount:
        start_next_level()
        return

    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot += 1
    else:
        for trap in traps:
            if trap.collidepoint(pos):                
                break
        lines = []
        next_dot = 0


def update():
    pass

setup()


pgzrun.go()