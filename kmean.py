from PIL import Image
import numpy as np
from render import Show
import os
from scipy.cluster.vq import kmeans2



def imageto_array(image_path,v=False):
    im = Image.open(image_path)
    im.thumbnail((256,256))
    arrayim =  np.asarray(im)
    if v:
        print(im.size,im.format,im.mode)
        print(arrayim.shape)
    return arrayim


def open_show(image_path,v=False):

    image_array = imageto_array(image_path,v=False)/256
    h=image_array.shape[0]
    w=image_array.shape[1]
    image_list=np.reshape(image_array,((h*w),3))

    def draw(self,cr):
        for i in range(h):
            for j in range(w):
                cr.set_source_rgb(*image_array[i,j])
                cr.rectangle(j, i, 1, 1)
                cr.fill()

    app = Show(draw,[w,h])

def open_kmean(image_path,clusters=5,v=False,show=False):
    image_array = imageto_array(image_path,v=False)/256
    h=image_array.shape[0]
    w=image_array.shape[1]
    image_list=np.reshape(image_array,((h*w),3))
    centers=kmeans2(image_list,clusters)
    if v:
        print(centers)
    if show:
        def draw(self,cr):
            #Draw the image
            for i in range(h):
                for j in range(w):
                    cr.set_source_rgb(*image_array[i,j])
                    cr.rectangle(j, i, 1, 1)
                    cr.fill()
            #Draw the cluster centers
            for i in range(len(centers[0])):
                cr.set_source_rgb(*centers[0][i])
                cr.rectangle(i*w/clusters, h, w/clusters, h*0.1)
                cr.fill()

        app = Show(draw,[w,h*1.1])
    return centers[0]


if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    open_kmean("testimage.jpg",clusters=5,show=True,v=True)
