import numpy as np
import soundfile as sf

def generate_sine_wave(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

# Parameters
frequency = 174  # Frequency in Hz
duration = 5  # Duration in seconds
sample_rate = 44100  # Sample rate in Hz

# Generate the sine wave
sine_wave = generate_sine_wave(frequency, duration, sample_rate)

# Save the sine wave as a .wav file
sf.write('174Hz_sine_wave.wav', sine_wave, sample_rate)

print("174 Hz sine wave file generated successfully.")