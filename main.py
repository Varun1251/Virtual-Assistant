from time import time
import pyttsx3                     # text to speech conversion 
import datetime                    # datetime
import speech_recognition as sr    # speech recognition
import wikipedia                   # access wikipedia
import webbrowser                  # access web browser
import pywhatkit                   # access the song on youtube 
import os                          # if the program is run it create the files
import smtplib                     # send email from gmail
import pyjokes                     # access programmin jokes

# Speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wishme Command
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternon!")

    else:
        speak("Good Evening!")
    
    speak("Hi, I am Zira. Please tell me how may I help you")

# Take Command
def takeCommand():
    # It take microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please.....")
        speak("Say that again please.....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('varunkapruwan1151@gmail.com', 'your-password')
    server.sendmail('youremial@gmail.com', to, content)
    server.close

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executed tasks based on query.
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # open youtube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        # open google 
        elif 'open google' in query:
            webbrowser.open("google.com")

        # open stackoverflow 
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")  

        # open geekforgeeks
        elif 'open geeks for geeks' in query:
            webbrowser.open("geeksforgeeks.com")

        # open salary predictor
        elif 'open salary predictor' in query:
            webbrowser.open("https://share.streamlit.io/vasugargdev/salary-predictor-ml-app/main/app.py")

        # open facebook
        elif 'facebook' in query:
            webbrowser.open("facebook.com")

        # open instagram
        elif 'instagram' in query:
            webbrowser.open("instagram.com")     

        # open Gmail
        elif 'gmail' in query:
            webbrowser.open("gmail.com")

        # play music
        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        # tell time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir ji, The time is {strTime}")

        # other Command
        elif 'date' in query:                 
            speak('sorry, I have a headache')

        # intro
        elif 'tell me something about you' in query:
            speak('yes sir, My name is zira and I am a advance AI machine and i\'m he re to help you') 

        # other Command
        elif 'are you single' in query:      
            speak('I am in a relationship with wifi')

        #other command 
        elif 'I love You' in query:
            speak("Sorry, I have a boyfriend")

        # open vs code
        elif 'open code' in query:
            codePath = "C:\\Users\\I5\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # open pycharm
        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.1\\bin\\pycharm64.exe"
            os.startfile(codePath)

        # tell joke
        elif 'joke' in query:                 
            speak(pyjokes.get_joke())

        # play on youtube
        elif 'play' in query:            
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        # access gmail 
        elif 'email to varun' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "varunkapruwan1251@gmial.com"
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Varun Bhai. I am not able to send this email.")

        

            
