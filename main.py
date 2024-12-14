import os
import sys
import time
import numpy as np
from PIL import Image
from image_converter import ImageConverter

# Automatically add the 'lib' directory relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(script_dir, 'lib')
pic_path = os.path.join(script_dir, 'pic')
sys.path.append(lib_path)
from waveshare_epd import epd4in2_V2

def main():
    epd = epd4in2_V2.EPD()
    epd.init()
    epd.Clear()

    epd.Init_4Gray()

    bmp_image_path = ImageConverter.to_bmp('pic/image.jpg', 'pic/image.bmp')
    bmp_image = Image.open(bmp_image_path)
    buf2 = epd.getbuffer_4Gray(bmp_image)
    epd.display_4Gray(epd.getbuffer_4Gray(bmp_image))
    time.sleep(5)

    epd.init()
    epd.Clear()
    epd.sleep()

if __name__ == "__main__":
    main()


