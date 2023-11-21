import librosa
import numpy as np
import matplotlib.pyplot as plt

def get_vocal_range(audio_file):
    # Load the audio file
    y, sr = librosa.load(audio_file)

    # Extract the chromagram feature
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)

    # Sum the chroma features over time to get a pitch distribution
    pitch_distribution = np.sum(chroma, axis=1)

    # Find the index of the maximum value in the pitch distribution
    max_pitch_index = np.argmax(pitch_distribution)

    # Convert the index to a MIDI note number
    max_pitch_midi = librosa.hz_to_midi(librosa.note_to_hz(max_pitch_index))

    # Print the result
    print(f"The maximum pitch (in MIDI) is: {max_pitch_midi}")

if __name__ == "__main__":
    audio_file_path = "path/to/your/audio/file.wav"
    get_vocal_range(audio_file_path)
