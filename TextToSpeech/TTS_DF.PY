import asyncio
import os
import edge_tts
from playsound3 import playsound


VOICE = "en-IN-NeerjaNeural"


async def generate_speech(text, output_file):
    communicate = edge_tts.Communicate(
        text,
        VOICE
    )

    await communicate.save(output_file)


def speak(text):
    output_file = os.path.join(
        os.getcwd(),
        "speech.mp3"
    )

    try:
        print()
        print("=" * 50)
        print("EDGE TTS")
        print("=" * 50)
        print()

        print("Text:")
        print(text)
        print()

        print("Voice:")
        print(VOICE)
        print()

        print("Generating speech...")

        asyncio.run(
            generate_speech(
                text,
                output_file
            )
        )

        print("Audio generated.")
        print()

        if not os.path.exists(output_file):
            print("ERROR: Audio file was not created.")
            return

        print("Playing audio...")

        playsound(output_file)

        print("Speech finished.")

    except Exception as error:
        print()
        print("=" * 50)
        print("TTS ERROR")
        print("=" * 50)
        print(error)

    finally:
        if os.path.exists(output_file):
            try:
                os.remove(output_file)
                print("Temporary audio file removed.")
            except Exception as error:
                print("Could not remove audio file:", error)


if __name__ == "__main__":
    speak("Hello, I am Mia")
    speak("hey krishna aap kese ho")
    speak("me aapki kese madatt kar sakti hu")
    