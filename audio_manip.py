import wave
import librosa
from gtts import gTTS


def get_duration_wav(wav_filename):
    f = wave.open(wav_filename, "r")
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    f.close()
    return duration


def save_wav(text, output_file):
    tts = gTTS(text=text, lang="en")
    tts.save(output_file + ".wav")
    return output_file + ".wav"


def stretch(input_file, output_file, speed):
    """Phase-vocoder time stretch demo function.
    :parameters:
      - input_file : str
          path to input audio
      - output_file : str
          path to save output (wav)
      - speed : float > 0
          speed up by this factor
    """

    # 1. Load the wav file, resample
    print("Loading ", input_file)

    y, sr = librosa.load(input_file)

    # 2. Time-stretch through effects module
    print("Playing back at {:3.0f}% speed".format(speed * 100))

    y_stretch = librosa.effects.time_stretch(y, speed)

    print("Saving stretched audio to: ", output_file)
    librosa.output.write_wav(output_file, y_stretch, sr)
