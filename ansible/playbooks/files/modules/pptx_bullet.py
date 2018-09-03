#!/bin/env python
from pptx import Presentation
import sys
from pptx import Presentation
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches

def main():
  module = AnsibleModule(
    argument_spec=dict(
      filename = dict(required=True),
      title = dict(required=True),
      bullets = dict(required=True, type='list')
      ),
      supports_check_mode=False
  )
  try:
    filename = module.params['filename']
    prs = Presentation(filename)
    
    bullet_slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(bullet_slide_layout)
    shapes = slide.shapes
    title_shape = shapes.title
    body_shape = shapes.placeholders[1]
    title_shape.text = module.params['title']
    bullets = module.params['bullets']
    tf = body_shape.text_frame
    tf.text = 'Topics for discussion'
    
    for topic in bullets:
      if topic: 
        p = tf.add_paragraph()
        p.text = topic
        p.level = 1
      
    prs.save(filename)
    module.exit_json(changed=True)
  except:
    pass
    #print sys.exc_info()[0]
    #raise
    #module.fail_json(msg=sys.exc_info()[0])

from ansible.module_utils.basic import *
main()
