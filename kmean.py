from PIL import Image
import numpy as np
from render import Show
import os



def imageto_array(image_path,v=False):
    im = Image.open(image_path)
    im.thumbnail((256,256))
    arrayim =  np.asarray(im)
    if v:
        print(im.size,im.format,im.mode)
        print(arrayim.shape)
    return arrayim


if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    image_array = imageto_array("testimage.jpg",v=False)
    h=image_array.shape[0]
    w=image_array.shape[1]
    image_list=np.reshape(image_array,((h*w),3)).shape

    def draw(self,cr):
        cr.set_line_width(9)
        cr.set_source_rgb(0.7, 0.2, 0.0)

        w, h = self.get_size()

        cr.translate(w/2, h/2)
        cr.arc(0, 0, 50, 0, 2*np.pi)
        cr.stroke_preserve()

        cr.set_source_rgb(0.3, 0.4, 0.6)
        cr.fill()
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    app = Show(draw)
