import pygal
pie_chart=pygal.Pie()
pie_chart.title="Protocol Details"
pie_chart.add("TCP",15)
pie_chart.add("UDP",30)
pie_chart.add("ICMP",45)
pie_chart.add("Others",10)
pie_chart.render_in_browser()
#pie_chart.render_to_file("pie_chart.png")