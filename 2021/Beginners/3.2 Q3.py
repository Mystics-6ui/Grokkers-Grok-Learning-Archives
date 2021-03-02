from turtle import *
pencolour('pink')
pensize(5)
oh = int(input('Length? '))
e = oh/2
for i in range(6):
  forward(oh)
  left(60)
  backward(e)
