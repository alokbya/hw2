#!/usr/bin/env python3

import datetime
from webcam import *
from PIL import ImageStat


def call_back(image):
    # calculate the average intensity in the image
    intensity = ImageStat.Stat(image).mean[0]
    # show the image
    image.show()
    print('Intensity: ' + str(intensity))
    # print('You are a callback')

def get_image():
    w = Webcam()
    w.register_callback(call_back, 1)
    w.start()
    input('Hit Enter to Stop \n')
    w.stop()

if __name__ == '__main__':
    # create csv file
    # with open('intensities.csv', 'w+') as f:
    #     f.write('Date/Time, Intensity')
        
    print(datetime.datetime.now())
    get_image()