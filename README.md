# Text-to-Speech
A simple Python-based Text-to-Speech (TTS) application that converts user-input text into speech using the pyttsx3 library. This program runs in a loop and allows users to enter text continuously until they type "stop" to exit.

## Features
Converts text into speech.
Runs continuously until the user types stop.
Supports case-insensitive commands for stopping.
Cross-platform compatibility (works on Windows, macOS, and Linux).

## How it Works
The program initializes the TTS engine using the pyttsx3 library.
The user is prompted to enter text that the program will convert into speech.
If the user types stop, the program says a goodbye message and exits.
Otherwise, it reads the text aloud and continues until "stop" is entered.

## Installation
1. Clone this repository
2. Install Python: Ensure you have Python 3.x installed on your system.
3. Install the required library: Use pip to install the pyttsx3 library

## Code Overview
1.The project is a single Python script.
2.It uses the pyttsx3 library for text-to-speech conversion.
3.Includes an infinite loop that continuously accepts user input.
4.Exits gracefully when the user types "stop".

## Contact
For any issues or suggestions, feel free to contact me:
Email: swastik.mandal2023@iem.edu.in
