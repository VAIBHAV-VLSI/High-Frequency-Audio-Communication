# High Frequency Audio Communication

## Introduction

This project explores High-Frequency Audio Communication through Amplitude Shift Keying (ASK) modulation and the implementation of a Universal Asynchronous Receiver-Transmitter (UART) protocol. The system facilitates continuous one-byte data transmission in UART format with a configurable baud rate.

The ability to transmit data seamlessly in the audio frequency range opens avenues for wireless communication, remote sensing, and numerous Internet of Things (IoT) applications. The application of modulation techniques like ASK offers adaptability to diverse signal representations, making them invaluable in high-frequency scenarios.

In this project, we design and implement a UART-based communication system, allowing continuous, serial transmission of one byte of data. The baud rate is set to 1/(0.1) seconds, aligning with the transmission requirements and ensuring synchronized and reliable communication.

## Features

- Data transmission modulated using ASK at 10 kHz, 15 kHz, and 18 kHz carrier frequencies for signal representation flexibility.
- UART protocol implementation with a configurable baud rate of 1/(0.1) seconds for reliable serial data transmission.
- Continuous, serial transmission of one byte of data.
- Receiver module for recording and displaying raw microphone data and extracting transmitted data.
- Visual representation of received ASK waveforms and demodulated binary data.

## System Architecture

The system consists of a transmitter laptop with a speaker and a receiver laptop with a microphone, as shown in the following block diagram:

![System Model](system_model.png)

### Transmitter Side

In the transmitter stage, a single byte of data undergoes conversion to the UART protocol, introducing a distinctive communication structure. The UART protocol involves framing the data within a start bit (logic 0) and a stop bit (logic 1), encased by an idle state of 1. Ten iterations of this packet formation are sequentially transmitted, ensuring a robust and repeatable data transmission process.

Following the UART protocol, the data undergoes modulation into Amplitude Shift Keying (ASK) by multiplication with a high-frequency carrier wave. The modulation process is explored at different carrier wave frequencies: 10 kHz, 15 kHz, and 18 kHz. In this context, a logic high is represented by 1.2 volts, while logic 0 is denoted by 0 volts.

The modulated signals are then efficiently transmitted via a speaker, marking a comprehensive evaluation of the transmission process at distinct audio frequencies.

```python
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
    frequency = 18000  # Change modulation frequency to 10 kHz
    amplitude_0 = 0  # amplitude for bit '0' (Logic-Low)
    amplitude_1 = 1.2  # amplitude for bit '1' (Logic-High)

    # To generate a continuous signal with start and stop bits between each "10101010"
    continuous_signal = []

    for _ in range(5):  # Repeat the pattern 10 times
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
```
### Receiver

On the receiver side, the system is designed to capture the transmitted audio signals. The captured audio is then subjected to signal processing, and the raw data is plotted to visualize the Amplitude Shift Keying (ASK) modulation patterns.

The receiver incorporates demodulation techniques to extract the binary data embedded in the received waveform. This demodulation process is crucial in deciphering the original information encoded during transmission.

The project report includes visual representations of the received ASK waveforms and demodulated binary data for each carrier frequency, providing insights into the successful decoding and extraction of information from the transmitted audio signals.

## Installation and Usage

1. Clone the repository:
