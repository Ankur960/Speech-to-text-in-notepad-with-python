import pyautogui
import speech_recognition as sr  # pip install speechRecognition


def opennotepad():
    pyautogui.press('win', interval=0.2)
    pyautogui.typewrite('notepad', interval=0.1)
    pyautogui.press('enter', interval=0.2)

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

        pyautogui.press('space',interval=0.2)
        pyautogui.typewrite(query)
        if "new line" in query:
            pyautogui.press('enter')


    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
        opennotepad()
        while True:
            # if 1:
             takeCommand()
