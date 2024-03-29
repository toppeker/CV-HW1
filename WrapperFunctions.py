import cv2
import numpy as np

InputImage = cv2.imread('color1.png', 1)   # read the 3 channel input image
bChannelInput, gChannelInput, rChannelInput = cv2.split(InputImage)   # split the color channels of input image

TargetImage = cv2.imread('color2.png', 1)   # read the 3 channel target image
bChannelTarget, gChannelTarget, rChannelTarget = cv2.split(TargetImage)   # split the color channels of target image


# Method that calculates CDF for the given channel and for the given intensity value
# Returns the CDF for corresponding image and intensity value
def calculatePDF(colorChannel):
    totalIntensities = 0
    pdf = np.zeros((256, 1))

    for i in range(colorChannel.shape[0]):
        for j in range(colorChannel.shape[1]):
            intensityVal = colorChannel[i, j]
            pdf[intensityVal] += 1
            totalIntensities += 1

    return pdf / float(totalIntensities)



# Method that calculates CDF from PDF
def calculateCDF(inputChannel):
    pdf = calculatePDF(inputChannel)
    cdf = np.zeros((256, 1))
    for i in range(256):
        cdf[i] = sum(pdf[0 : i + 1])
        
    return cdf


# Method that matches the histogram of single channel
# Returns the matched histogram output
def matchSingleChannelHistogram(colorChannelInput, colorChannelTarget):
    cdfInput = calculateCDF(colorChannelInput)
    cdfTarget = calculateCDF(colorChannelTarget)
    LookUpTable = np.zeros((256, 1))
    gj = 0
    for gi in range(256):
        while cdfTarget[gj] < cdfInput[gi] and gj < 255:
            gj += 1
        LookUpTable[gi] = gj

    colorChannelOutput = np.uint8(LookUpTable[colorChannelInput])
    colorChannelOutput = colorChannelOutput.reshape(colorChannelOutput.shape[0], colorChannelOutput.shape[1])
    return colorChannelOutput


# Method that calculates the histogram of single channel
# Returns a histogram vector
def histogramCalculator(colorChannel):
    histogramVector = np.zeros((256, 1))
    for i in range(colorChannel.shape[0]):
        for j in range(colorChannel.shape[1]):
            histogramVector[colorChannel[i, j]] += 1
    return histogramVector


# bOutputChannel = matchSingleChannelHistogram(bChannelInput, bChannelTarget)
# print(histogramCalculator(bOutputChannel))
