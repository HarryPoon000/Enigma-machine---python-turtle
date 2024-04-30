import turtle
import enigma

eng = enigma.machine()

turtle.setworldcoordinates(-50,-50,350,350)
turtle.tracer(False)

disp = turtle.Turtle()
disp.up()

msg = ''

def handle(txt):
    global msg
    disp.clear()
    if len(msg)%48 == 0:
        msg += '\n'
    msg += txt
    out = eng.compute(msg, reset = True)
    disp.write(out, font = ('Arial', 20, 'normal'))
    turtle.update()

alph = 'abcdefghijklmnopqrstuvwxyz '
for i in alph:
    if i == ' ':
        exec(f'def key_space():\n\thandle(" ")')
        turtle.onkey(eval(f'key_space'), 'space')
    else:
        exec(f'def key_{i}():\n\thandle("{i}")')
        turtle.onkey(eval(f'key_{i}'), i)

def reset(x,y):
    global msg
    msg = ''
    disp.clear()

rst = turtle.Turtle()
rst.shape('square')
rst.up()
rst.goto(150, -25)

rst.color('grey')
rst.shapesize(1,2)
rst.onclick(reset)

turtle.listen()
turtle.update()
turtle.mainloop()
