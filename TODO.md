# Moving forward
#### make the parameters setable via external input.
- this could be simple dials and sliders 
- could also be some form of analogue input, ie audio
#### make some form of this realtime
- this could allow performance a la tims video shows, or encorporation into his shows
- it could also allow for interractive art. allow people to change settings on the fly, or maybe pick settings they like and watch the parameter space evolve based on those selections.


### Flocking
- need to wrap the flocking into a class.
- write test cases for that class these could include
    - a timing example for a specific set of cases iterating over image size and particle number. This could actually return logged timing to see if there is any variation over time
    - visual check examples. ie two particles from opposite sides colliding, a couple of parallel particles from one side. stationary particle in center(null check)
- after all this, make a new class that uses kd-trees instead. benchmark against brute force.
- could also explore an expanded or altered rule set, which could include non-biological inspired rules. could think of "leader" or "predetor/repulsor" particles
- see this link for a [tweet](https://twitter.com/mattdesl/status/835931748471013376) on images that probably incorporate altered rules
- see this paper on [steering behaviour](https://red3d.com/cwr/papers/1999/gdc99steer.pdf) for some behavioural ideas
- a very small flock, maybe < 10 boids could be used to draw curves between the boids, or fill an area between them. this would be interesting for life work.
- could use the flock class as a general grouping of particles. this would eventually encompass the randomcolorline as one of the possible configurations.
    - flock would have to include the lifetime of the flock (total number of steps), the colormapping of the flock, and any accelerators that the flock responds to (brownian, point or vector field, or particle particle interractions)
    - having all of this information contained within a flock would allow multiple flocks in one image.

### colormap-dev
explore the color sampling from images.
- could use [k-mean clustering](https://en.wikipedia.org/wiki/K-means_clustering) to group pixels from an image. however, k means tends to group to spatially equivalent groups, while [expectation-maximum](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm) allows clusters of different sizes. Could investigate the differences between both
- a byproduct of the need to sample pixels from an image could be some sort of extensability to pixel sorting and image glitching. maybe sort, blocks of pixels on an image, or bands to produce glitch patterns?
- explore a varying alpha level to ensure that as particles become more sparse the color is not lost.
- another avenue to explore regarding ensuring that the colors are visible would be restricted color ranges. in RGB this could just be all values >0.3 for example. or I could play around with HSB color space.


### master
1. do a central start, brownian with custom color maps *tweet*
2. randomize colormaps *tweet my favorite*
    - make sure to log the colormap values and positions within the map space alongside images
3. do colormap matrices, with incremental, but random parameter changes *tweet grid*
4. mabye make a bot to do random colormaps



    
    
