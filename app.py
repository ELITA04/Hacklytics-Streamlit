import io
import pickle
import librosa
import librosa.display
import pandas as pd
import numpy as np
import base64
import matplotlib.pyplot as plt

from utils.toc import Toc
from utils.AudioPredict import get_features, predict
from utils.visualization import create_multibarchart, create_barchart, create_piechart, create_spectrogram, create_waveplot

import streamlit as st
import streamlit.components.v1 as components
from pydub import AudioSegment
import plotly.graph_objects as go



@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

def main():
    toc = Toc()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    set_png_as_page_bg('dataset_plots/Background.jpg')

    toc.title('Mood Boost 🧠😄')
    #Visualizations
    toc.header("📊 Visualizations")
    toc.subheader("1. Effects of COVID-19 on College Students' Mental Health in the US : Interview Survey")
    st.markdown('#### Challenges to College Students Mental Health ')
    create_piechart()

    st.markdown('#### Participants ratings of mental health aspects in order of negative impacts')
    create_multibarchart()

    toc.subheader('2. Kaggle : Survey On Indian Students')
    create_barchart()

    toc.subheader('3. Sucide rates by State from 2015 - 2020')
    st.image('dataset_plots/heatmap.jpg')
    
    # uploading the file and getting the results
    toc.header("🎤 Voice based Emotion Detection")
    uploaded_file = st.file_uploader("Select file from your directory")
    if uploaded_file is not None:
        audio_bytes = uploaded_file.read()
        # st.audio(audio_bytes, format='audio/mp3')

        file_var = AudioSegment.from_file(io.BytesIO(audio_bytes), format = 'wav')
        file_var.export(uploaded_file.name[:-4] + '.wav', format='wav')   
        wav_file =  uploaded_file.name[:-4]+'.wav'
        data, sampling_rate = librosa.load(wav_file)

        (text, link) = predict(data, sampling_rate, wav_file)
        st.markdown(f'### {text}')
        st.markdown(f"![Alt Text]({link})")
        
        create_waveplot(data, sampling_rate)
        create_spectrogram(data, sampling_rate)

    toc.placeholder()
    toc.generate()

if __name__ == "__main__":
    main()