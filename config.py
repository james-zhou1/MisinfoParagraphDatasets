import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import json
import librosa
import sounddevice as sd
import os
import subprocess
from pathlib import Path

def play():
    audio_data, sample_rate = librosa.load('../duolingo.mp3', sr=None)
    sd.play(audio_data, sample_rate)
    sd.wait()

__all__ = ['pd', 'json', 'warnings', 'play', 'Path', 'os', 'subprocess']


