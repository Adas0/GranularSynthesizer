import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import threading
import GUI
import sound_generator

switch_1 = True
switch_2 = True


class GranularSynthesizer:
    def __init__(self, gen_, sig_type):
        self.generator_ = gen_
        self.sig_type = sig_type
        # self.gen = []
        # self.signal = sig

    def add_signals(self, sig1, sig2):
        result = []
        if len(sig1) > len(sig2):
            for el in range(0, len(sig1)-len(sig2)):
                sig2.append(0)
        elif len(sig2) > len(sig1):
            for el in range(0, len(sig2)-len(sig1)):
                list(sig1).append(0)
        if len(sig1) == len(sig2):
            for el in range(0, len(sig1)):
                result.append((3*sig1[el] + sig2[el])/4)
        return result

    def get_sigma_value(self):
        if self.sig_type == "sine":
            return GUI.sine_sigma_value_slider.get()
        elif self.sig_type == "noise":
            return GUI.noise_sigma_value_slider.get()

    def get_grain_time(self):
        if self.sig_type == "sine":
            return GUI.sine_grain_time_slider.get()
        elif self.sig_type == "noise":
            return GUI.noise_grain_time_slider.get()

    def get_silence_time(self):
        if self.sig_type == "sine":
            return GUI.sine_silence_time_slider.get()
        elif self.sig_type == "noise":
            return GUI.noise_silence_time_slider.get()

    def update_gen(self):
        # self.signal = 0
        gen = sound_generator.SoundGenerator(fs=44100, grain_time=self.get_grain_time(), silence_time=self.get_silence_time())
        gen.samples_number = gen.fs * gen.grain_time
        gen.samples_number = int(gen.samples_number)
        new_sig = []
        if self.sig_type == "sine":
            new_sig = gen.generate_sine(freq=GUI.sine_freq_slider.get(), time=self.generator_.grain_time)
        elif self.sig_type == "noise":
            new_sig = gen.generate_noise(gen.samples_number)
        # new_noise = gen.adjust_amplitude(new_noise, amplitude_slider.get())   #amplitude slider
        # new_sig = self.add_signals(new_sig, new_noise)
        new_sig = gen.adjust_amplitude(new_sig, 0.5)
        new_sig = gen.add_envelope(new_sig, self.get_sigma_value())
        new_sig = gen.add_silence(new_sig, gen.silence_time)
        new_sig = gen.adjust_amplitude(new_sig, 1)
        self.generator_.signal = new_sig
        self.generator_.grain_time = gen.grain_time
        return new_sig

    def audio(self):
        def start_audio():
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

            if self.sig_type == "sine":
                while switch1:
                    self.signal = self.update_gen()
                    samples = np.float32(self.signal)
                    stream.write(samples)
                    if not switch1:
                        break
            elif self.sig_type == "noise":
                while switch2:
                    self.signal = self.update_gen()
                    samples = np.float32(self.signal)
                    stream.write(samples)
                    if not switch2:
                        break

            stream.stop_stream()
            stream.close()
            p.terminate()

        thread = threading.Thread(target=start_audio)
        thread.start()

    def switch_on(self):
        if self.sig_type == "sine":
            global switch1
            switch1 = True
        elif self.sig_type == "noise":
            global switch2
            switch2 = True

        self.audio()

    def switch_off(self):
        if self.sig_type == "sine":
            global switch1
            switch1 = False
        elif self.sig_type == "noise":
            global switch2
            switch2 = False

    def draw(self):
        plt.plot(self.generator_.signal)
        plt.axis([0, int(self.generator_.fs * self.get_grain_time()/1000 / 2), -1, 1])
        plt.show()


generator = sound_generator.SoundGenerator(fs=44100, grain_time=10, silence_time=500)

synth_sine = GranularSynthesizer(gen_=generator, sig_type="sine")
synth_noise = GranularSynthesizer(gen_=generator, sig_type="noise")


# synth_n = GranularSynthesizer(gen_=generator, sig=noise_)
