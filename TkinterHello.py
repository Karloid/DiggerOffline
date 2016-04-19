import threading
from tkinter import *  # Importing the Tkinter (tool box) library
from winsound import *

CELL_SIZE = 16

WIDTH = 30
HEIGHT = 20

userX = 5
userY = 1

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
    canvas.delete("all")
    x = userX * CELL_SIZE
    y = userY * CELL_SIZE
    canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="#689F38", width=1)


def last_key_is(dir):
    return last_key is not None and last_key.lower() == dir.lower()


def update():
    global userX, userY, last_key
    if last_key_is('s'):
        userY += 1
    elif last_key_is('d'):
        userX += 1
    elif last_key_is('a'):
        userX -= 1
    elif last_key_is('w'):
        userY -= 1
    last_key = None


def do_loop():
    update()
    draw()
    window.after(int(1000 / 15), do_loop)


def play_sound_track():
    PlaySound('crest.wav', SND_FILENAME)


thread = threading.Thread(target=play_sound_track)
thread.daemon = True
thread.start()

do_loop()
window.mainloop()
