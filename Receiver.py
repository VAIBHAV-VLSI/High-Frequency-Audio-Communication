import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def record_audio(duration, fs):
    print("Recording...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    print("Recording complete.")
    return audio_data[:, 0]

# Sampling frequency
fs = 44100  # You can adjust this according to your needs
# Duration of recording in seconds
duration = 18  # Change this to the desired duration

# Record audio
audio_data = record_audio(duration, fs)

# Convert audio data to mono if it's stereo
if audio_data.ndim > 1:
    audio_data = np.mean(audio_data, axis=1)

# Normalize the audio data to be between -1 and 1
normalized_audio_data = audio_data / np.max(np.abs(audio_data))

# Create a time axis for raw ASK waveform
time_axis_raw = np.arange(len(normalized_audio_data)) / fs

# Plot the raw ASK waveform
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time_axis_raw, normalized_audio_data)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Raw ASK Waveform vs Time')
plt.grid(True)
plt.ylim(-1.2, 1.2)

# Plot the binary array with respect to time
average_amplitude = 0.3
binary_array = np.where(np.abs(normalized_audio_data) >= average_amplitude, 1, 0)
idle_state = np.ones(int(fs * 0.1))
binary_array = np.concatenate((idle_state, binary_array))
time_axis_binary = np.arange(len(binary_array)) / fs

plt.subplot(2, 1, 2)
plt.plot(time_axis_binary, binary_array)
plt.xlabel('Time (s)')
plt.ylabel('Binary Array (1 for above or equal to average, 0 for below average)')
plt.title('Binary Array vs Time')
plt.grid(True)

plt.tight_layout()
plt.show()
