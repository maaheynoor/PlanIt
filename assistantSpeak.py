import pyttsx3


def assistant_speaks(output):
    engine = pyttsx3.init()
    engine.say(output)
    engine.runAndWait()
