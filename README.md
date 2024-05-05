# High-Frequency-Audio-Communication

This project explores High-Frequency Audio Communication through Amplitude Shift Keying (ASK) modulation and the implementation of a UART protocol. The system facilitates continuous one-byte data transmission in UART format with a configurable baud rate.

## Features

- Data transmission modulated using ASK at 10 kHz, 15 kHz, and 18 kHz carrier frequencies for signal representation flexibility.
- UART protocol implementation with a configurable baud rate for reliable serial data transmission.
- Receiver module for recording and displaying raw microphone data and extracting transmitted data.
- Visual representation of received ASK waveforms and demodulated binary data.

## System Architecture

The system consists of a transmitter laptop with a speaker and a receiver laptop with a microphone. The transmitter converts the data into the UART protocol, modulates it using ASK, and transmits the modulated signal through the speaker. The receiver captures the transmitted audio, processes the signal, and demodulates the data to extract the original information.

For detailed information on the system architecture, modulation techniques, and implementation details, please refer to the project report included in this repository.

## Installation and Usage

1. Clone the repository:
