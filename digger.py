import threading
from tkinter import *  # Importing the Tkinter (tool box) library
from terrain import *

PLAYER_COLOR = "#689F38"

itIsWin = False  # TODO detect
if itIsWin:
    from winsound import *

CELL_SIZE = 16

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

init_terrain()

window = Tk()
window.wm_title("Копатель офлаен")

canvas = Canvas(window, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE)
canvas.pack()


def on_click(event):
    x = event.x
    y = event.y
    print("mouse click: " + str(x) + " " + str(y))


last_key = None


def on_key_press(key):
    global last_key
    last_key = key.char


canvas.bind_all("<Key>", on_key_press)
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


def last_key_is(dir):
    return last_key is not None and last_key.lower() == dir.lower()


def update():
    global userX, userY, last_key, currentTick
    x = userX
    y = userY
    if last_key_is('s'):
        y += 1
    elif last_key_is('d'):
        x += 1
    elif last_key_is('a'):
        x -= 1
    elif last_key_is('w'):
        y -= 1

    # if x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT:
    if 0 <= x < WIDTH and 0 <= y < HEIGHT and terrain[x][y].isAccessible():
        userX = x
        userY = y

    last_key = None
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
