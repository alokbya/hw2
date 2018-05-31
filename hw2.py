#!/usr/bin/env python3

import datetime
from webcam import *
from PIL import ImageStat
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import operator
import collections

class MUCamera:

    def __init__(self):
# stores intensities
        self.inte = []
        self.dates = []
        self.nums = []
        self.counter = 0
        self.df = {}
        self.image_intensity = 0
        self.pro_color = 0          # stores proportion of most common color

    def mean_filter(self, l, width=3):
        place_holder = 0
        new = []

        # Find the distance from center number to either side
        side = int((width - 1)/2)

        # Iterate through list starting with left side of number
        # To last number with side buffer
        for i in range(side, len(l) - (side+1)+1):
            for j in range(i-side, i+side+1):
                place_holder = place_holder + l[j]
            new.append(round(place_holder/width, 2))
            place_holder = 0
    
        return new
    
    def filtered_average_intensity(self):
        df = pd.read_csv('overnight_1.csv')
        self.inte = df['Intensity'].tolist()
        self.dates = df['Date'].tolist()
        
        
        # clean up data (remove repeats)
        # for i in range(len(inte) - 1):
        #     if inte[i] == inte[i+1]:
        #         del inte[i]
        #         del dates[i]

        # perform movmean averaging on data to smooth
        # inte = mean_filter(inte, 3)
        self.inte = self.mean_filter(self.inte, 150)
        print(self.inte)
        # print(dates)
        index = list(range(len(self.inte)))
        
        # plot the graph
        plt.plot(index, self.inte)
        plt.ylabel('Intensity')
        plt.xlabel('Time')
        plt.show()

    def plot_intense(self, df):
        # get times
        plt.plot(df['Date'], df['Intensity'])
        plt.ylabel('Intensity')
        plt.xlabel('Time')
        plt.show()
            
    def to_csv(self, df):
        df.to_csv('inte.csv', sep=',')
            
    def average_intensity(self, im):
        return ImageStat.Stat(im).mean[0]

    def call_back(self, image):
        # calculate the average intensity in the image
        intensity = self.average_intensity(image)
        # show the image
        # image.show()
        # store image intensity in class variable
        self.image_intensity = intensity
        self.inte.append(intensity)
        # format the date
        self.dates.append(datetime.datetime.now().strftime("(%m-%d) %H:%M:%S"))
        # create a dataframe with date/time and corresponding intensity
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

    def daytime(self):
        w = Webcam()
        w.start()
        im = w.grab_image()
        intensity = self.average_intensity(im)
        w.stop()
        if intensity > 70.0:
            return True
        return False

    def get_color(self):
        w = Webcam()
        w.start()
        im = w.grab_image()
        colors = np.array(im)
        w.stop()
        color_key = {'[1, 2, 3]': 1}
        color_list = []
        
        # check each element
        for i in range(len(colors)):
            for j in range(len(colors[i])):
                color_list.append(str(colors[i][j]))
                try:
                    color_key[str(colors[i][j])] += 1
                except:
                     color_key[str(colors[i][j])] = 1

        dd = collections.defaultdict(list)
        for k, v in color_key.items():
            dd[v].append(k)
            x = sorted(dd.items())
        
        common_num = color_key[x[-3][1][0]]     # occurance of common color
        self.pro_color = common_num/len(color_list)
        print(color_key[x[-3][1][0]])

        return x[-3][1][0]
        

if __name__ == '__main__':
    # create csv file
    # with open('intensities.csv', 'w+') as f:
    #     f.write('Date/Time, Intensity')
        
    # print(datetime.datetime.now())
    cam = MUCamera()
    # cam.get_image()
    # cam.filtered_average_intensity()
    print(cam.get_color())
    print(cam.pro_color)