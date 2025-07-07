from dash import Dash, html, Input, Output, State, callback, dcc
import dash
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
import base64
import io
import os 


###############################################################################################
# Functions
###############################################################################################
def show_plot(df_plot, ri="RI", val="Value"):
    #df_plot = df_plot[df_plot[ri].notna()]
    df_plot = df_plot.dropna()
    
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=df_plot[ri], y=df_plot[val], mode="lines", line=dict(width=0.4))
    )

    fig.update_layout(
        title="GC-Chromatogram",
        width=600,  
        height=400,
        xaxis_title="Retention Index (RI)",
        yaxis_title="Intensity/counts",
    )

    return fig


def calculate_RI(Rt, Retentionszeit, Alkan):
    if Rt <= Retentionszeit[0]:
        return None

    for i in range(len(Retentionszeit) - 1):
        if Retentionszeit[i] < Rt <= Retentionszeit[i + 1]:
            return 100 * (
                Alkan[i]
                + (
                    (Rt - Retentionszeit[i])
                    / (Retentionszeit[i + 1] - Retentionszeit[i])
                )
            )

    return None



def transform_data(df_Alk, df_Raw, c_time, c_int):
    # extract the retention times and retention indices from the CSV file:
    print(df_Alk.columns)
    Retentionszeit = df_Alk["Retentionszeit"].tolist()
    Alkan = df_Alk["Alkan"].tolist()
    # transform time column into retention index:
    df_Raw.iloc[:, c_time] = df_Raw.iloc[:, c_time].apply(
        lambda x: calculate_RI(x, Retentionszeit, Alkan))
    # adds only the new RI column and raw intensity column in the new data frame:
    df_Raw = df_Raw.iloc[:, [c_time, c_int]]

    return df_Raw 


###############################################################################################
# Application
###############################################################################################

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
)  
server = app.server


