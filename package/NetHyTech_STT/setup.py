from setuptools import setup, find_packages


setup(
    name="NetHyTech-STT",
    version="0.1.1",
    author="Krishna Jadon",
    author_email="krishnajadon813@gmail.com",
    description="Speech to Text package created by Krishna Jadon",
    packages=find_packages(),
    install_requires=[
        "SpeechRecognition",
        "sounddevice",
        "numpy",
    ],
)