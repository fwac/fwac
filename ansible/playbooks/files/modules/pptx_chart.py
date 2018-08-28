#!/usr/bin/python
from pptx import Presentation
import sys


def bar_chart(obj):
  slide = obj.slides.add_slide(prs.slide_layouts[5])
  chart_data = ChartData()
  chart_data.categories = ['East', 'West', 'Midwest']
  chart_data.add_series('Series 1', (19.2, 21.4, 16.7))
  x, y, cx, cy = Inches(2), Inches(2), Inches(6), Inches(4.5)
  slide.shapes.add_chart(
      XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data
  )
  return obj

def main():
  module = AnsibleModule(
    argument_spec=dict(
      filename = dict(required=True),
      categories = dict(required=True, type='list'),
      series_name = dict(required=True),
      series_values = dict(required=True),
      chart_type = dict(type= 'str', choices=['bar', 'pie']),
      ),
      supports_check_mode=False
  )
  filename = module['filename']
  categories = module['categories']
  series_name = module['series_name']
  series_values = module['series_values']
  chart_type = module['chart_type']
  try:
    prs = Presentation(filename)
    if chart_type == 'bar':
      prs = bar_chart(prs)
    else if chart_type == 'pie':
      prs = pie_chart(prs)
    prs.save(filename)

    module.exit_json(changed=True)
  except:
    module.fail_json(msg=sys.exc_info()[0])

from ansible.module_utils.basic import *
main()
