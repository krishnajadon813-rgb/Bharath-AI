import pyttsx3


def speak(text):
    engine = pyttsx3.init()

    voices = engine.getProperty("voices")

    print("Available voices:")

    for i, voice in enumerate(voices):
        print(i, voice.name)

    # Same voice selection as the working main.py
    if len(voices) > 2:
        engine.setProperty("voice", voices[2].id)
    elif len(voices) > 0:
        engine.setProperty("voice", voices[0].id)

    # Working slow speed
    engine.setProperty("rate", 120)

    engine.setProperty("volume", 1.0)

    print()
    print("Speaking:")
    print(text)
    print("Rate:", engine.getProperty("rate"))
    print()

    engine.say(text)
    engine.runAndWait()

    engine.stop()

    print("Speech finished.")


speak("Hello")
speak("i am mia")
speak("what are you doing")