app.layout = dbc.Container(
    [  # Overhead Navigation Bar with the Logo and a Title
        dbc.Navbar(
            [
                dbc.NavbarBrand(
                    [
                        html.Img(
                            src=dash.get_asset_url("TUD_Logo.png"),
                            height="40px",
                            style={
                                "marginRight": "20px",
                                "marginLeft": "10px",
                            },
                        ),
                        "Rt-to-RI",
                    ],
                    href="/",
                    className="mr-4",
                    style={"color": "white"},
                ),
            ],
            color = "#00305d",
        ),
        # imports the page structure
        dbc.Container(
            [
                html.Div(
                    [
                        html.Br(),
                        html.P(
                            [
                                "Rt-to-RI is a Python tool that converts the retention time (Rt) into the corresponding retention index (RI). The resulting data set can be imported into a visualisation programme and used to display GC chromatograms with the RI instead of the Rt on the abscissa.",
                                html.Br(),
                                html.Hr(),
                                html.Strong("How do I use this application?"),
                                html.Br(),
                                "1) Download the template in which you fill in the retention times of the alkanes.",
                                html.Ul(
                                    [
                                        html.Li("Column 'Alkan' contains the number of C-atoms (do not chance the numbers)."),
                                        html.Li("Column 'Retentionszeit' contains the retention time of the alkane with comma as numeric separator. -> Enter your measured retention times here!"),
                                        html.Li("Measurement of the alkane mixture must be done with the same chromatographic system as your sample from which you want to convert your raw data."),
                                    ],
                                    style={
                                        'margin-left': '10px',
                                        'margin-bottom': '4px'
                                    }
                                ),
                                "2) Fill in the drop-down fields. Note the conditions in your sample measurement raw data file. (The file must be in csv or txt format.)",
                                html.Br(),
                                "3) Upload the completed alkanmix file to the field provided. Then upload your raw file provided.",
                                html.Br(),
                                "4) A preview image will now appear. You can download the converted file using the button provided.",
                                html.Br(),
                                html.Br(),
                            ]
                        ),

                        dbc.Row(
                            [                              
                                html.Hr(style={"border-top": "5px solid #00305d"}),
                                dbc.Col(
                                    [
                                        html.P('1) Download the template for the alkane mix:'),
                                        dbc.Button(
                                            "Download alkane mix template",
                                            id="download-button-alkan",
                                            className="mt-3",
                                            disabled=False,
                                            style={
                                                "background-color": "grey",
                                                "height": "60px",
                                                "width": "87%",
                                                "font-size": "20px",
                                                "font-weight": "bold",
                                                "border-color": "grey",
                                                "borderRadius": "5px",
                                                "lineHeight": "40px",
                                                "textAlign": "center",
                                                "margin": "10px"
                                            },
        
                                        ),
                                        # Component for downloading data
                                        dcc.Download(id="download-alkan"),
                                        html.Br(),
                                        html.Br(),
                                    ]
                                ),

                                dbc.Col(
                                    [
                                        # leer, für das Layout
                                    ]
                                ),
                                html.Hr(style={"border-top": "5px solid #00305d"}),
                            ]
                        ),

                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                         html.P('2) Number of the column with time values in your raw data file:'),
                                         dcc.Dropdown(
                                             id='time-dropdown',
                                             options=[
                                                 {'label': str(i), 'value': i-1} for i in range(1, 6)
                                              ],
                                             placeholder='Select the number of the column',
                                         ),
                                    ]
                                ),

                                dbc.Col(
                                    [
                                        html.P('3) Number of the column with intensity values in your raw data file:'),
                                        dcc.Dropdown(
                                            id='int-dropdown',
                                            options=[
                                                {'label': str(i), 'value': i-1} for i in range(1, 6)
                                             ],
                                            placeholder='Select the number of the column',
                                        ),
                                        html.Br(),
                                    ]
                                ),
                                
                            ]
                        ),

                        dbc.Row(
                            [                              
                                dbc.Col(
                                    [
                                        html.P('4) Number of the first row with values for time and intensity:'),
                                        dcc.Dropdown(
                                            id='skip-dropdown',
                                            options=[
                                                {'label': str(i), 'value': i-1} for i in range(1, 101)
                                            ],
                                            placeholder='Select the number of the first row',
                                        ),
                                        html.Br(),
                                    ]
                                ),

                                dbc.Col(
                                    [
                                        # leer, für das Layout
                                    ]
                                ),
                                html.Hr(),
                            ]
                        ),

                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P('5) Decimal separator in your raw data file:'),
                                        dcc.Dropdown(
                                            id='num-sep-dropdown',
                                            options=[
                                                {'label': 'Comma to separate the decimal places (e.g. 12,34567)', 'value': ','},
                                                {'label': 'Dot to separate the decimal places (e.g. 12.34567)', 'value': '.'},
                                             ],
                                            placeholder='Select the decimal separator',
                                        ),       
                                    ]
                                ),

                                dbc.Col(
                                    [
                                        html.P('6) Separator between the columns in your raw data file:'),
                                        dcc.Dropdown(
                                            id='column-sep-dropdown',
                                            options=[
                                                {'label': 'Semicolon', 'value': ';'},
                                                {'label': 'Comma', 'value': ','},
                                                {'label': 'Tab stop', 'value': '\t'},                                        
                                                {'label': 'Space', 'value': ' '},
                                             ],
                                            placeholder='Select the column separator',
                                        ),
                                        html.Br(),
                                    ]
                                ),
                            ]
                        ),

                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P('7) Thousands separator in your raw data file:'),
                                        dcc.Dropdown(
                                            id='thou-sep-dropdown',
                                            options=[
                                                {'label': 'No mark for the separation of the thousands (e.g. 1234567)', 'value': 'None'},
                                                {'label': 'Comma to separate the thousands places (e.g. 1,234,567)', 'value': ','},
                                                {'label': 'Dot to separate the thousands places (e.g. 1.234.567)', 'value': '.'},
                                             ],
                                            placeholder='Select the thousands separator',
                                        ), 
                                            html.Br(),      
                                    ]
                                ),

                                dbc.Col(
                                    [
                                        # leer, für das Layout
                                    ]
                                ),

                                html.Hr(style={"border-top": "5px solid #00305d"}),
                            ]
                        ),

                        
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P(
                                            [
                                                "8) Please upload the 'Alkanmix.csv' file required.",
                                                html.Br(),
                                            ]
                                        ),
                                        dcc.Upload(
                                            id="alkanmix-upload",
                                            children=html.Div(
                                                [
                                                    "Drag or click ",
                                                    html.A(
                                                        "to select a file."
                                                    ),
                                                ]
                                            ),
                                            # Styling for the upload box
                                            style={
                                                "width": "90%",
                                                "height": "60px",
                                                "lineHeight": "60px",
                                                "borderWidth": "1px",
                                                "borderStyle": "dashed",
                                                "borderRadius": "5px",
                                                "textAlign": "center",
                                                "margin": "10px",
                                            },
                                        ),
                                        dcc.Store(id="stored-alkan"),
                                    ]
                                ),

                                dbc.Col(
                                    [
                                        html.P(
                                            [
                                                "9) Please upload the raw data file required.",
                                                html.Br(),
                                            ]
                                        ),
                                        dcc.Upload(
                                            id="data-upload",
                                            children=html.Div(
                                                [
                                                    "Drag or click ",
                                                    html.A(
                                                        "to select a file."
                                                    ),
                                                ]
                                            ),
                                            # Styling for the upload box
                                            style={
                                                "width": "90%",
                                                "height": "60px",
                                                "lineHeight": "60px",
                                                "borderWidth": "1px",
                                                "borderStyle": "dashed",
                                                "borderRadius": "5px",
                                                "textAlign": "center",
                                                "margin": "10px",
                                            },
                                        ),
                                        dcc.Store(id="stored-data"),
                                    ]
                                ),

                                html.Br(),
                                html.Hr(style={"border-top": "5px solid #00305d"}),
                            ]
                        ),
                        html.Div(
                            [
                                html.Center(id="graph-goeshere")
                            ]
                        ),
                        
                        html.P(
                            [
                                "This is an interactive preview image. Use the left mouse button to select an area and enlarge it by drawing a window. Double-click on the image with the left mouse button to zoom out again.",
                            
                                html.Hr(),

                            ],
                            style={
                                'font-size': '15px',
                                'color': "#7F888F"
                            }
                        ),
                        
                        html.Div(
                            [
                                dcc.Store(id="transformed-data"),
                                html.Div(
                                    [
                                        dbc.Button(
                                            "Download new CSV file",
                                            id="download-button",
                                            disabled=True,
                                            style={
                                                "background-color": "#00305d",
                                                'opacity': '1', 
                                                'border-color': 'transparent',
                                                "height": "100px",
                                                "width": "500px",
                                                "font-size": "24px",
                                                "font-weight": "bold"
                                            },
                                        ),
                                        # Component for downloading data
                                        dcc.Download(id="download-dataframe"),
                                    ],
                                    style={
                                        "display": "flex",
                                        "justify-content": "center",
                                        "align-items": "center"
                                    }
                                ),
                            ],           
                        ),
                        html.Br(),
                        html.Br(),
                    ]
                )
            ]
        ),
    ]
)


