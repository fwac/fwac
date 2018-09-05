#!/bin/env python
from pptx import Presentation
import sys
from pptx import Presentation
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches

def table_create(prs,position,title_text,table_header,table_data):
  try: 
    cols = position['cols']
    rows = position['rows']
    left = top = Inches(position['left'])
    width = Inches(position['width'])
    height = Inches(position['height'])

    title_only_slide_layout = prs.slide_layouts[5]
    slide = prs.slides.add_slide(title_only_slide_layout)
    shapes = slide.shapes
    shapes.title.text = title_text
    table = shapes.add_table(rows, cols, left, top, width, height).table
  
    x = 0
    for key,value in table_header.iteritems():
      table.columns[x].width = Inches(value)
      table.cell(0, x).text = key
      x += 1
    
    for y in xrange(0, len(table_data)):
      for x in xrange(0, cols):
        table.cell(y+1, x).text = " ".join(table_data[y][x])
  except:
    print sys.exc_info()[0]
    raise

def main():
  module = AnsibleModule(
    argument_spec=dict(
      filename = dict(required=True),
      title = dict(required=True),
      position = dict(required=False, type='dict', default={'cols': 5, 'rows': 10, 'left': 1.0 , 'top': 2.0, 'width': 8.0, 'height': 0.8 }),
      table_data = dict(required=True, type='list'),
      table_header = dict(required=False, type='dict', default={'Name': 2.0, 'Project': 1.0, 'Role': 2.0 , 'Ansible': 1.0, 'Email': 2.0 })
      ),
      supports_check_mode=False
  )
  try:
    table_data = module.params['table_data']
    title_text = module.params['title']
    filename = module.params['filename']
    position = module.params['position']
    table_header = module.params['table_header']
    rows = position['rows']

    prs = Presentation(filename)   
    #for i in range(0, len(table_data), rows):
    #  table_create(prs,position,title_text,table_header,table_data[i:i + rows])
    table_create(prs,position,title_text,table_header,table_data)
    prs.save(filename)
    module.exit_json(changed=True)
  except:
    print sys.exc_info()[0]
    raise

from ansible.module_utils.basic import *
main()
