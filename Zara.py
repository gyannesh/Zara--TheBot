from tkinter import *
import cv2
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from PIL import Image
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender_mail@gmail.com', 'sender_pass')
    server.sendmail('sender_mail@gmail.com', to, content)
    server.close()

    #************************************WISH ME FUNCTION**************************************#

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        var.set('Good Morning')
        window.update()
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        var.set('Good Afternoon')
        window.update()
        speak("Good Afternoon!")   

    else:
        var.set('Good Evening')
        window.update()
        speak("Good Evening!")  

    speak("My name is Zara, how may I help you")

   #************************************TAKE COMMAND FUNCTION **************************************#
   
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set('Listening...')
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        var.set('Analysing...')
        window.update()
        print("Analysing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        var.set('Sorry sir please repeat...')
        window.update()
        print("Sorry sir please repeat...")
        Lost =("Sorry sir please repeat...")
        speak(Lost)
        return "None"
    return query
    #************************************PLAY AND EXIT COMMAND  **************************************#
def play():
    btn1['state'] = 'disabled'
    btn0.configure(bg = 'lime')
    wishme()
    while True:
        btn1.configure(bg = 'lime')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg = '#5C85FB')
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir")
            break

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
       #************************************QUERIES  **************************************#
        elif  'open youtube' in query:
            var.set('opening youtube')
            window.update()
            webbrowser.open("https://www.youtube.com/")

        elif 'hello' in query:
            var.set('Hello sir')
            window.update()
            greet = ("Hello sir, what can I do for you")
            speak(greet)

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        
        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate)

        elif "tell me the weather" in query:
            var.set('tell me the weather')
            window.update()
            webbrowser.open("https://www.google.com/search?q=eweather&oq=eweather&aqs=chrome..69i57j0i10i131i433l2j0i10l2j0i10i433j0i10j0i10i433.2756j1j7&sourceid=chrome&ie=UTF-8")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'who created you' in query:
            var.set('Virtual assistant created by Gyan')
            window.update()
            speak('Virtual assistant created by Gyan')

                   
        elif 'your name' in query:
            var.set("My name is Zaara")
            window.update()
            speak('my name is zaara')

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        
        elif 'what can you do for me' in query:
            var.set('I can do multiple tasks for you sir. tell me whatever you want to perform ')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform ')

        elif 'how are you' in query:
            var.set("I am absolutely fine and Iam always available to help you")
            window.update()
            speak("I am absolutely fine and Iam always available to help you")

            
   #************************************ QUERIES  **************************************#

        elif 'play music' in query:
            var.set('play music')
            window.update()
            query = query.replace("play music", "")
            webbrowser.open("https://wynk.in/music/detailsearch/"+query+"?q="+ query)

        elif 'in youtube' in query:
            query = query.replace("open in youtube", "")
            webbrowser.open('https://www.youtube.com//results?search_query=' + query)
            
        

        elif 'search' in query:
            speak("just a second...")
            query = query.replace("search", "")
            webbrowser.open('https://google.com/?#q=' + query)
            speak('I found this on web')


    

        elif 'what is' in query:
            query = query.replace("what is", "")
            webbrowser.open('https://google.com/?#q=' + query)

        elif 'Tell me something about' in query:
            query = query.replace("Tell me something about", "")
            webbrowser.open('https://google.com/?#q=' + query)

        elif 'open blackboard' in query:
            var.set('Opening BB...')
            window.update()
            webbrowser.open('https://cuchd.blackboard.com/ultra/course')
            speak('Opening Blackboard')

        elif 'open my time table' in query:
            var.set('Opening CUIMS')
            window.update()
            webbrowser.open('https://uims.cuchd.in/UIMS/frmMyTimeTable.aspx')
            speak('Opening your time table for online classes')

               #************************************EMAIL command **************************************#

        elif 'email to' in query:
            try:
                var.set('What should I say?')
                windows.update()
                speak("What should I say?")
                content = takeCommand()
                to = "reciever's_mail@gmail.com"    
                sendEmail(to, content)
                var.set('Email has been sent!')
                window.update()
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                var.set('Email has not been sent!')
                window.update()
                speak("Email has not been sent..") 






   #************************************GUI **************************************#

    
def update(ind):
    frame = frames
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#856ff8')
label2.config(font=("Times", 20))
var1.set('ZARA 1.0')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#856ff8')
label1.config(font=("Courier", 20))
var.set('Welcome ')
label1.pack()

frames = [PhotoImage(file='assistant.gif')]
window.title('ZARA')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'PLAY',width = 20,command = play, bg = 'cyan')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = 'yellow')
btn1.config(font=("Courier", 12))
btn1.pack()


window.mainloop()
