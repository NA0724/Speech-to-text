import speech_recognition as sr

r=sr.Recognizer()


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Please say something...")

    audio = r.listen(source)
    

    print("Recognizing...")

result = r.recognize_google(audio)
try:
    print("You said: "+result)
    print("Speech to text converted successfully!!")
except Exception as e:
    print("Error "+str(e))
