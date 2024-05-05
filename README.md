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

### Transmitter

In the transmitter stage, a single byte of data undergoes conversion to the UART protocol, introducing a distinctive communication structure. The UART protocol involves framing the data within a start bit (logic 0) and a stop bit (logic 1), encased by an idle state of 1. Ten iterations of this packet formation are sequentially transmitted, ensuring a robust and repeatable data transmission process.

Following the UART protocol, the data undergoes modulation into Amplitude Shift Keying (ASK) by multiplication with a high-frequency carrier wave. The modulation process is explored at different carrier wave frequencies: 10 kHz, 15 kHz, and 18 kHz. In this context, a logic high is represented by 1.2 volts, while logic 0 is denoted by 0 volts.

The modulated signals are then efficiently transmitted via a speaker, marking a comprehensive evaluation of the transmission process at distinct audio frequencies.

### Receiver

On the receiver side, the system is designed to capture the transmitted audio signals. The captured audio is then subjected to signal processing, and the raw data is plotted to visualize the Amplitude Shift Keying (ASK) modulation patterns.

The receiver incorporates demodulation techniques to extract the binary data embedded in the received waveform. This demodulation process is crucial in deciphering the original information encoded during transmission.

The project report includes visual representations of the received ASK waveforms and demodulated binary data for each carrier frequency, providing insights into the successful decoding and extraction of information from the transmitted audio signals.

## Installation and Usage

1. Clone the repository:
