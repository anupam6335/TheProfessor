import pyttsx3 as p
import speech_recognition as sr
engine = p.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
voiceList = engine.setProperty('voice',voices[1].id)

# print(voiceList)
def speak(text):
    engine.say(text)
    engine.runAndWait()


# create a instance of the recognizer class
r = sr.Recognizer()


speak("Hello sir, I'm your voice assistant The Professor, how are you")

#main code starts here
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Lisenting...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
    
if 'what' and 'about' and 'you' in text:
    speak('I am also having a good day sir')
speak('what can i do for you?')