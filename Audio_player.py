import time
import pyaudio
import wave

# Ask the user for the input audio file
input_file = input("Input Terentij.wav")

# Set the chunk size of the audio data
chunk_size = 1024

# Open the input audio file
with wave.open(input_file, 'rb') as audio_file:
    # Create an instance of PyAudio
    audio = pyaudio.PyAudio()

    # Open a stream to play the audio data
    stream = audio.open(format=audio.get_format_from_width(audio_file.getsampwidth()),
                        channels=audio_file.getnchannels(),
                        rate=audio_file.getframerate(),
                        output=True)

    # Read the audio data in chunks and play it through the stream
    data = audio_file.readframes(chunk_size)
    while data:
        stream.write(data)
        data = audio_file.readframes(chunk_size)

    # Close the stream and PyAudio instance
    stream.stop_stream()
    stream.close()
    audio.terminate()

time.sleep(2)
input("Нажмите Enter для выхода")