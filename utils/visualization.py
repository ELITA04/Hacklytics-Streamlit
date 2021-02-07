import librosa
import librosa.display
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def create_piechart():
    labels = ['Stressed And Anxious', 'No Effect']
    values = ['138', '39']
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    st.plotly_chart(fig)

def create_waveplot(data, sampling_rate):
    plt.figure(figsize=(8, 3))
    plt.title('Waveplot for audio ', size=15)
    librosa.display.waveplot(data, sr=sampling_rate)
    st.pyplot()

def create_spectrogram(data, sampling_rate):
    X = librosa.stft(data)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(8, 3))
    plt.title('Spectrogram for audio ', size=15)
    librosa.display.specshow(Xdb, sr=sampling_rate, x_axis='time', y_axis='hz')   
    plt.colorbar()
    st.pyplot()


def create_barchart():
    df = pd.read_csv('dataset_plots/teachers.csv')
    field_1 = ['YES', 'NO']
    field_1_counts = [831,351]
    # Use the hovertext kw argument for hover text
    fig = go.Figure(data=[go.Bar(x=field_1, y=field_1_counts,
                hovertext=['Response:Yes', 'Response:No'])])
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
    fig.update_layout(title_text='Responses to the survey question "Do you find yourself more connected <br> with your family, close friends , relatives  ?"')
    st.plotly_chart(fig)


def create_multibarchart():
    labels = ['None', 'Mild', 'Moderate', 'Severe']
    colors = ['rgba(125, 119, 119, 0.8)', 'rgba(222, 199, 49, 0.8)', 'rgba(224, 99, 40, 0.8)', 'rgba(237, 25, 21, 0.8)']

    x_data = [       
                [92,  5,  3, 0],
                [56, 29, 10,  5],
                [46, 15, 28, 11],
                [41, 30, 17, 12],
                [33, 22, 19, 25],
                [30, 23, 30, 17],
                [18, 31, 31, 19],
                [14, 28, 26, 32],
                [14, 21, 27, 38],
                [11, 21, 36, 32],
                [9, 31, 44, 16],]

    y_data = [  'Suicidal thoughts',
                'Depressive thoughts',
                'Increased class workload',
                'Financial difficulties',
                'Disruptions in eating patterns',
                'Changes in living environment',
                'Academic performance',
                'Increased social isolation',
                'Disruption in sleep patterns',
                'Difiiculty concentrating', 
                'Concerns on health', 
                ]

    fig = go.Figure()

    for i in range(0, len(x_data[0])):
        for xd, yd in zip(x_data, y_data):
            fig.add_trace(go.Bar(
                x=[xd[i]], y=[yd],
                orientation='h',
                marker=dict(
                    color=colors[i],
                    line=dict(color='rgb(248, 248, 249)', width=1)
                )
            ))

    fig.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.15, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=120, r=10, t=140, b=80),
    showlegend=False,
    )

    annotations = []

    for yd, xd in zip(y_data, x_data):
        # labeling the y-axis
        annotations.append(dict(xref='paper', yref='y',
                                x=0.14, y=yd,
                                xanchor='right',
                                text=str(yd),
                                font=dict(family='Arial', size=14,
                                        color='rgb(67, 67, 67)'),
                                showarrow=False, align='right'))
        # labeling the first percentage of each bar (x_axis)
        annotations.append(dict(xref='x', yref='y',
                                x=xd[0] / 2, y=yd,
                                text=str(xd[0]) + '%',
                                font=dict(family='Arial', size=14,
                                        color='rgb(248, 248, 255)'),
                                showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations.append(dict(xref='x', yref='paper',
                                x=xd[0] / 2, y=1.1,
                                text=labels[0],
                                font=dict(family='Arial', size=14,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
        # labeling the rest of percentages for each bar (x_axis)
        annotations.append(dict(xref='x', yref='y',
                                x=space + (xd[i]/2), y=yd,
                                text=str(xd[i]) + '%',
                                font=dict(family='Arial', size=14,
                                            color='rgb(248, 248, 255)'),
                                showarrow=False))
        # labeling the Likert scale
        if yd == y_data[-1]:
            annotations.append(dict(xref='x', yref='paper',
                                    x=space + (xd[i]/2), y=1.1,
                                    text=labels[i],
                                    font=dict(family='Arial', size=14,
                                                color='rgb(67, 67, 67)'),
                                    showarrow=False))
        space += xd[i]

    fig.update_layout(annotations=annotations)
    st.plotly_chart(fig)

    
