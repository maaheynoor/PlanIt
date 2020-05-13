import speech_recognition as sr

# import from our module
from assistantSpeak import assistant_speaks


def get_audio():
    r = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")

        # recording the audio using speech recognition
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=3)
        # audio = r.listen(source)
    print("Stop.")  # limit 5 secs

    try:
        text = ""
        text = r.recognize_google(audio)
        print("You : ", text)
        return text

    except:

        assistant_speaks("Could not understand your audio, PLease try again !")
