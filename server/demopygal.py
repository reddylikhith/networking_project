import pygal
b_chart=pygal.Bar()
b_chart.title="Density Ratio"
b_chart.add("A",[0.94])
b_chart.add("B",[1.05])
b_chart.add("C",[1.10])
b_chart.render_in_browser()
