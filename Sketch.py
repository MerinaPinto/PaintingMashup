from p5 import *

def setup():
  createCanvas(500,500)
  background("black")
  
def draw():
  x=random(0,500)
  y=random(0,500)
  size=random(3,8)
  drawTickAxes()
  
  strokeWeight(size)
  #blue dots 
  if 100<x<200 and 100<y<200:
    stroke("blue")
    point(x,y)
  
  #red dots
  elif 200<x<300 and 100<y<300:
    stroke("red")
    point(x,y)

  #white dots 
  elif 300<x<400 and 100<y<400:
    stroke("white")
    point(x,y)

  #green dots 
  elif 400<x<500 and 100<y<500:
    stroke("green")
    point(x,y)
  else:
    stroke("yellow")
    point(x,y)
  #square(x,y,size)
  #square(150,200,random(100,250))
