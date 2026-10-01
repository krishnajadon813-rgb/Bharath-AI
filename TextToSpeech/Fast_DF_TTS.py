import asyncio
import os
import tempfile
import threading

import edge_tts
from playsound3 import playsound


VOICE = "en-IN-NeerjaNeural"


async def generate_speech(text, output_file):
    communicate = edge_tts.Communicate(
        text,
        VOICE
    )

    await communicate.save(output_file)


def play_audio(output_file):
    try:
        playsound(output_file)
    except Exception as error:
        print("PLAYBACK ERROR:")
        print(error)
    finally:
        try:
            if os.path.exists(output_file):
                os.remove(output_file)
        except Exception:
            pass


def speak(text: str) -> None:
    try:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        ) as tmpfile:
            output_file = tmpfile.name

        print("Generating speech...")

        asyncio.run(
            generate_speech(
                text,
                output_file
            )
        )

        print("Playing...")

        threading.Thread(
            target=play_audio,
            args=(output_file,),
            daemon=True
        ).start()

    except Exception as error:
        print("TTS ERROR:")
        print(error)


while True:
    text = input("You: ")

    if not text.strip():
        continue

    speak(text)