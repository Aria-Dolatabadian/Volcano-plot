import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_bio as dashbio
from dash import html, dcc

app = dash.Dash(__name__)
#Copy your data file in working directory
df = pd.read_csv('volcano_data1.csv')

app.layout = html.Div([
    'Effect sizes',
    dcc.RangeSlider(
        id='default-volcanoplot-input',
        min=-3,
        max=3,
        step=0.05,
        marks={i: {'label': str(i)} for i in range(-3, 3)},
        value=[-0.5, 1]
    ),
    html.Br(),
    html.Div(
        dcc.Graph(
            id='dashbio-default-volcanoplot',
            figure=dashbio.VolcanoPlot(
                dataframe=df
            )
        )
    )
])

@app.callback(
    Output('dashbio-default-volcanoplot', 'figure'),
    Input('default-volcanoplot-input', 'value')
)
def update_volcanoplot(effects):
    return dashbio.VolcanoPlot(
        dataframe=df,
        genomewideline_value=2.5,
        effect_size_line=effects
    )

if __name__ == '__main__':
    app.run_server(debug=True)
