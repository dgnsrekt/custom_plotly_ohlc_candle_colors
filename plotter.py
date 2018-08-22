from download import get_pickle
import plotly.offline as py
import plotly.graph_objs as go

from plotly.figure_factory import utils
from plotly.figure_factory._ohlc import validate_ohlc

import pandas as pd
from random import choices

COLORS = dict(GREEN = '#009237',
             WHITE = '#333333',
             RED = '#82000F',
             YELLOW = '#FFFF41')

df = get_pickle()

df['color']= choices(list(COLORS.keys()), k=len(df))


class ColoredCandles:
    def __init__(self, dataframe, **kwargs):
        self.dataframe = dataframe

    def make_colored_candles(self):
        candle_data = []
        for idx, data in self.dataframe.iterrows():
            y = [data.low, data.open, data.close,
                data.close, data.close, data.high]
            # id = ['low', 'open', 'close',
                 # 'close', 'cose']
            x = [idx, idx, idx, idx, idx, idx]
            candle_data.append(go.Box(y=y,x=x,
                                      whiskerwidth=0,
                                      boxpoints=False,
                                      showlegend=False,
                                      name='candle',
                                      fillcolor=COLORS[data.color],
                                      marker=dict(color=COLORS[data.color])))
        return candle_data

    def create_candle_plot(self):
        candle_data = self.make_colored_candles()
        axisx = dict(tickfont=dict(family='Arial, sans-serif',
                                   size=10,
                                   color='white'),
                                   rangeslider=dict(visible=False))
        axisy = dict(tickfont=dict(family='Arial, sans-serif',
                                   size=10,
                                   color='white'),
                     tickformat='.8f')
        layout = go.Layout(
                font=dict(family='Arial, san-serif', size=12, color='white'),
                autosize=True,
                yaxis=axisy,
                xaxis=axisx,
                paper_bgcolor='black',
                plot_bgcolor='black')
        return go.Figure(data=candle_data, layout=layout)


candle = ColoredCandles(df)
py.plot(candle.create_candle_plot())
