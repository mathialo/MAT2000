import dwt              # Wavelet functionality 
import images as img    # Imgaing functionality
import numpy as np      # For data structures
from sys import argv    # Reading from cmd-line


def main():
    # read image, read location from command line
    image = np.double(img.imread("%s.jpg" % argv[1]))

    # apply 2d Haar DWT
    dwt.DWT2Impl(image, 1, dwt.DWTKernelHaar)

    # make sure the elements of the image are in [0, 255]
    img.mapto01(image)
    image *= 255

    # save and show image
    img.imwrite(image, "%s_wavelet.jpg" % argv[1])
    img.imshow(image)


if __name__ == "__main__":
    main()
