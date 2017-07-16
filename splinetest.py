import cairo
import numpy as np
from render import Render

def random_point():
    return [np.random.uniform(0,1),np.random.uniform(0,1)]
def point_collection(n):
    points=[]
    for i in range(n):
            points.append(random_point())
    return points
def midpoint(a,b):
    return np.mean([a,b],axis=0)
def draw_multiline(im,points,width):
    for i in range(1,len(points)):
        im.line(points[i-1],points[i],width)
def draw_curvyline(im,points,width):
    for i in range(1,len(points)-1):
        mid1=midpoint(points[i-1],points[i])
        mid2=midpoint(points[i],points[i+1])
        im.curve(mid1,points[i],mid2,width)

def circle_curve(im,points,width):
    assert len(points)==3
    l1=points[:2]
    l2=points[1:]


def curvetest():
    # use for loop to test all 3 line types with different colors
    # straight
    # curvy
    # arced
    pass


points=[ [0,0]  , [0.5,0.5],[0,1] ]
im=Render([256,256], [0,0,0,1], [[1,1,1,1]])
# draw_multiline(im,points,width=1./256)
# im.curve(*points,width=1./256)
# draw_curvyline(im,points,width=1./256)
draw_curvyline(im,[ [0,0]  , [0.5,0.5],[1,0] ],width=1./256)
draw_curvyline(im,[ [1,0]  , [0.5,0.5],[1,1] ],width=1./256)
draw_curvyline(im,[ [1,1]  , [0.5,0.5],[0,1] ],width=1./256)
draw_curvyline(im,[ [0,1]  , [0.5,0.5],[0,0] ],width=1./256)
circle_curve(im,[ [0,0]  , [0.5,0.5],[1,0] ],width=1./256)

im.sur.write_to_png("test.png")
