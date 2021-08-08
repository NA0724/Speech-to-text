import speech_recognition as sr

r=sr.Recognizer()

audio_file = sr.AudioFile("STT.wav")

with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

result = r.recognize_google(audio)

with open("my_speech.txt",mode='w') as file :
    file.write("Recognised Text: ")
    file.write("\n")
    file.write(result)
    print(" Speech converted to Text Successfully !!! ")
