#!/usr/bin/env python

from os import path
from PIL import Image
import numpy as np
import os
from wordcloud import WordCloud

def main():
  module = AnsibleModule(
    argument_spec=dict(
      image_file = dict(required=True),
      mask_file = dict(required=False),
      width = dict(required=False, type='int', default=820),
      height = dict(required=False, type='int', default=400),
      background_color = dict(required=False, default='None'),
      contour_color = dict(required=False, default='white'),
      mode = dict(required=False, default='RGBA'),
      word_file = dict(required=False),
      words = dict(required=False)
      ),
      supports_check_mode=False
  )
  try:
    image_file = module.params['image_file']
    mask_file = module.params['mask_file']
    background_color = module.params['background_color']
    contour_color = module.params['contour_color']
    word_file = module.params['word_file']
    height = module.params['height']
    width = module.params['width']
    mode = module.params['mode']

    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    # # d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    # # text = open(path.join(d, word_file)).read()    
    
    #ansible_mask = np.array(Image.open(path.join(d, mask_file)))
    wc = WordCloud(background_color=None, colormap='PRGn', max_words=2000, mode=mode, height=height, width=width)
    # # wc.generate(text)
    wc.generate(words)
    
    # # wc.to_file(path.join(d, image_file))
    wc.to_file(image_file)
    module.exit_json(changed=True)
  except:
    pass
    #print sys.exc_info()[0]
    #raise
    

from ansible.module_utils.basic import *
main()
