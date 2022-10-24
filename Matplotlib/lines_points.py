from PIL import Image
from pylab import *

def plot_points_lines():
    # read image to numpy array
    im = array(Image.open("empire_state.jpg"))
    # plot the image
    imshow(im)
    # some points
    x = [100,100,400,400]
    y = [200,500,200,500]
    # plot the points with red star-markers
    plot(x,y,"r*")
    # line plot connecting the first two points
    plot(x[:2],y[:2])
    # add title and show the plot
    title("Empire State Building")
    axis("off") # To remove the axis from plot (show only image)
    show()

if __name__ == "__main__":
    plot_points_lines()