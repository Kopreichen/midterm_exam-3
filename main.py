x0 = 0
y0 = 0
j = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0

def on_forever():
    global x0, y0, j, x1, y1, x2, y2
    x0 = 4
    y0 = 0
    for i in range(5):
        j = 0
        led.plot(x0, y0)
        while j <= i - 1:
            j += 1
            x1 = x0
            y1 = y0 - j
            x2 = x0 + j
            y2 = y0
            led.plot(x1, y1)
            led.plot(x2, y2)
        basic.pause(200)
        x0 = x0 - 1
        y0 = y0 + 1
    basic.clear_screen()
basic.forever(on_forever)
