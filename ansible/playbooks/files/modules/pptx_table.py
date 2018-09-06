#!/bin/env python
# this module should be called lalaloopy
from pptx import Presentation
from pptx.util import Inches
import sys

def table_size(data, size):
    for i in xrange(1, len(data), size):
        yield data[i:i + size]
        
def table_create(prs,position,title_text,table_header,table_data):
  try: 
    cols = position['cols']
    rows = position['rows']
    top = position['top']
    l = ['Name','Project','Role','Ansible','Email']
    left = Inches(position['left'])
    width = Inches(position['width'])
    height = Inches(position['height'])

    for data in table_size(table_data,rows):
      title_only_slide_layout = prs.slide_layouts[5]
      slide = prs.slides.add_slide(title_only_slide_layout)
      shapes = slide.shapes
      shapes.title.text = title_text
      table = shapes.add_table(rows, cols, left, top, width, height).table
    
      for i in xrange(0, len(table_header)):
        table.columns[i].width = Inches(table_header[i])
        table.cell(0, i).text = l[i]
      
      for y in xrange(0, len(data)):
        for x in xrange(0, cols):
          table.cell(y+1, x).text = data[y][x]
  except:
    print sys.exc_info()[0]
    raise

def main():
  module = AnsibleModule(
    argument_spec=dict(
      filename = dict(required=True),
      title = dict(required=True),
      position = dict(required=False, type='dict', default={'cols': 5, 'rows': 9, 'left': 0.6 , 'top': 2.0, 'width': 10.0, 'height': 0.8 }),
      table_data = dict(required=True, type='list'),
      table_header = dict(required=False, type='list', default=[2.5,1.5,3.0,2.0,3.0])
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
    table_create(prs,position,title_text,table_header,table_data)
    prs.save(filename)
    module.exit_json(changed=True)
  except:
    print sys.exc_info()[0]
    raise

from ansible.module_utils.basic import *
main()
