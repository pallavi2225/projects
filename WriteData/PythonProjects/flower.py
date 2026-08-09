import turtle as t
import colorsys
t.bgcolor('black')
t.tracer (500)

def draw():
    h=0
    for i in range(100):
        c=colorsys.hsv_to_rgb(h,1,1)
        h+=0.5
        t.up()
        t.goto(0,0)
        t.down()
        t.color('black')
        t.fillcolor(c)
        t.begin_fill()
        t.rt (98)
        t.circle(i,12)
        t.fd(290)
        t.fd(i)
        t.lt(29)
        for j in range(129):
            t.fd(i)
            t.circle(j, 299, steps=2)
            t.end_fill()
draw()
t.done()
            
        
        
        

        
        
