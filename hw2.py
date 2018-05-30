#!/usr/bin/env python3

import datetime
from webcam import *
from PIL import ImageStat
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class MUCamera:

    def __init__(self):
# stores intensities
        self.inte = []
        self.dates = []
        self.nums = []
        self.counter = 0
        self.df = {}
        
        

    def plot_intense(self, df):
        # get times

        plt.plot(df['Date'], df['Intensity'])
        plt.ylabel('Intensity')
        plt.xlabel('Time')
        plt.show()
        
        return 0

    def to_csv(self, df):
        df.to_csv('inte.csv', sep=',')
            
    def average_intensity(self, im):
        return ImageStat.Stat(im).mean[0]

    def filtered_average_intensity(self, im):
        return 0

    def call_back(self, image):
        # calculate the average intensity in the image
        intensity = self.average_intensity(image)
        # show the image
        # image.show()
        self.inte.append(intensity)
        self.dates.append(datetime.datetime.now().strftime("(%m-%d) %H:%M:%S"))
        
        self.df = pd.DataFrame({'Intensity': self.inte, 'Date': self.dates})
        

        print('Intensity: ' + str(intensity))

    def get_image(self):
        w = Webcam()
        w.register_callback(self.call_back, 1)
        w.start()
        input('Hit Enter to Stop \n')
        w.stop()
        self.plot_intense(self.df)
        self.to_csv(self.df)
        print(self.df)

if __name__ == '__main__':
    # create csv file
    # with open('intensities.csv', 'w+') as f:
    #     f.write('Date/Time, Intensity')
        
    print(datetime.datetime.now())
    cam = MUCamera()
    cam.get_image()