#backend
import speech_recognition as sr
#initalises the recognizer
r1 = sr.Recognizer()
#uses microphone to take the input
def record():

 with sr.Microphone() as source:
    print('Listening..')
    #listens to the user
    audio = r1.listen(source)
    #recognises the audio and converts it to text
    audio = r1.recognize_google(audio, language = 'en-IN', show_all = True )
    print(audio)


record()
