# implementation of card game - Memory

import simplegui
import random

mem = []
width = 0
start_coordinat = []
color = 'Green'
text = False

clicks = []
guessed = []
step = 0


def create_memory_list():
    global mem
    list1 = []
    list2 = []
    while len(list1) < 8:
        list1.append(random.randrange(0, 8))
        list2.append(random.randrange(0, 8))

    mem.extend(list1)
    mem.extend(list2)
    return random.shuffle(mem)


create_memory_list()


def create_memory_cell():
    global width, start_coordinat
    k = 0
    while k < 16:
        width += 50
        start_coordinat.append([[width, 0], [width, 100], mem[k], [width - 40, 70], color])
        k += 1
    return start_coordinat


create_memory_cell()


# helper function to initialize globals
def new_game():
    global mem, width, start_coordinat, text, color, clicks, guessed, step
    label.set_text("Turns = 0")
    mem = []
    width = 0
    start_coordinat = []
    text = False
    color = 'Green'
    step = 0
    clicks = []
    guessed = []
    create_memory_list()
    create_memory_cell()


# define event handlers
def mouseclick(pos):
    global clicks, guessed, step, text

    # add game state logic here

    step += 1
    if step % 2 == 0:
        label.set_text("Turns = " + str(step / 2))

    for i in start_coordinat:
        if pos[0] < i[1][0] and pos[0] > (i[1][0] - 50):
            text = True
            i[4] = 'Transparent'
            clicks.append([start_coordinat.index(i), i[2], i[3]])
            print
            clicks

            if len(clicks) > 2 and (clicks[0][1] != clicks[-1][1]) and (clicks[0][0] != clicks[-1][0]):
                start_coordinat[clicks[0][0]][4] = 'Green'
                start_coordinat[clicks[1][0]][4] = 'Green'
                clicks.pop(1)
                clicks.pop(0)
            elif len(clicks) > 2 and (clicks[0][1] == clicks[-1][1]) and (clicks[0][0] != clicks[-1][0]):
                guessed.extend([clicks[0]])
                guessed.extend([clicks[1]])
                clicks.pop(1)
                clicks.pop(0)
            elif len(clicks) > 1 and (clicks[0][1] == clicks[1][1]) and (clicks[0][0] != clicks[1][0]):
                guessed.extend([clicks[0]])
                guessed.extend([clicks[1]])
                clicks.pop(1)
                clicks.pop(0)
            elif len(clicks) > 1 and (clicks[0][0] == clicks[1][0]) or (len(clicks) > 1) and (
                    clicks[1][0] == clicks[-1][0]):
                if step % 2 == 0:
                    step -= 1
                    label.set_text("Turns = " + str(step / 2))


# cards are logically 50x100 pixels in size
def draw(canvas):
    global width, start_coordinat

    canvas.draw_line([0, 0], [800, 0], 2, 'White')
    canvas.draw_line([0, 100], [800, 100], 2, 'White')
    canvas.draw_line([0, 0], [0, 100], 2, 'White')
    for i in start_coordinat:
        canvas.draw_line(((i[0][0] - 25), (i[0][1] + 2)),
                         ((i[1][0] - 25), (i[1][1] - 2)
                          ), 48, i[4])
        canvas.draw_line(i[0], i[1], 2, 'White')
    if text:
        for t in clicks:
            canvas.draw_text(
                str(start_coordinat[t[0]][2]),
                (start_coordinat[t[0]][3][0], start_coordinat[t[0]][3][1]),
                60, 'Red')
    if guessed:
        for g in guessed:
            canvas.draw_text(str(g[1]), (g[2][0], g[2][1]), 60, 'Red')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric