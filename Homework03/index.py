import simplegui

mlsec = user = pc = 0


def create_timer():
    global mlsec
    mlsec += 1
    return str(mlsec)


def format(n):
    milliseconds = ((n % 6000) % 100) % 10
    seconds = ((n / 100) % 6) * 10
    minutes = n // 600
    if seconds < 10:
        seconds = '0' + str(int(seconds))
    else:
        seconds = int(seconds)
    return str(minutes) + ':' + str(seconds) + '.' + str(milliseconds)


def result(user, pc):
    return str(user) + '/' + str(pc)


def reset():
    global mlsec, user, pc
    mlsec = user = pc = 0


def stop():
    timer.stop()
    stp = format(mlsec)
    if stp[-1] == '0':
        global user, pc
        user += 1
    else:
        pc += 1


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(format(mlsec), [50, 112], 48, "Red")
    canvas.draw_text(result(user, pc), [150, 40], 28, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_canvas_background('Silver')

timer = simplegui.create_timer(100, create_timer)

frame.add_button("Start", timer.start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
