import matplotlib.pyplot as plt
import cv2
import numpy as np

# Method that plots the histogram of single color channel
def plotSingleChannelHistogram(colorChannelHist, color):
    x = np.arange(256)
    plt.bar(x, colorChannelHist, color=color)
    plt.show()


# Method that merges 3 color channels into 1 and writes the merged image to a file
def mergeColorChannels(red, green, blue):
    OutputImage = cv2.merge((blue, green, red))
    cv2.imwrite('output.png', OutputImage)
    # cv2.imshow('OutputImage', OutputImage)


# RUN
# plotSingleChannelHistogram(bOutputHist, "blue")
# plotSingleChannelHistogram(rTargetHist, "red")
# mergeColorChannels(rOutputChannel, gOutputChannel, bOutputChannel)
