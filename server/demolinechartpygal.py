import pygal
line_chart=pygal.Line()
line_chart.title="Browser usage in (%)"
line_chart.x_labels=map(str,range(2015,2022))
line_chart.add("Chrome",[1,20,35,38,45,50,60,75])
line_chart.add("Firefox",[None,0,23,38,45,50,54,60])
line_chart.render_in_browser()

