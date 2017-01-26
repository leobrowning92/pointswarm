import numpy as np
import cairo

import gi
gi.require_version('Gtk', '3.0') #ensures correct version of gtk
from gi.repository import Gtk
from gi.repository import GObject
import time





class Render(object):
    """contains the cairo image surface and context information as well as abs
    color information. also has all of the actual shape drawing information"""

    def __init__(self,n, background_color, foreground_colors):
        self.n = n
        self.colors=foreground_colors
        self.background_color = background_color
        self.unit = 1./float(n)

        self.ncolors = 0
        self.num_img = 0
        self.__init_cairo()

    def __init_cairo(self):
        sur = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.n, self.n)
        ctx = cairo.Context(sur)
        ctx.scale(self.n, self.n)
        self.sur = sur
        self.ctx = ctx
        self.clear_canvas()

    def colorset(self,color):
        self.ctx.set_source_rgba(*color)

    def clear_canvas(self):
        ctx = self.ctx
        ctx.set_source_rgba(*self.background_color)
        ctx.rectangle(0, 0, 1, 1)
        ctx.fill()
        ctx.set_source_rgba(*self.colors[0])



    def dot(self, x, y):
        ctx = self.ctx
        pix = self.unit
        ctx.rectangle(x, y, pix, pix)
        ctx.fill()


    def circle(self,x,y,r):
        self.ctx.arc(x,y,r,0,np.pi*2)
        self.ctx.fill()
    def line(self,start,end,width=1):
        self.ctx.set_line_width(width)
        self.ctx.move_to(start[0],start[1])
        self.ctx.line_to(end[0],end[1])
        self.ctx.stroke()


class Image_Creator(Render):
    def __init__(self, image_size, background_color, foreground_colors, step_function, stop, name=""):
        Render.__init__(self,image_size, background_color, foreground_colors)
        self.name=name
        self.stop=stop
        self.step_function=step_function
        self.step=0

    def create(self):
        for i in range(self.stop):
            self.step=i
            if len(self.colors)!=1:
                self.colorset(self.colors[i])
            self.step_function(self)

        self.sur.write_to_png(time.strftime("pics/"+'%Y-%m-%d_%H-%M-%S') + ".png")



class Animate(Render):

    def __init__(self, n, foreground_color, background_color,step,stop=-1,interval=100,save=True):
        Render.__init__(self, n, foreground_color, background_color)

        window = Gtk.Window()
        self.window = window
        window.resize(self.n, self.n)

        window.connect("destroy", self.__destroy)

        darea = Gtk.DrawingArea()
        self.darea = darea

        window.add(darea)
        window.show_all()
        self.step=step
        self.steps = 0
        self.save=save
        self.stop=stop
        #idle function that will continue to run as long as it remains true
        GObject.timeout_add(interval,self.steper) #interval is in milliseconds

    def steper(self):
        """this is the function that is run repeatedly"""
         # draw function that will be used.
        repeat = self.step(self)

        self.expose()

        if self.stop==-1:
            return True
        elif self.steps<self.stop:
            if len(self.colors)!=1:
                self.colorset(self.colors[self.steps])
            self.steps += 1
            return True
        else:
            return False

    # Starts and finishes the animation window setup and teardown functions
    def __destroy(self,*args):
        if self.save:
            self.sur.write_to_png(time.strftime("pics/"+'%Y-%m-%d_%H-%M-%S')+".png")
        Gtk.main_quit(*args)
    def start(self):
        Gtk.main()

    def expose(self, *args):
        cr = self.darea.get_property('window').cairo_create()
        cr.set_source_surface(self.sur, 0, 0)
        cr.paint()
