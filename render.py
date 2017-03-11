import numpy as np
import cairo

import gi
gi.require_version('Gtk', '3.0') #ensures correct version of gtk
from gi.repository import Gtk
from gi.repository import GObject
import time

class Show(Gtk.Window):

    def __init__(self,draw,image_size):
        super(Show, self).__init__()
        self.draw=draw
        self.image_size=image_size
        self.init_ui()



    def init_ui(self):

        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        self.add(darea)

        self.set_title("Fill & stroke")
        self.resize(*self.image_size)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        Gtk.main()


    def on_draw(self, wid, cr):
        self.draw(self,cr)
        #print(cr,type(cr))



class Render(object):
    """contains the cairo image surface and context information as well as abs
    color information. also has all of the actual shape drawing information"""

    def __init__(self,image_size,background_color, foreground_colors):
        self.image_size = image_size
        self.colors=foreground_colors
        self.background_color = background_color
        self.unit = 1./max(image_size)
        assert image_size[0]>=image_size[1] , "oh no, things might get funny with an aspect ratio < 1, beware!"

        self.ncolors = 0
        self.num_img = 0
        self.__init_cairo()

    def __init_cairo(self):
        sur = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.image_size[0],self.image_size[1])
        ctx = cairo.Context(sur)
        ctx.scale(self.image_size[0],self.image_size[0])
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
        ctx.rectangle(x, y, 1./image_size[0], 1./image_size[1])
        ctx.fill()
    def scalexy(self,xy):
        #note, this only works if xdim,ydim
        return xy[0],xy[1]*self.image_size[1]/self.image_size[0]

    def circle(self,x,y,r):
        x,y =self.scalexy([x,y])
        self.ctx.arc(x,y,r,0,np.pi*2)
        self.ctx.fill()
    def line(self,start,end,width=1):
        self.ctx.set_line_width(width)
        self.ctx.move_to(start[0],start[1])
        self.ctx.line_to(end[0],end[1])
        self.ctx.stroke()


class Image_Creator(Render):
    def __init__(self, image_size, background_color, foreground_colors, step_function, stop, fname):
        Render.__init__(self,image_size, background_color, foreground_colors)
        self.fname=fname
        self.stop=stop
        self.step_function=step_function
        self.step=0

    def create(self):
        for i in range(self.stop):
            self.step=i
            if len(self.colors)!=1:
                self.colorset(self.colors[i])
            self.step_function(self)

        self.sur.write_to_png(time.strftime(fname))


class Animate(Render):

    def __init__(self, image_size, foreground_color, background_color,step,stop=-1,interval=100,save=True,fname='test.png'):
        Render.__init__(self, image_size, foreground_color, background_color)

        window = Gtk.Window()
        self.window = window
        self.window.resize(self.image_size[0],self.image_size[1])

        self.window.connect("destroy", self.__destroy)

        darea = Gtk.DrawingArea()
        self.darea = darea

        self.window.add(darea)
        self.window.show_all()
        self.step=step
        self.steps = 0
        self.save=save
        self.stop=stop
        self.fname=fname
        #idle function that will continue to run as long as it remains true
        GObject.timeout_add(interval,self.steper) #interval is in milliseconds


    def steper(self):
        """this is the function that is run repeatedly"""
         # draw function that will be used.
        repeat = self.step(self)

        self.draw()

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
            self.sur.write_to_png(time.strftime(self.fname))
        Gtk.main_quit(*args)
    def start(self):
        Gtk.main()

    def draw(self, *args):
        cr = self.darea.get_property('window').cairo_create()
        cr.set_source_surface(self.sur, 0, 0)
        cr.paint()
