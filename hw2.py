#!/usr/bin/env python3


from webcam import *
from PIL import ImageStat

def get_image():
    w = Webcam()
    
    w.register_callback(callback, 1)
    w.start()
    
    input('\nHit Enter to Stop\n')
    im = w.grab_image()     # the current image of MU
    intensity = ImageStat.Stat(im).mean[0]
    im.show()
    intensity = ImageStat.Stat(im).mean[0]
    print('Average Intensity: ' + str(intensity))
    

    w.stop()
    
    print('Average Intensity: ' + str(intensity))

    print('hello_world!')
def avg_intensity(img):
    return 'HELLO!!!!'


if __name__ == '__main__':
    get_image()