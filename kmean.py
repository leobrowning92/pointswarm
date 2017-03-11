from PIL import Image
import numpy as np
from render import Show
import os
from scipy.cluster.vq import kmeans



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

    image_array = imageto_array("testimage.jpg",v=False)/256
    h=image_array.shape[0]
    w=image_array.shape[1]
    image_list=np.reshape(image_array,((h*w),3))
    print(kmeans(image_list,5))

    def draw(self,cr):
        for i in range(h):
            for j in range(w):
                cr.set_source_rgb(*image_array[i,j])
                #cr.translate(w/2, h/2)
                cr.rectangle(j, i, 1, 1)
                cr.fill()
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    app = Show(draw,[w,h])