###############################################################################################
# CALLBACKS
###############################################################################################

@callback(
    Output("download-alkan", "data"),
    Input("download-button-alkan", "n_clicks"),
    prevent_initial_call=True,
)
def download_alkane(n_clicks):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "template", "Alkanmix.csv")
    df = pd.read_csv(
        file_path,
        sep=";", 
        decimal=","
        )
    return dcc.send_data_frame(
        df.to_csv, 
        filename="Alkanmix.csv", 
        sep = ";",
        decimal = ",",
        index=False)

@app.callback(
        Output("stored-alkan", "data"),
        Input("alkanmix-upload", "contents"))
def store_file_alkan(contents):
    if contents:
        content_type, content_string = contents.split(",")
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(
            io.StringIO(decoded.decode("iso-8859-1")),
            sep=";",
            decimal=",",
            on_bad_lines="skip",
        )
        return df.to_json(date_format="iso", orient="split")
    return None

@app.callback(
        Output("stored-data", "data"),
        Input("data-upload", "contents"), 
        State("skip-dropdown", "value"),
        State("num-sep-dropdown", "value"),
        State("column-sep-dropdown", "value"),
        State("thou-sep-dropdown", "value"),
        )
def store_file_data(contents, n_skip, num_sep, column_sep, thou_sep): 
    # falls Dropdowns nicht ausgefüllt werden:
    if n_skip is None:
        n_skip = 100
    
    if num_sep is None:
        num_sep = '.'
    
    if column_sep is None:
        column_sep = ','

    if thou_sep is None:
        thou_sep = None
   
    if thou_sep == 'None':
        thou_sep = None
 
    if contents:
        content_type, content_string = contents.split(",")
        decoded = base64.b64decode(content_string)
   
        try:
            df = pd.read_csv(
                io.StringIO(decoded.decode("utf-8")),
                sep=column_sep,
                decimal=num_sep,
                skiprows=n_skip,
                thousands=thou_sep,
            )
            return df.to_json(date_format="iso", orient="split")
        except UnicodeDecodeError:
            # wenn UTF8 nicht funktioniert, dann UTF16
            try:
                df = pd.read_csv(
                    io.StringIO(decoded.decode("utf-16")),
                    sep=column_sep,
                    decimal=num_sep,
                    skiprows=n_skip,
                    thousands=thou_sep,
                )
                return df.to_json(date_format="iso", orient="split")
            except UnicodeDecodeError:
                # wenn auch UTF16 nicht funktioniert, gibt es einen Fehler
                return None
    
    return None


# Create plot only if both files are uploaded
@app.callback(
    Output("graph-goeshere", "children"),
    Output("transformed-data", "data"),
    Output("download-button", "disabled"),
    Input("stored-alkan", "data"),
    Input("stored-data", "data"),
    State("time-dropdown", "value"),
    State("int-dropdown", "value"),
)
def update_graph(json_alkan, json_data, c_time, c_int):
    # falls Dropdowns nicht ausgefüllt werden
    if c_time is None:
        c_time = 0
    
    if c_int is None:
        c_int = 1

    if json_alkan and json_data:
        alkan = pd.read_json(json_alkan, orient="split")
        data = pd.read_json(json_data, orient="split")
        print(data.columns)
        data_transf = transform_data(alkan, data, c_time, c_int)
        data_transf.columns = ["RI", "Value"] + list(data_transf.columns[2:])
        return (
            dcc.Graph(figure=show_plot(data_transf, "RI", "Value")),
            data_transf.to_json(date_format="iso", orient="split"),
            False,
        )
    return None, None, True


@callback(
    Output("download-dataframe", "data"),
    Input("download-button", "n_clicks"),
    State("transformed-data", "data"),
    prevent_initial_call=True,
)
def download(_, data_json):
    """Downloads the updated csv file"""
    if data_json:
        df = pd.read_json(data_json, orient="split")
        return dcc.send_data_frame(
            df.to_csv, 
            filename="transformed_data_file.csv", 
            index=False
        )


###############################################################################################

if __name__ == "__main__":
    app.run(debug=True)
