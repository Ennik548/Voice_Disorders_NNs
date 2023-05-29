import os

import numpy as np
import librosa
import tensorflow as tf
from tensorflow import keras

from django.conf import settings
n_mfcc = 17 # Количество коэффициентов MFCC (от 13 до 40, для исследуемого
            # сигнала рекомендуется 13<=n_mfcc<=17)

def network_inference(path_to_file) -> bool:
    signal, sr = librosa.load(path_to_file)
    harmonic_signal, _ = librosa.effects.hpss(signal)
    mfcc = librosa.feature.mfcc(y=harmonic_signal, sr = sr, n_mfcc=n_mfcc)
    mfcc = np.array(mfcc.T.tolist())

    config_path = os.path.join(settings.BASE_DIR, 'VoiceDisorders_App', 'NeuralNetwork', 'network_config.h5')
    model = keras.models.load_model(config_path)
    prediction = model.predict(mfcc)
    l = [(bool(np.argmax(i))) for i in prediction]

    return(l.count(True) / len(l) < 0.5)