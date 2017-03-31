def save_image(data, colormap, filename):
    """
    Saves the image without all the ugly axes and spacing matplotlib usually gives you.

    This is a slightly modified version of the funciton found on
    https://fengl.org/2014/07/09/matplotlib-savefig-without-borderframe/
    """

    import numpy as np

    sizes = np.shape(data)
    height = float(sizes[0])
    width = float(sizes[1])
     
    fig = plt.figure()
    fig.set_size_inches(width/height, 1, forward=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
 
    ax.imshow(data, cmap=colormap)
    plt.savefig(filename, dpi = height) 
    #plt.show()
    plt.close()
