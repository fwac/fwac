#!/usr/bin/env python
"""
Masked wordcloud
================

Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import os

from wordcloud import WordCloud, STOPWORDS

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'playbook.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/ansible%20in%20wonderland/255fk.jpg
ansible_mask = np.array(Image.open(path.join(d, "ansible_mask.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="black", max_words=2000, mask=ansible_mask,stopwords=stopwords, contour_color="white")

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "ansible.png"))
os.system('convert ansible_mask.png ansible.png ansible_negate.png -composite ansible_cloud.png')
os.system('gdrive upload ansible_cloud.png')

