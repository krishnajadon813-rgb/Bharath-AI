import speech_recognition as sr
import sounddevice as sd
import numpy as np
import os
import io
import wave
from mtranslate import translate
from colorama import Fore, init

init(autoreset=True)


# Microphone settings
SAMPLE_RATE = 44100
CHANNELS = 1
MICROPHONE_DEVICE = 1
RECORD_SECONDS = 5


def print_loop():
    while True:
        print(Fore.GREEN + "Listening...", end="", flush=True)


def translate_hindi_to_english(text):
    try:
        english_text = translate(text, "en")
        return english_text
    except Exception as error:
        print(
            Fore.RED +
            f"\nTranslation error: {error}"
        )
        return text


def record_audio():
    print(
        Fore.GREEN +
        "\nListening... Speak now!"
    )

    try:
        audio = sd.rec(
            int(RECORD_SECONDS * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="int16",
            device=MICROPHONE_DEVICE
        )

        sd.wait()

        print(
            Fore.LIGHTBLACK_EX +
            "Recording finished. Recognizing..."
        )

        audio_bytes = audio.tobytes()

        wav_buffer = io.BytesIO()

        with wave.open(wav_buffer, "wb") as wav_file:
            wav_file.setnchannels(CHANNELS)
            wav_file.setsampwidth(2)
            wav_file.setframerate(SAMPLE_RATE)
            wav_file.writeframes(audio_bytes)

        wav_buffer.seek(0)

        return wav_buffer.read()

    except Exception as error:
        print(
            Fore.RED +
            f"\nMicrophone error: {error}"
        )
        return None


def speech_to_text_python():
    recognizer = sr.Recognizer()

    while True:

        audio_data = record_audio()

        if audio_data is None:
            print(
                Fore.RED +
                "Could not record from microphone."
            )
            return ""

        try:
            audio_file = sr.AudioFile(io.BytesIO(audio_data))

            with audio_file as source:
                audio = recognizer.record(source)

            recognized_text = recognizer.recognize_google(audio)

            recognized_text = recognized_text.lower().strip()

            if recognized_text:

                print(
                    Fore.CYAN +
                    "You: " +
                    recognized_text
                )

                english_text = translate_hindi_to_english(
                    recognized_text
                )

                print(
                    Fore.BLUE +
                    "Bharat AI: " +
                    english_text
                )

                return english_text

            else:
                print(
                    Fore.YELLOW +
                    "No speech detected."
                )
                return ""

        except sr.UnknownValueError:

            print(
                Fore.RED +
                "Could not understand audio."
            )
            return ""

        except sr.RequestError as error:

            print(
                Fore.RED +
                f"Speech recognition service error: {error}"
            )
            return ""

        except Exception as error:

            print(
                Fore.RED +
                f"Unexpected error: {error}"
            )
            return ""


def main():

    print(
        Fore.CYAN +
        "===================================="
    )

    print(
        Fore.CYAN +
        "        BHARAT AI"
    )

    print(
        Fore.CYAN +
        "===================================="
    )

    print(
        Fore.GREEN +
        "Microphone: Realtek HD Audio"
    )

    print(
        Fore.GREEN +
        "Ready!"
    )

    speech_to_text_python()


if __name__ == "__main__":
    main()
