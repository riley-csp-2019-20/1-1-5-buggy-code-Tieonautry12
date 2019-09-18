
import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
w = 8
length= 90
circle = 380 / w
spider.pensize(5)
spiderlegs = 0
while (spiderlegs < w):
  spider.goto(0,0)
  spider.setheading(circle*spiderlegs)
  spider.forward(length)
  spiderlegs = spiderlegs + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
