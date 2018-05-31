#!/usr/bin/env python3
import pandas as pd
import hw2
import csv
import matplotlib.pyplot as plt
import math
import operator
import collections

def mean_filter(l, width=3):
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
    

def filtered_average_intensity():
    df = pd.read_csv('inte.csv')
    inte = df['Intensity'].tolist()
    dates = df['Date'].tolist()
    
    
    # clean up data (remove repeats)
    # for i in range(len(inte) - 1):
    #     if inte[i] == inte[i+1]:
    #         del inte[i]
    #         del dates[i]

    # perform movmean averaging on data to smooth
    # inte = mean_filter(inte, 3)
    inte = mean_filter(inte, 150)
    print(inte)
    # print(dates)
    index = list(range(len(inte)))
    
    # plot the graph
    plt.plot(index, inte)
    plt.ylabel('Intensity')
    plt.xlabel('Time')
    plt.show()

def color(color_key):
    d = color_key
    dd = collections.defaultdict(list)
    for k, v in d.items():
        dd[v].append(k)
    x = sorted(dd.items())


    return x[-2]
if __name__ == '__main__':
    trial_key = {'blue': 2000, 'red': 1, 'green': 10, 'yellow': 2001}
    print(color(trial_key))