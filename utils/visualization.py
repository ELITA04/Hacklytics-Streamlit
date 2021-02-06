import matplotlib.pyplot as plt
import librosa
import librosa.display

def create_waveplot(data, sampling_rate):
    plt.figure(figsize=(10, 3))
    plt.title('Waveplot for audio ', size=15)
    return librosa.display.waveplot(data, sr=sampling_rate)
    
