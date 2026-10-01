import asyncio
import os
import edge_tts
import playsound


VOICE = "en-IN-NeerjaNeural"
OUTPUT_FILE = "mia_voice.mp3"


async def generate_audio(text):
    communicate = edge_tts.Communicate(
        text,
        VOICE,
        rate="+0%",
        volume="+0%",
        pitch="+0Hz"
    )

    await communicate.save(OUTPUT_FILE)


def speak(message: str):
    try:
        # Audio generate करो
        asyncio.run(generate_audio(message))

        # Audio play करो
        playsound.playsound(OUTPUT_FILE)

        # Temporary audio file delete करो
        if os.path.exists(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)

    except Exception as e:
        print(f"TTS Error: {e}")


if __name__ == "__main__":
    speak("Hello sir, I am Mia.")