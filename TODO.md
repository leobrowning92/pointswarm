- need to make the colormap an passed arguement to the Animation rather than an internal process. at the moment it simply happens with any
- The end goal of this would be to allow the passing of custom colormaps. see [this](http://bsou.io/posts/color-gradients-with-python) article for an extremely clear article on how to generate the colormaps for the future.
- then would be interesting to play around with non uniform color gradients, iehter from multiple linear interpolations, or via bezier curves.


consolidating scripts
need to consolidate the three scripts in to one cohesive functio. to do this i need to:
1. have the color and color map be made to be arguments. This has been done for the random_color_line. this then needs to be updated to work with the image creator as well as the animator.
2. pass the particles as an agrugment
3. pass the acceleration as an argument.
