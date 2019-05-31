#C:\Python34\Lib\site-packages\;all iofo from hereh  ttps://plot.ly/python/line-charts/ 
import plotly.plotly as py
import plotly.graph_objs as go
import plotly


month = [i for i in range(1,12*3+1)]

uSergei= go.Scatter(
    x = month,
    y=[None, None ,None , None, 11000, 14100, 16109, 11230, 4000, 10700, 17626, 43245, 17200, 29177, 24377, 26406, 15000, 21153, 20805, 17905, 11962, 18614, 7904,
        24662, 21000, 34442, 34420],
    mode = 'lines+markers', # 'markers', 'lines'
    name = 'Sergei',
    line=dict(shape='spline',  # spline options include 'linear', 'vh', 'hv', 'vhv', 'hvh'
        #color = ('rgb(205, 12, 24)'),
        #wconnectgaps=True,
        width = 1,
        dash = 'dash') # dash options include 'dash', 'dot', and 'dashdot'v
    )

uOleg = go.Scatter(
    x = month,
    y = [28400,	73070,	47690,	43760,	31900,	33410,	31267,	30548,	30519,	31182,	59133,	36265	,33726	,21248	,28328	,22115	,31000	,24876	,20885	,39335	,36847	,48424	,31908	,16931	,26947	,35910	,34144],
    mode = 'lines+markers',
    name = 'Oleg',
    line=dict(shape='spline'),
    )

uDima = go.Scatter(
    x = month,
    y = [24840	,47260	,59390	,41620	,39885	,35550	,39921	,38465	,49560	,29167	,66057	,53354	,24349	,40430	,28218	,26547	,45428	,41380	,46589	,41289	,52398	,45868	,34502	,34572	,33764	,89500	,49186],
    mode = 'lines+markers',
    line=dict(shape='spline'),
    name = 'Dima')

uNataly = go.Scatter(
    x = month,
    y = [5000	,13160	,27000	,20645	,12810	,19417	,23624	,9491	,17330	,26670	,37370	,22575	,20075	,21850	,11450	,17200	,28042	,27614	,25365	,12045	,18630	,19147	,19469	,12514	,0	,33516	,26263],
    mode = 'lines+markers',
    line=dict(shape='spline'),
    name = 'Nataly')


uVeronika = go.Scatter(
    x = month,
    y = [None,None,None,None,None,None,None,None,None,None,None,None,	11045	,10345	,18345	,19145	,17000	,24300	,31860	,15000	,25200	,26356	,13000	,6620	,14523	,25100	,32090	,25255],
    mode = 'lines+markers',
    line=dict(shape='spline'),
    name = 'Veronika')

uElena = go.Scatter(
    x = month,
    y = [6000	,12600	,16650	,30220	,22876	,0	,28529	,18958	,28888	,17388	,35520	,37650	,39650	,26200	,29000	,21020	,38600	,23600	,27200	,32780	,29530	,24111	,30003	,20670	,30000	,42711	,48320],
    mode = 'lines+markers',
    line=dict(shape='spline'),
    name = 'Elena')


data = [uSergei, uDima, uNataly, uVeronika, uElena]

#plotly.offline.plot({
py.iplot({
    "data":data, 
    "layout": go.Layout(title="COLOR Wages")
}, auto_open=True)
