import pyttsx3 as p

engine = p.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
voiceList = engine.setProperty('voice',voices[1].id)

print(voiceList)

engine.say("Hello there i am your voice assistant")
engine.runAndWait()