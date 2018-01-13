import plotly.offline as pyoff
import plotly.graph_objs as go


class Bar:

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

        trace = go.Bar(
                y=series,
                opacity=0.75
            )
        return [trace]
