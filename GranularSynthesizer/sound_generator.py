import math
import numpy as np

class SoundGenerator:
    signal = []

    def __init__(self, fs, grain_time, silence_time):
        self.fs = fs
        self.grain_time = grain_time
        self.grain_time /= 1000
        self.silence_time = silence_time

    def generate_sine(self, freq, time):
        return np.array(np.sin(2 * np.pi * freq * np.arange(0, time, 1 / self.fs)), dtype=np.float32)

    def generate_noise(self, samples_number_):
        noise = np.random.randint(-100, 100, samples_number_)
        noise = [x / 100 for x in noise]
        return noise

    def adjust_amplitude(self, sig, factor):
        sig = [el * factor for el in sig]
        return sig

    def add_silence(self, sine_, silence_time_ms):
        sine_silence = []
        for el in range(0, len(sine_)):
            sine_silence.append(sine_[el])

        for el in range(0, int((silence_time_ms/1000)*self.fs)):
            sine_silence.append(0)

        return sine_silence

    def calculate_gaussian(self, signal, sigma):
        gauss = []
        sig_len = int(len(signal) / 2)
        for el in range(0, int(len(signal) / 2)):
            gauss.append(math.exp(-1 / 2 * ((el - (sig_len - 1) / 2) / sigma / 2) ** 2))
        for el in range(int(len(signal) / 2) + 1, len(signal) + 1):
            gauss.append(0)
        # self.draw(gauss, 0, 1)
        return gauss

    def add_envelope(self, signal, sigma):
        sine_silence_gaussed = []
        gauss_envelope = self.calculate_gaussian(signal, sigma)
        for el in range(0, int(len(gauss_envelope))):
            sine_silence_gaussed.append(signal[el] * gauss_envelope[el])
        return sine_silence_gaussed
