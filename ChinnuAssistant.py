import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyaudio
listener = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            str="Heyy i am chinnu what can i do for you"
            talk(str)
            print("speak....")
            voice=listener.listen(source)
            name=listener.recognize_google(voice)
            command = listener.recognize_google(voice)
            print(command)
            #talk(command)
    except:
        pass
    return command
def running():
    command=take_command()
    if "play" in command:
        cur=command.replace("play","")
        talk("playing"+cur)
        pywhatkit.playonyt(cur)
        exit(0)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print('Current time is ' + time)

        exit(0)
    elif "what" or "who" or "where" in command:
        search = command.replace('who the heck is', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
        exit(0)
    elif "exit":
        talk("Bye")
        print("Bye")
        exit(0)
    else:
        talk("I am sorry.I cant hear you")
while True:
    running()