from curses import baudrate
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

def generate_ask_signal(bits, duration, sample_rate, frequency, amplitude_0, amplitude_1):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.zeros_like(t)

    for i, bit in enumerate(bits):
        amplitude = amplitude_1 if bit == '1' else amplitude_0
        signal[i * int(len(t) // len(bits)): (i + 1) * int(len(t) // len(bits))] = amplitude

    modulated_signal = signal * np.sin(2 * np.pi * frequency * t)
    return t, modulated_signal

def generate_uart_packet(data, bit_duration, sample_rate, frequency, amplitude_0, amplitude_1):
    stop_bit = '1'
    packet_duration = (len(data) + 2) * bit_duration  # Add start and stop bits
    t = np.linspace(0, packet_duration, int(sample_rate * packet_duration), endpoint=False)
    signal = np.zeros_like(t)

    # start bit
    signal[:int(bit_duration * sample_rate)] = amplitude_0

    # data bits
    for i, bit in enumerate(data):
        amplitude = amplitude_1 if bit == '1' else amplitude_0
        signal[int((i + 1) * bit_duration * sample_rate): int((i + 2) * bit_duration * sample_rate)] = amplitude

    # Add stop bit
    signal[int((len(data) + 1) * bit_duration * sample_rate):] = amplitude_1

    modulated_signal = signal * np.sin(2 * np.pi * frequency * t)
    return t, modulated_signal

def play_audio(signal, sample_rate):
    sd.play(signal, samplerate=sample_rate)
    sd.wait()

def plot_waveform(t, signal):
    plt.figure(figsize=(10, 4))
    plt.plot(t, signal)
    plt.title('UART-Transmitted Signal')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()  

if __name__ == "__main__":
    bits = '10101010'
    bit_duration = 0.1  # Set bit duration to 0.1 seconds
    sample_rate = 44100  # audio sample rate
    frequency = 18000  # modulation frequency of 18 kHz
    amplitude_0 = 0  # amplitude for bit '0' (Logic-Low)
    amplitude_1 = 1.2  # amplitude for bit '1' (Logic-High)

    # To generate a continuous signal with start and stop bits between each "10101010"
    continuous_signal = []

    for _ in range(5):  
        # Generate UART-modulated signal for the packet
        t, uart_signal = generate_uart_packet(bits, bit_duration, sample_rate, frequency, amplitude_0, amplitude_1)
        continuous_signal.extend(uart_signal)

        # Add logic high for 0.5 seconds after the stop bit
        gap_bits = '1' * int(0.5 / bit_duration)
        gap_t, gap_signal = generate_ask_signal(gap_bits, 0.5, sample_rate, frequency, amplitude_0, amplitude_1)
        continuous_signal.extend(gap_signal)

    # Play the combined signal
    play_audio(continuous_signal, sample_rate)

    # Plot the waveform interactively
    plot_waveform(np.linspace(0, len(continuous_signal) / sample_rate, len(continuous_signal)), continuous_signal)

