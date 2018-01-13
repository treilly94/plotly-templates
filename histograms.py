import plotly.offline as pyoff
import plotly.graph_objs as go


class Hist:

    bar_mode = ""

    def __init__(self, data):

        data = self.get_data(data)
        layout = self.get_layout()
        fig = go.Figure(data=data, layout=layout)

        pyoff.iplot(fig)

    def get_layout(self):

        layout = go.Layout(barmode=self.bar_mode,
                           xaxis=dict(autotick=True,
                                      ticks='outside')
                           )
        return layout

    def get_data(self, series):

        trace = go.Histogram(
                x=series,
                opacity=0.75
            )
        return [trace]


class OverlayHist(Hist):

    bar_mode = "overlay"

    def get_data(self, series):

        data = []
        for s in series:
            trace = go.Histogram(
                x=s,
                opacity=0.75
            )
            data.append(trace)
        return data
