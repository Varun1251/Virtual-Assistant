# libraries
import speech_recognition as sr                 # for voice recognition
import pyttsx3                                  # alexa talk to me
import pywhatkit                                # access the song on youtube
import datetime                                 # to show the time
import wikipedia                                # to access the wikipedia
import pyjokes                                  # for jokes

listener = sr.Recognizer()
# create engine to speak with you 
engine = pyttsx3.init()
# to change the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# alexa talk to you
engine.say('hi Varun')
engine.say('What can I do for you')
engine.runAndWait()


def talk(text):                         # alexa repeat your words
    engine.say(text)
    engine.runAndWait()


def take_command():                 # alexa take commands
    try:
        with sr.Microphone() as source:         # use microphone
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)          # convert voice to text
            command = command.lower()
            if 'alexa' in command:                              # detect alexa is mention or not
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():                        # access the take_command
    command = take_command()
    print(command)
    if 'play' in command:               # play song on youtube
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:              # show and tell the time
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:          # show in wikipedia
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:                 # other comments
        talk('sorry, I have a headache')
    elif 'are you single' in command:       # other comments
        talk('I am in a relationship with wifi')
    elif 'joke' in command:                 # for jokes
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again my friend.')


while True:
    run_alexa()