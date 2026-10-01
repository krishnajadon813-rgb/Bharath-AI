import io
import wave

import sounddevice as sd
import speech_recognition as sr


SAMPLE_RATE = 44100
CHANNELS = 1
MICROPHONE_DEVICE = 1
RECORD_SECONDS = 5


def listen():
    print("\nListening... Speak now!")

    try:
        audio = sd.rec(
            int(RECORD_SECONDS * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="int16",
            device=MICROPHONE_DEVICE
        )

        sd.wait()

        audio_bytes = audio.tobytes()

        wav_buffer = io.BytesIO()

        with wave.open(wav_buffer, "wb") as wav_file:
            wav_file.setnchannels(CHANNELS)
            wav_file.setsampwidth(2)
            wav_file.setframerate(SAMPLE_RATE)
            wav_file.writeframes(audio_bytes)

        wav_buffer.seek(0)

        recognizer = sr.Recognizer()

        with sr.AudioFile(wav_buffer) as source:
            recorded_audio = recognizer.record(source)

        text = recognizer.recognize_google(
            recorded_audio,
            language="en-IN"
        )

        print("You:", text)

        return text

    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""

    except sr.RequestError as error:
        print("Speech recognition service error:", error)
        return ""

    except Exception as error:
        print("Microphone error:", error)
        return ""