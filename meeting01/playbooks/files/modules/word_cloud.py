#!/usr/bin/env python

from wordcloud import WordCloud

def main():
  module = AnsibleModule(
    argument_spec=dict(
      image_file = dict(required=True),
      mask_file = dict(required=False),
      width = dict(required=False, type='int', default=820),
      height = dict(required=False, type='int', default=400),
      background_color = dict(required=False, default=None),
      contour_color = dict(required=False, default='white'),
      mode = dict(required=False, default='RGB'),
      colormap = dict(required=False, default='binary'),
      words = dict(required=False)
      ),
      supports_check_mode=False
  )
  try:
    image_file = module.params['image_file']
    mask_file = module.params['mask_file']
    background_color = module.params['background_color']
    contour_color = module.params['contour_color']
    words = module.params['words']
    height = module.params['height']
    width = module.params['width']
    mode = module.params['mode']
    colormap = module.params['colormap']
    
    #make words more pretty 
    nocommas = words.replace(',','')
    words = nocommas.capitalize()
    
    wc = WordCloud(background_color=background_color, colormap=colormap, max_words=2000, mode=mode, height=height, width=width)
    wc.generate(words)
    wc.to_file(image_file)
    
    module.exit_json(changed=True)
  except:
    pass
    #print sys.exc_info()[0]
    #raise
    
from ansible.module_utils.basic import *
main()
