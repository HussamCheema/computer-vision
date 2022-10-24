from PIL import Image
from pylab import *

if __name__ == "__main__":
    # read image to array
    im = array(Image.open("empire_state.jpg").convert("L"))
    # create a new figure
    figure()
    # don’t use colors
    gray()
    # show contours with origin upper left corner
    contour(im, origin="image")
    axis("equal")
    axis("off")

    figure()
    hist(im.flatten(),128)
    # print("Please click 3 points")
    # x = ginput(3) # Use it for annotation
    show()