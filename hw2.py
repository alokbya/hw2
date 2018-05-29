#!/usr/bin/env python3

import datetime
from webcam import *
from PIL import ImageStat
import matplotlib.pyplot as plt

# stores intensities
inte = []
dates = []

def plot_intense(arr1, arr2):
    # get intensities
    
    # get times
    plt.plot(arr1, arr2)
    plt.show()
    
    return 0

def call_back(image):
    # calculate the average intensity in the image
    intensity = ImageStat.Stat(image).mean[0]
    # show the image
    # image.show()
    # store file 
    # with open('intensities.csv', 'w') as f:
    #     f.write(intensity)
    #     f.write(datetime.datetime.now())
    inte.append(intensity)
    dates.append(datetime.datetime.now())
    unit = []
    
    print('Intensity: ' + str(intensity))

def get_image():
    w = Webcam()
    w.register_callback(call_back, 1)
    w.start()
    input('Hit Enter to Stop \n')
    w.stop()
    print(inte, dates)
    plot_intense(dates, inte)

if __name__ == '__main__':
    # create csv file
    # with open('intensities.csv', 'w+') as f:
    #     f.write('Date/Time, Intensity')
        
    print(datetime.datetime.now())
    get_image()