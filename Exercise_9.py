# SPEAKER


def speak(string):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(string)


if __name__ == "__main__":
    speak("Neha you should study for your interview and SSC examination")
