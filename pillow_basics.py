#!/usr/bin/env python3
from PIL import Image
import os

#from where program will read the images
directory = "images/"

#where program will save final images
output_directory = "/opt/icons/"

#rotate, resize and convert into .jpeg 
for filename in os.listdir(directory):
        if filename != ".DS_Store":
                im = Image.open(os.path.join(directory, filename))
                im = im.rotate(-90)
                im = im.resize((128,128))
                im = im.convert("RGB")
                im.save(os.path.join(output_directory, filename+".jpeg"))
                