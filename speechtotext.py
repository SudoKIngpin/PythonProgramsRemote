import speech_recognition as sr
r=sr.Recognizer()
source=sr.Microphone()

audio=r.listen(source)
r.pause_threshold=1
r.adjust_for_ambient_noise(source)

query=r.recognize_google(audio,language='en')
print(f"User said : {query}")
