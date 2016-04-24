import threading
from tkinter import *  # Importing the Tkinter (tool box) library
from random import randint

from terrain import *

PLAYER_COLOR = "#689F38"

itIsWin = False  # TODO detect
if itIsWin:
    from winsound import *

CELL_SIZE = 32

WIDTH = 30
HEIGHT = 20

userX = 5
userY = 1

currentTick = 0


def init_terrain():
    global terrain
    terrain = [[Terrain() for i in range(HEIGHT)] for i in range(WIDTH)]
    for x in range(WIDTH):
        for y in range(userY + 3):
            terrain[x][y] = EmptySpace()
        for y in range(userY + 3, userY + 4):
            terrain[x][y] = Humus()
        for y in range(userY + 4, userY + 7):
            terrain[x][y] = Sand()
        for y in range(userY + 7, HEIGHT):
            terrain[x][y] = Diorite()

        for y in range(userY + 2, userY + 3):
            if randint(0, 9) > 8:
                terrain[x][y] = Tree()


init_terrain()

window = Tk()
window.wm_title("Копатель офлаен")

canvas = Canvas(window, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE)
canvas.pack()


def on_click(event):
    x = event.x
    y = event.y
    print("mouse click: " + str(x) + " " + str(y))


pressed_keys = set()


def on_key_press(key):
    global pressed_keys
    pressed_keys.add(key.char)


def on_key_release(key):
    global pressed_keys
    pressed_keys.discard(key.char)


canvas.bind_all("<KeyPress>", on_key_press)
canvas.bind_all("<KeyRelease>", on_key_release)
# canvas.bind("<KeyRelease>", on_key_release)
canvas.bind("<Button-1>", on_click)


def draw():
    def draw_rect_at(x, y, color, width=0):
        x *= CELL_SIZE
        y *= CELL_SIZE
        canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=color, width=width)

    canvas.delete("all")

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            draw_rect_at(x, y, terrain[x][y].color())

    draw_rect_at(userX, userY, PLAYER_COLOR, 1)


def is_pressed(dir):
    return dir in pressed_keys


def update():
    global userX, userY, pressed_keys, currentTick

    def move(x, y):
        global userX, userY
        if 0 <= x < WIDTH and 0 <= y < HEIGHT and terrain[x][y].isAccessible():
            userX = x
            userY = y
            return True
        return False

    solid_under_foot = not move(userX, userY + 1)  # gravity

    x = userX
    y = userY

    if is_pressed('w') and solid_under_foot:
        y -= 1
        move(x, y)
    if is_pressed('s'):
        y += 1
        move(x, y)
    if is_pressed('a'):
        x -= 1
    if is_pressed('d'):
        x += 1

    move(x, y)

    currentTick += 1


def do_loop():
    update()
    draw()
    window.after(int(1000 / 15), do_loop)


def play_sound_track():
    if not itIsWin:
        return
    PlaySound('cr1est.wav', SND_FILENAME)
    pass


thread = threading.Thread(target=play_sound_track)
thread.daemon = True
thread.start()

do_loop()
window.mainloop()
