import streamlit as st
from pydub import AudioSegment
from utils.toc import Toc
import plotly.graph_objects as go
import pandas as pd
import io
import librosa
import librosa.display
import matplotlib.pyplot as plt

#from utils.visualization import create_waveplot

@st.cache
def predict(uploaded_file):
    """
    Runs the model to find the mood
    Then provides some images to boost the mood
    """
    loc = AudioPredict.return_image(uploaded_file)
    return loc

def main():
    toc = Toc()

    st.set_option('deprecation.showPyplotGlobalUse', False)

    toc.title('Title here 😄😐😟')
    # uploading the file and getting the results
    toc.header("📁 Choose a file")
    uploaded_file = st.file_uploader("Select file from your directory")
    if uploaded_file is not None:
        audio_bytes = uploaded_file.read()
        st.audio(audio_bytes, format='audio/mp3')

        file_var = AudioSegment.from_file(io.BytesIO(audio_bytes), format = 'wav')
        file_var.export(uploaded_file.name[:-4] + '.wav', format='wav')   
        wav_file =  uploaded_file.name[:-4]+'.wav'
        data, sampling_rate = librosa.load(wav_file)
        
        # create a waveplot
        plt.figure(figsize=(8, 3))
        plt.title('Waveplot for audio ', size=15)
        librosa.display.waveplot(data, sr=sampling_rate)
        st.pyplot()

        # creeate a spectrogram
        X = librosa.stft(data)
        Xdb = librosa.amplitude_to_db(abs(X))
        plt.figure(figsize=(8, 3))
        plt.title('Spectrogram for audio ', size=15)
        librosa.display.specshow(Xdb, sr=sampling_rate, x_axis='time', y_axis='hz')   
        plt.colorbar()
        st.pyplot()


    toc.placeholder()
    toc.generate()

if __name__ == "__main__":
    main()