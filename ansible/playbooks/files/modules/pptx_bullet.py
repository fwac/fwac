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
      title = dict(default=True),
      bullet = dict(default=True),
      ),
      supports_check_mode=False
  )
  try:
    prs = Presentation()
    bullet_slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(bullet_slide_layout)
    shapes = slide.shapes
    title_shape = shapes.title
    body_shape = module.params['title']
    tf = body_shape.text_frame
    tf.text = 'Topics for discussion'
    for topic in bullet:
      p = tf.add_paragraph()
      p.text = topic
      p.level = 1
    prs.save(module.params['filename'])
    module.exit_json(changed=True)
  except:
    module.fail_json(msg=sys.exc_info()[0])

from ansible.module_utils.basic import *
main()