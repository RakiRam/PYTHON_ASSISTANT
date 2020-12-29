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
        #print('Current time is ' + time)

        exit(0)
    elif "who" in command:
        search = command.replace('who the heck is', '')
        info = wikipedia.summary(search, 1)
        #print(info)
        talk(info)
        exit(0)
    elif "send" in command:
        talk("Enter phone number with country code: ")
        p=input()
        talk("Enter your message:")
        m=input()
        talk("Enter time in hours:")
        h=int(input())
        talk("Enter time in minutes: ")
        min=int(input())
        pywhatkit.sendwhatmsg(p,m,h,min)
        exit(0)
    elif "mail":
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('ramakrishnamlrit2019@gmail.com', 'Ram@2002')
        reciever="Enter the recievers email id : "
        talk(reciever)
        #print(reciever)
        a=input()
        b="what is the message"
        talk(b)
        with sr.Microphone() as source:
            print("speak....")
            voice = listener.listen(source)
            n = listener.recognize_google(voice)
            c = listener.recognize_google(voice)
            print(c)
        server.sendmail('ramakrishnamlrit2019@gmail.com',a,c)
        talk("Mail sent")
        exit(0)
    elif "goodbye":
        talk("Bye")
        #print("Bye")
        exit(0)
    else:
        talk("I am sorry.I cant hear you")
while True:
    running()
