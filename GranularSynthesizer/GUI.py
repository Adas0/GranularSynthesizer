import tkinter as tk
import requests
from ttkthemes import ThemedTk
from synthesizer import synth_sine, synth_noise


# root = tk.Tk()

# root = ttk.Tk
# root = ThemedTk(theme="equilux")

# root_ = tk_.ThemedTk()
# root_.get_themes()
# root_.set_theme("plastik")


root = ThemedTk(theme="equilux")
root.title('Granular')
height = 1000
width = 500
geometry_factor = width/height
geometry = str(height) + "x" + str(width)
root.geometry(geometry)


sine_wave_label = tk.Label(root, text="sine wave")
sine_wave_label.place(relx=0.08, rely=0, relwidth=0.1, relheight=0.1)


start_button = tk.Button(root, text="start", command=synth_sine.switch_on)
start_button.place(relx=0.05, rely=0.1, relwidth=0.1*geometry_factor, relheight=0.1)
# start_button.place(height=50, width=50)
# start_button.grid(row=5, column=5)

stop_button = tk.Button(root, text="stop", command=synth_sine.switch_off)
stop_button.place(relx=0.1, rely=0.1, relwidth=0.1*geometry_factor, relheight=0.1)

draw_button = tk.Button(root, text="draw", command=synth_sine.draw)
draw_button.place(relx=0.15, rely=0.1, relwidth=0.1*geometry_factor, relheight=0.1)

grain_time_label = tk.Label(root, text="Grain time [ms]")
grain_time_label.place(relx=0, rely=0.2, relwidth=0.5*geometry_factor, relheight=0.1)
sine_grain_time_slider = tk.Scale(root, from_=2, to=100, resolution=1, orient=tk.HORIZONTAL, length=300, width=20)
sine_grain_time_slider.place(relx=0, rely=0.3, relwidth=0.5*geometry_factor, relheight=0.1)

silence_time_label = tk.Label(root, text="Break time [ms]")
silence_time_label.place(relx=0, rely=0.4, relwidth=0.5*geometry_factor, relheight=0.1)
sine_silence_time_slider = tk.Scale(root, from_=2, to=500, resolution=1, orient=tk.HORIZONTAL, length=300, width=20)
sine_silence_time_slider.place(relx=0, rely=0.5, relwidth=0.5*geometry_factor, relheight=0.1)

gaussian_sigma_label = tk.Label(root, text="Gaussian sigma")
gaussian_sigma_label.place(relx=0, rely=0.6, relwidth=0.5*geometry_factor, relheight=0.1)
sine_sigma_value_slider = tk.Scale(root, from_=1, to=500, resolution=1, orient=tk.HORIZONTAL, length=300, width=20)
sine_sigma_value_slider.place(relx=0, rely=0.7, relwidth=0.5*geometry_factor, relheight=0.1)


amplitude_slider = tk.Scale(root, from_=0, to=1, resolution=0.01, orient=tk.VERTICAL, length=200, width=20)
# amplitude_slider.pack()

frequency_label = tk.Label(root, text="Sine Frequency [Hz]")
frequency_label.place(relx=0, rely=0.8, relwidth=0.5*geometry_factor, relheight=0.1)
sine_freq_slider = tk.Scale(root, from_=50, to=5000, resolution=1, orient=tk.HORIZONTAL, length=300, width=20)
sine_freq_slider.place(relx=0, rely=0.9, relwidth=0.5*geometry_factor, relheight=0.1)

# ustawienia suwakow: 100, 28, 5 woda padajaca na piasek
# 24, 125, 33, 3910 - ptak


################# NOISE #####################

noise_label = tk.Label(root, text="noise")
noise_label.place(relx=0.08+0.3, rely=0, relwidth=0.1, relheight=0.1)

noise_start_button = tk.Button(root, text="start", command=synth_noise.switch_on)
noise_start_button.place(relx=0.05+0.3, rely=0.1, relwidth=0.1*geometry_factor, relheight=0.1)
# start_button.place(height=50, width=50)
# start_button.grid(row=5, column=5)

noise_stop_button = tk.Button(root, text="stop", command=synth_noise.switch_off)
noise_stop_button.place(relx=0.1+0.3, rely=0.1, relwidth=0.1*geometry_factor, relheight=0.1)

noise_draw_button = tk.Button(root, text="draw", command=synth_noise.draw)
noise_draw_button.place(relx=0.15+0.3, rely=0.1, relwidth=0.1*geometry_factor, relheight=0.1)

noise_grain_time_label = tk.Label(root, text="Grain time [ms]")
noise_grain_time_label.place(relx=0+0.3, rely=0.2, relwidth=0.5*geometry_factor, relheight=0.1)
noise_grain_time_slider = tk.Scale(root, from_=2, to=100, resolution=1, orient=tk.HORIZONTAL, length=300, width=20)
noise_grain_time_slider.place(relx=0+0.3, rely=0.3, relwidth=0.5*geometry_factor, relheight=0.1)

noise_silence_time_label = tk.Label(root, text="Break time [ms]")
noise_silence_time_label.place(relx=0+0.3, rely=0.4, relwidth=0.5*geometry_factor, relheight=0.1)
noise_silence_time_slider = tk.Scale(root, from_=2, to=500, resolution=1, orient=tk.HORIZONTAL, length=300, width=20)
noise_silence_time_slider.place(relx=0+0.3, rely=0.5, relwidth=0.5*geometry_factor, relheight=0.1)
#
noise_gaussian_sigma_label = tk.Label(root, text="Gaussian sigma")
noise_gaussian_sigma_label.place(relx=0+0.3, rely=0.6, relwidth=0.5*geometry_factor, relheight=0.1)
noise_sigma_value_slider = tk.Scale(root, from_=1, to=500, resolution=1, orient=tk.HORIZONTAL, length=300, width=20)
noise_sigma_value_slider.place(relx=0+0.3, rely=0.7, relwidth=0.5*geometry_factor, relheight=0.1)
#
# add_signals_button = tk.Button(root, text="+", command=synth_noise.switch_off)
# add_signals_button.place(relx=0.6, rely=0.1, relwidth=0.1*geometry_factor, relheight=0.1)


tk.mainloop()
