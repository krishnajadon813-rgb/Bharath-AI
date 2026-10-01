Bharath AI

A Python-based voice assistant designed to understand spoken commands,
respond with speech, and automate common web-based tasks.

✨ Overview

Bharath AI is a modular voice-assistant project built with Python.
It combines:

🎤 Speech-to-Text (STT)

🔊 Text-to-Speech (TTS)

🌐 Voice-controlled website opening

🧠 Command and alias handling

🗂️ Organized website data

🧩 Modular project structure for future AI and automation features

The project is being developed as a learning-focused, extensible voice
assistant that can grow into a more capable personal assistant over
time.

🚀 Features

🎙️ Voice Commands

Bharath AI can listen through the microphone and convert spoken commands
into text.

🔊 Natural Voice Responses

The assistant uses Microsoft Edge TTS voices through edge-tts and can
speak responses aloud.

🌐 Website Automation

Common websites can be opened through voice commands.

Examples:

Open YouTube
Open Instagram
Open GitHub
Open WhatsApp
Open ChatGPT
Open Canva
Open Google Maps

🔎 Command Aliases

Bharath AI supports alternative names and common speech variations.

Examples:

yt       → YouTube
insta    → Instagram
ig       → Instagram
fb       → Facebook
wa       → WhatsApp
tg       → Telegram
chat gpt → ChatGPT
git hub  → GitHub

🧱 Modular Architecture

The project separates major responsibilities into different modules:

Bharath AI/
├── Automation/
│   └── web_open.py
├── DATA/
│   └── Web_Data.py
├── SpeechToText/
│   └── SpeechToText_Python.py
├── TextToSpeech/
│   ├── Fast_DF_TTS.py
│   ├── TTS_DF.PY
│   ├── TextToSpeech_B.py
│   ├── TextToSpeech_python.py
│   └── ttsB.py
├── package/
│   └── NetHyTech_STT/
├── main.py
├── mia.py
└── .gitignore

🛠️ Technology Stack

Technology          Purpose

Python              Core application
SpeechRecognition   Speech recognition
sounddevice         Microphone audio recording
NumPy               Audio data handling
edge-tts            Text-to-Speech
playsound           Audio playback
webbrowser          Opening websites
Git                 Version control
GitHub              Source-code hosting

⚙️ Requirements

Recommended environment:

Python 3.14+

Windows

Working microphone

Internet connection for online speech recognition and Edge TTS

Git

A virtual environment is recommended.

📥 Installation

1. Clone the repository

git clone https://github.com/krishnajadon813-rgb/Bharath-AI.git
cd Bharath-AI

2. Create a virtual environment

python -m venv .venv

3. Activate the virtual environment

Windows PowerShell:

.\.venv\Scripts\Activate.ps1

4. Install dependencies

If a requirements.txt file is available:

pip install -r requirements.txt

For the current development setup, the main packages include:

pip install requests edge-tts playsound==1.2.2 pyttsx3 SpeechRecognition sounddevice numpy

▶️ Running Bharath AI

Activate the virtual environment first:

.\.venv\Scripts\Activate.ps1

Then run the assistant:

python mia.py

You should see:

==================================================
        BHARATH AI - MIA
==================================================
Voice assistant started.
Say 'exit' or 'quit' to stop.
==================================================

Bharath AI will then listen for voice commands.

🎤 Example Commands

Try commands such as:

Hello Mia
Open YouTube
Open Instagram
Open GitHub
Open ChatGPT
Open WhatsApp
Open Canva
Open Google Maps

To stop the assistant:

Exit

or:

Quit

📁 Project Modules

mia.py

Main assistant logic. It connects speech recognition, command
processing, website lookup, browser automation, and voice responses.

DATA/Web_Data.py

Contains the website dictionary used to map spoken website names to
URLs.

TextToSpeech/

Contains the text-to-speech implementations and voice output utilities.

SpeechToText/

Contains speech recognition related code.

package/NetHyTech_STT/

Contains the project's reusable speech-to-text package.

Automation/

Contains browser and automation utilities.

🔐 Security

Do not commit sensitive information such as:

API keys

Passwords

Access tokens

Private certificates

.env files containing secrets

The repository's .gitignore is configured to exclude common
virtual-environment, cache, generated-audio, and secret files.

🧪 Development Status

Bharath AI is an actively developing project.

Current development focuses on:

Improving speech recognition

Improving voice responses

Expanding website and command support

Making command recognition more reliable

Building a stronger assistant architecture

Adding more automation capabilities

Features may change as development continues.

🗺️ Future Roadmap

Planned areas for future development include:

More natural conversations

Better command understanding

More desktop automation

Application launching

Improved multilingual support

Custom wake-word support

Smarter context handling

More assistant skills

Improved error handling

A polished user interface

🤝 Contributing

Contributions, suggestions, and improvements are welcome.

A simple contribution workflow:

git clone https://github.com/krishnajadon813-rgb/Bharath-AI.git
git checkout -b feature/your-feature

Make your changes, test them, then commit:

git add .
git commit -m "Add your feature"
git push origin feature/your-feature

Then open a Pull Request on GitHub.

📄 License

No license has currently been specified for this repository.

If you intend to allow others to legally reuse, modify, or distribute
the project, consider adding an appropriate open-source license.

👨‍💻 Author

Mayank Pratap Singh Jadon

GitHub: @krishnajadon813-rgb

🔗 Repository

Bharath AI:
https://github.com/krishnajadon813-rgb/Bharath-AI
