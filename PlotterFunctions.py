import matplotlib.pyplot as plt
import cv2
import numpy as np
import WrapperFunctions

# Method that plots the histogram of single color channel
def plotSingleChannelHistogram(colorChannelHist, color):
    x = np.arange(256)
    plt.bar(x, colorChannelHist, color=color)
    plt.show()


# That function do the all jobs related to histogram plots
# Input is image name, output is 3 channel histogram plots
def doHistogramPlots(imageName, fileOutputName):
    Image = cv2.imread(imageName, 1)   # read the 3 channel input image
    bChannel, gChannel, rChannel = cv2.split(Image)   # split the color channels of input image

    rHist = WrapperFunctions.histogramCalculator(rChannel)
    gHist = WrapperFunctions.histogramCalculator(gChannel)
    bHist = WrapperFunctions.histogramCalculator(bChannel)

    plotAllHistogramChannels(rHist, gHist, bHist, imageName, fileOutputName)



# Method that plots the histogram of all three channels
def plotAllHistogramChannels(colorChannelHistR, colorChannelHistG, colorChannelHistB, imageName, fileOutputName):
    fig = plt.figure()
    x = np.arange(256)

    plt.subplot(3, 1, 1)
    plt.bar(x, colorChannelHistR.reshape(colorChannelHistR.shape[0]), color='red')
    plt.subplot(3, 1, 2)
    plt.bar(x, colorChannelHistG.reshape(colorChannelHistG.shape[0]), color='green')
    plt.subplot(3, 1, 3)
    plt.bar(x, colorChannelHistB.reshape(colorChannelHistB.shape[0]), color='blue')

    fig.savefig(fileOutputName)


# Method that merges 3 color channels into 1 and writes the merged image to a file
def mergeColorChannels(red, green, blue):
    OutputImage = cv2.merge((blue, green, red))
    cv2.imwrite('output.png', OutputImage)
    # cv2.imshow('OutputImage', OutputImage)

def matchThreeChannels(Input, Target):
    InputImage = cv2.imread(Input, 1)   # read the 3 channel input image
    bChannelInput, gChannelInput, rChannelInput = cv2.split(InputImage)   # split the color channels of input image

    TargetImage = cv2.imread(Target, 1)   # read the 3 channel target image
    bChannelTarget, gChannelTarget, rChannelTarget = cv2.split(TargetImage)   # split the color channels of target image

    bOutputChannel = WrapperFunctions.matchSingleChannelHistogram(bChannelInput, bChannelTarget)
    gOutputChannel = WrapperFunctions.matchSingleChannelHistogram(gChannelInput, gChannelTarget)
    rOutputChannel = WrapperFunctions.matchSingleChannelHistogram(rChannelInput, rChannelTarget)

    bOutputHist = WrapperFunctions.histogramCalculator(bOutputChannel)
    gOutputHist = WrapperFunctions.histogramCalculator(gOutputChannel)
    rOutputHist = WrapperFunctions.histogramCalculator(rOutputChannel)

    mergeColorChannels(rOutputChannel, gOutputChannel, bOutputChannel)

# HOW TO RUN
# plotSingleChannelHistogram(bOutputHist, "blue")
# plotSingleChannelHistogram(rTargetHist, "red")
# mergeColorChannels(rOutputChannel, gOutputChannel, bOutputChannel)

# rInputHist = histogramCalculator(rChannelTarget)
# gInputHist = histogramCalculator(gChannelTarget)
# bInputHist = histogramCalculator(bChannelTarget)
# plotAllHistogramChannels(rInputHist, gInputHist, bInputHist)
