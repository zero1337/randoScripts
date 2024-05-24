import numpy as np
import soundfile as sf

def generate_sine_wave(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

def generate_oscillating_wave(freq1, freq2, duration, interval, sample_rate=44100):
    num_intervals = int(duration / interval)
    wave = np.array([])

    for i in range(num_intervals):
        if i % 2 == 0:
            wave = np.concatenate((wave, generate_sine_wave(freq1, interval, sample_rate)))
        else:
            wave = np.concatenate((wave, generate_sine_wave(freq2, interval, sample_rate)))

    remaining_duration = duration - num_intervals * interval
    if remaining_duration > 0:
        if num_intervals % 2 == 0:
            wave = np.concatenate((wave, generate_sine_wave(freq1, remaining_duration, sample_rate)))
        else:
            wave = np.concatenate((wave, generate_sine_wave(freq2, remaining_duration, sample_rate)))

    return wave

# Parameters
freq1 = 174  # First frequency in Hz
freq2 = 528  # Second frequency in Hz
duration = 30  # Total duration in seconds
interval = 0.022  # Interval between frequency changes in seconds
sample_rate = 96000  # Sample rate in Hz

# Generate the oscillating wave
oscillating_wave = generate_oscillating_wave(freq1, freq2, duration, interval, sample_rate)

# Save the oscillating wave as a .wav file
sf.write('osci_wave.wav', oscillating_wave, sample_rate)

print("Oscillating wave file generated successfully.")