import streamlit as st
from pydub import AudioSegment
from utils.toc import Toc
import plotly.graph_objects as go
import pandas as pd
import io
import soundfile as sf

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

    toc.title('Title here 😄😐😟')
    # uploading the file and getting the results
    toc.header("📁 Choose a file")
    uploaded_file = st.file_uploader("Select file from your directory")
    if uploaded_file is not None:
        audio_bytes = uploaded_file.read()
        st.audio(audio_bytes, format='audio/mp3')

        file_var = AudioSegment.from_file(io.BytesIO(audio_bytes), format = 'mp3')
        file_var.export(uploaded_file.name[:-4] + '.wav', format='wav')   
        # wav_file =  uploaded_file.name[:-4]+'.wav'
        # y, sr = librosa.load(wav_file)



    toc.placeholder()
    toc.generate()

if __name__ == "__main__":
    main()