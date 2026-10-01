import os
import sys
import webbrowser

# =========================================================
# PATH SETUP
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


# =========================================================
# IMPORTS
# =========================================================

from DATA.Web_Data import WEBSITES
from NetHyTech_STT import listen
from TextToSpeech.ttsB import speak


# =========================================================
# COMMON ALIASES
# =========================================================

ALIASES = {
    "yt": "youtube",
    "you tube": "youtube",

    "ig": "instagram",
    "insta": "instagram",

    "fb": "facebook",

    "wa": "whatsapp",
    "whats app": "whatsapp",

    "tg": "telegram",

    "dc": "discord",

    "x": "twitter",

    "flipcart": "flipkart",

    "shopsy": "shopsy",
    "shopsee": "shopsy",

    "amazone": "amazon",

    "g mail": "gmail",
    "gmail": "gmail",

    "g drive": "google drive",

    "g maps": "google maps",
    "maps": "google maps",

    "chat gpt": "chatgpt",

    "github": "github",
    "git hub": "github",

    "linkedin": "linkedin",

    "canva": "canva",

    "netflix": "netflix",

    "spotify": "spotify",

    "telegram web": "telegram web",
    "whatsapp web": "whatsapp web",
}


# =========================================================
# WEBSITE FINDER
# =========================================================

def find_website(name):
    name = name.lower().strip()

    # Direct match
    if name in WEBSITES:
        return WEBSITES[name]

    # Alias match
    if name in ALIASES:
        real_name = ALIASES[name]

        if real_name in WEBSITES:
            return WEBSITES[real_name]

    return None


# =========================================================
# OPEN WEBSITE
# =========================================================

def openweb(command):
    command = command.lower().strip()

    # Remove common voice command words
    prefixes = [
        "open ",
        "launch ",
        "go to ",
        "visit ",
        "start "
    ]

    for prefix in prefixes:
        if command.startswith(prefix):
            command = command[len(prefix):].strip()
            break

    # First try the complete command.
    # This is important for names like:
    # google maps
    # chat gpt
    # youtube studio
    # whatsapp web
    # telegram web
    url = find_website(command)

    if url:
        webbrowser.open(url)
        print("Opening:", command)
        return True

    # Try aliases after normalizing spaces
    normalized = command.replace("  ", " ").strip()

    url = find_website(normalized)

    if url:
        webbrowser.open(url)
        print("Opening:", normalized)
        return True

    # Finally try individual words
    words = normalized.split()

    for word in words:
        url = find_website(word)

        if url:
            webbrowser.open(url)
            print("Opening:", word)
            return True

    print("Website not found:", command)
    return False


# =========================================================
# MAIN VOICE ASSISTANT
# =========================================================

def main():
    print("=" * 50)
    print("        BHARAT AI - MIA")
    print("=" * 50)
    print("Voice assistant started.")
    print("Say 'exit' or 'quit' to stop.")
    print("=" * 50)

    speak("Hello sir, I am Mia. I am ready.")

    while True:

        try:
            # Listen through NetHyTech STT
            command = listen()

            if not command:
                continue

            command = command.lower().strip()

            print("Command:", command)

            # ---------------------------------------------
            # EXIT COMMANDS
            # ---------------------------------------------

            if command in [
                "exit",
                "quit",
                "close",
                "stop",
                "goodbye"
            ]:
                speak("Okay sir. Goodbye.")
                print("Bharat AI stopped.")
                break

            # ---------------------------------------------
            # GREETING
            # ---------------------------------------------

            if command in [
                "hello",
                "hi",
                "hey",
                "hello mia",
                "hi mia",
                "hey mia"
            ]:
                speak("Hello sir. How can I help you?")
                continue

            # ---------------------------------------------
            # WEBSITE COMMAND
            # ---------------------------------------------

            if (
                command.startswith("open ")
                or command.startswith("launch ")
                or command.startswith("go to ")
                or command.startswith("visit ")
                or command.startswith("start ")
            ):
                if openweb(command):
                    speak("Opening it.")
                else:
                    speak("Sorry sir, I could not find that website.")

                continue

            # ---------------------------------------------
            # DIRECT WEBSITE NAME
            # ---------------------------------------------

            if find_website(command):
                if openweb(command):
                    speak("Opening it.")

                continue

            # ---------------------------------------------
            # UNKNOWN COMMAND
            # ---------------------------------------------

            speak(
                "Sorry sir, I am still learning this command."
            )

        except KeyboardInterrupt:
            print("\nBharat AI stopped.")
            break

        except Exception as error:
            print("Bharat AI Error:", error)
            speak("Sorry sir, something went wrong.")


# =========================================================
# START
# =========================================================

if __name__ == "__main__":
    main()