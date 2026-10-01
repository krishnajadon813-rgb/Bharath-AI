import sys
import os
import webbrowser

# Bharat AI main folder ko Python path mein add karo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from DATA.Web_Data import WEBSITES


# Common short names / wrong spellings
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
    "flipkart": "flipkart",

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


def openweb(webname):
    website_names = webname.lower().split()

    urls_to_open = []

    for name in website_names:
        url = find_website(name)

        if url:
            urls_to_open.append(url)

    if urls_to_open:
        for url in urls_to_open:
            webbrowser.open(url)

        print("Opening...")
    else:
        print("Website not found.")


while True:
    web_input = input("Web name: ")

    if web_input.lower() in ["exit", "quit", "close"]:
        print("Closing...")
        break

    openweb(web_input)