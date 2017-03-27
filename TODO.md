
### Flocking
- need to wrap the flocking into a class.
- write test cases for that class these could include
    - a timing example for a specific set of cases iterating over image size and particle number. This could actually return logged timing to see if there is any variation over time
    - visual check examples. ie two particles from opposite sides colliding, a couple of parallel particles from one side. stationary particle in center(null check)
- after all this, make a new class that uses kd-trees instead. benchmark against brute force.

- could also explore an expanded or altered rule set, which could include non-biological inspired rules. could think of "leader" or "predetor/repulsor" particles
- see this link for a [tweet](https://twitter.com/mattdesl/status/835931748471013376) on images that probably incorporate altered rules
- see this paper on [steering behaviour](https://red3d.com/cwr/papers/1999/gdc99steer.pdf) for some behavioural ideas

### colormap-dev
explore the color sampling from images.
- could use [k-mean clustering](https://en.wikipedia.org/wiki/K-means_clustering) to group pixels from an image. however, k means tends to group to spatially equivalent groups, while [expectation-maximum](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm) allows clusters of different sizes. Could investigate the differences between both
- a byproduct of the need to sample pixels from an image could be some sort of extensability to pixel sorting and image glitching. maybe sort, blocks of pixels on an image, or bands to produce glitch patterns?
- explore a varying alpha level to ensure that as particles become more sparse the color is not lost.


### master
1. do a central start, brownian with custom color maps *tweet*
2. randomize colormaps *tweet my favorite*
    - make sure to log the colormap values and positions within the map space alongside images
3. do colormap matrices, with incremental, but random parameter changes *tweet grid*
4. mabye make a bot to do random colormaps


### printed work
look into doing photo prints of work.
- might be important to consider background color for this
