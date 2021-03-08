print ("Python Assistant Loading ...")
print('-----------------------------------------------------------------------')
import os
clear = lambda: os.system("cls")
clear
from pygame import mixer
clear()
print ("[#......................................]")
import time
clear()
print ("[##.....................................]")
from tkinter import *
clear()
print ("[###....................................]")
import tkinter.messagebox
clear()
print ("[####...................................]")
from subprocess import *
clear()
print ("[#####..................................]")
import webbrowser
clear()
print ("[######.................................]")
import pyttsx3
clear()
print ("[#######................................]")
import webbrowser
clear()
print ("[########...............................]")
import smtplib
clear()
print ("[#########..............................]")
import random
clear()
print ("[##########.............................]")
import speech_recognition as sr
clear()
print ("[###########............................]")
import wikipedia
clear()
print ("[############...........................]")
import datetime
clear()
print ("[#############..........................]")
import wolframalpha
clear()
print ("[##############.........................]")
import os
clear()
print ("[###############........................]")
import sys
clear()
print ("[################.......................]")
import time
clear()
print ("[#################......................]")
import win10toast
clear()
print ("[##################.....................]")
from subprocess import *
clear()
print ("[###################....................]")
import sounddevice
clear()
print ("[####################...................]")
from scipy.io.wavfile import write
clear()
print ("[#####################..................]")
from PyQt5 import QtWidgets
clear()
print ("[######################.................]")
from PyQt5.QtWidgets import QApplication, QMainWindow
clear()
print ("[#######################................]")
import sys
clear()
print ("[########################...............]")
from playsound import playsound
clear()
print ("[#########################..............]")
import datetime as dt
clear()
print ("[##########################.............]")
from gpiozero import Robot
clear()
print ("[###########################............]")
from time import sleep
clear()
print ("[############################...........]")
import win10toast
clear()
print ("[#############################..........]")
import time
clear()
print ("[##############################.........]")
import pywhatkit as kit
clear()
print ("[###############################........]")
from subprocess import *
clear()
print ("[################################.......]")
import datetime
clear()
print ("[#################################......]")
import time
clear()
print ("[##################################.....]")
import sys
clear()
print ("[###################################....]")
from math import floor
clear()
print ("[####################################...]")
import webbrowser
clear()
print ("[#####################################..]")
from playsound import playsound
clear()
print ("[######################################.]")
import time
clear()
print ("[#######################################]")
clear = lambda: os.system("cls")

clear()

print("""
----------------------------------------------------------------------
                       Python Assistant For Windows
----------------------------------------------------------------------

Conversation =>
""")

print("Hello from {PythonTech} AI community. " + "https://python-tech-boy.github.io/pythontech/")
#######################################################################################################
# HEY THERE YOU CAN SPECIFY THE ASSISTANT , YOUR NAME IN THE FOLLOWING SECTION!
#######################################################################################################
# You can enter your name here -->

User = ('User')

# You can enter the name of the AI here -->

a_name = ("Assistant")
########################################################################################################
root=Tk()
root.geometry('500x700')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title(a_name)
frame.config(background='white')
label = Label(frame, text=(a_name),bg='white',font=('Times 25'))
label.pack(side=TOP)
filename = PhotoImage(file="Logo.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)

def hel():
    webbrowser.open("https://join.skype.com/XObO15QhLbpx")
    print("Ask on Skype.")

def Contri():
    tkinter.messagebox.showinfo("Contributors","The Assistant was made by Prasoon rai.")

def playlist():
    tkinter.messagebox.showinfo("Assistant playlist","You can find the music on youtube and you can even download it.")
    webbrowser.open("https://music.youtube.com/playlist?list=PL8qJFT6AWCtLHzAbUax9HLxrhkWXpQGOa")
    sleep(5)

def anotherWin():
   tkinter.messagebox.showinfo("About",'Assistant\n Made Using\n-Python\n')

def more_info():
    webbrowser.open('https://arduinobo123.github.io/help/')

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Manager",menu=subm1)
subm1.add_command(label="Help",command=hel)
subm1.add_command(label="Music playlist",command=playlist)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Contributors",command=Contri)
subm2.add_command(label="Info",command=more_info)

def Open():
    clear = lambda: os.system("cls")
    clear
    toaster = win10toast.ToastNotifier()

    engine = pyttsx3.init('sapi5')

    client = wolframalpha.Client('V7EAL6-JGR56ELT3H')

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[len(voices)-2].id)

    def speak(audio):
        print('Assistant ' + (a_name) + ':' + audio)
        engine.say(audio)
        engine.runAndWait()

    def greetMe():
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            speak('Good Morning!')

        if currentH >= 12 and currentH < 18:
            speak('Good Afternoon!')

        if currentH >= 18 and currentH !=21:
            speak('Good Evening!')

        if currentH >= 21 and currentH !=0:
            speak("Good night!")

    playsound('ui-wakesound.mp3')

    def myCommand():
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold =  1
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print((User) + ':' + query + '\n')
        
        except sr.UnknownValueError:
            playsound('ui-endpointing-touch.mp3')
            speak('Sorry sir!  I didn\'t catch that! Can you please repeat that?')
            playsound('ui-wakesound.mp3')
            query = myCommand()

        return query

    if __name__ == '__main__':
        n = 0

        if n <= 1:
            query = myCommand();
            query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif "hello" in query or "hi" in query or "hello arduino" in query or "hi arduino" in query:
            greet = "Hello there. 😁😎😍"
            speak(greet)

        elif 'your help' in query or "help" in query:
            speak(" help section -")
            speak("Help is loading...")
            tip = ['I was designed by prasoon rai' , 'I am getting smarter everyday!' , 'I can play music' , 'What\'s up buddy!']
            time.sleep(1)
            print("#------- " + "12.5%")
            time.sleep(2)
            print("##------ " + "25%")
            time.sleep(2)
            print("###----- " + "37.5%")
            time.sleep(2)
            print("####---- " + "50%")
            time.sleep(2)
            print("#####--- " + "62.5%                                                        " + 'Do you know?: ' + (random.choice(tip)))                                               
            time.sleep(2)
            print("######-- " +"75%")
            time.sleep(2)
            print("#######- " + "87.5%")
            time.sleep(2)
            print("######## " + "100%")
            speak("Done!")
            playsound('system-alerts-melodic-01-short.mp3')
            print('''
            <------------------------------------------------------------------------------------------>
             help...
            Help -
            Assistant was designed by a solo developer, Prasoon rai.
            For more information just say 'more information arduino' or 'information arduino'.

            What's upcoming? --->

            The new version is out!!!

            What's new -->

            1. You can play game's with! like - Hangman, snake game, golf game, drawing pragram!
            Well, soon I am going to bring new updates to the Assistant like a online chess game!

            2. It can even recognize your face!
            Don\'t worry because your data is safe and will not be leaked.

            3. It can send e-mail, set alarms, play music, call anybody, perform many more amazing things.
            Just ask 'what can you do?' 

            4. I can tell you some of my most amazing features here -
              (a) Can tell you the weather of anyplace.
              (b) Tell you a story.
              (c) Tell you joke.
              (d) Perform mathematical operations.
              (e) Can do things related to science.
              (f) I can be your best friend!

             A common Tip by Assistant:

             Ok, please don't ask me such kind of questions, like 'can you walk?, can you dance and can you drive a car 
             etc...
             So, my answer to all such questions is |No|, but if you want me to do such things, make any kind
             of robotic body you like (using a raspberry PI) and just tell your Ideas to my developer
             at his G-mail ID  (arduinoboy.vbps@gmail.com) and you will get a responce from him under 5 days with basic codes...
             Well how to run the codes and other important information will be give with a handy guide added with the E-mail
             
             Well, you can Improve me because I am open source!

             Thanks!
            <------------------------------------------------------------------------------------------->
            All the information given in guide.
            In order to open the guide just say 'open help guide' or 'Help guide'.
            ''')

        elif "help guide" in query or "open help guide" in query:
            webbrowser.open("https://python-tech-boy.github.io/pythontech/")
                
        elif "what are your secrets" in query or "what is your secret" in query or "tell me your secrets" in query:
            speak("If, I will tell you my secrets. It will not be a secret")

        elif "set a alarm" in query or "set a timer" in query:
            inputbyuser = input("At What Time Do You Want The Alarm? [Format -> Hour : Minutes]: ")
            amPm = input("AM or PM?: ")

            if ":" in inputbyuser:
                listt = inputbyuser.split(":")
            else:
                print("Wrong Format")

            target_hrs = int(listt[0])
            target_mins = int(listt[1])

            if target_hrs == 12:
                if amPm.lower() == "am":
                    target_hrs = 0

            if amPm.lower() == "pm":
                if target_hrs == 12:
                    target_hrs = target_hrs
                else:
                    target_hrs = int(target_hrs) + 12

            elif amPm.lower() == "am":
                target_hrs = target_hrs

            current_time_min_value = int(datetime.datetime.now().hour) * 3600 + int(datetime.datetime.now().minute) * 60
            target_time_min_value = int(target_hrs) * 3600 + int(target_mins) * 60

            alarm_in = int(target_time_min_value) - int(current_time_min_value)

            h = int(alarm_in) / 3600
            h = floor(h)
            m = (int(alarm_in)/60) - h*60
            m = floor(m) - 1
            s = 60 - int(datetime.datetime.now().second)

            if alarm_in < 0:
                print("...Wrong Time for Alarm...")
            else:
                while alarm_in > 0:
                    sys.stdout.write("\x1b[1A\x1b[2k")
                    print(h, 'Hours', m, 'Minutes', s, "Seconds")
                    time.sleep(1)
                    s-=1
                if s == -1:
                    m -= 1
                    s = 59
                elif m == -1:
                    h -= 1
                    m = 59
                    s = 0
                    s = 59
                elif s == 0 and m == 0 and h == 0:
                    print(".......ALARM SIRENS.......\n...Timer Complete...")
                    playsound('system-alerts-melodic-01-short.mp3')


        elif "open binge" in query or "open bige" in query:
            webbrowser.open('https://www.bing.com/') 

        elif "play snake game" in query or "start snake game" in query or "snake game" in query:
            speak("Starting snake game...")
            Popen('snake.py')

        elif "open microsoft" in query or "open mycrosoft account" in query or "open my microsoft account" in query:
            webbrowser.open_new_tab('https://account.microsoft.com/')
            speak("Happy journey! " + ":-)")

        elif "start face recognition" in query or "detect face" in query or "recognize face" in query:
            
            import cv2

            # Load the cascade
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            # To capture video from webcam. 
            cap = cv2.VideoCapture(0)
            # To use a video file as input 
            # cap = cv2.VideoCapture('Your_File.mp4')

            while True:
                # Read the frame
                _, img = cap.read()

                # Convert to grayscale
                gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

                # Detect the faces
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                # Draw the rectangle around each face
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

                # Display
                cv2.imshow('img', img)

                # Stop if escape key is pressed
                k = cv2.waitKey(30) & 0xff
                if k==27:
                    break
        
                # Release the VideoCapture object
                cap.release()

        elif "clear" in query or "clear chat" in query:
            speak("Clearing...")
            speak("This may take some time...")
        
            print('Loading')
            time.sleep(2)
        
            print('Loading.')
            time.sleep(2)
        
            print('Loading..')
            time.sleep(2)
        
            print('Loading...')
            time.sleep(2)
        
            print('Loading')
            time.sleep(2)
        
        

            speak("Chat history is deleted...")
         
            speak("Loading codes...")
            time.sleep(2)
            print("--------------------------------------------------------------------------------")
            speak("Basic cascade loaded")
            time.sleep(1)
            speak("done")

# For making a robot move (IN BETA RIGHT NOW !)
            """

        elif "move forward" in query or "move forveward" in query:
            robot.forward()
            sleep(5)
            robot.stop()                   
                                                        #To make the robo move forward...

        elif "move backward" in query or "move bakward" in query:
            robot.backward()
            sleep(5)
            robot.stop()
                                                        #To make the robot move backward...

        elif "turn left" in query or "move left" in query:
            robot.left()
            sleep(5)
            robot.stop()
                                                        #To make the robot move left...

        elif "move right" in query or "turn right" in query:
            robot.right()
            sleep(5)
            robot.stop()
                                                        #To make the robot move right...

           """
                                                        
        elif "open python drawing program" in query or "python drawing" in query or "open python drawing" in query:
            Popen('python main.py')

        elif "record my voice" in query or "make a announcement" in query:
            speak("Ok, starting to record your voice!")

            fs=44100
            second=10
            print("recording -")
            record_voice=sounddevice.rec(int(second * fs),sample=fs,channels=2)
            sounddevice.wait()
            write("output.wav",fs,record_voice)

        elif "open hangman game" in query or "start hangman" in query or "open python hangman game" in query or "open python hangman" in query:
            Popen('python hangman.py')

        elif "play" in query:
            speak("Ok.")
            kit.playonyt(query)

        elif "remember that" in query or "remember" in query:
            speak("Ok, I will remember that you told me,")
            speak("To," + (query))

        elif "where do i kept" in query or "where is my" in query or "tell me where i kept" in query or "where i kept my" in query:
            speak("You told me to remember that -")
            speak(query)

        elif "show my history" in query or "show my browsing history" in query:
            speak("Heres your browsing history!")
            time.sleep(15)

        elif "send a notification" in query or "send me a notification" in query:
            speak("What should I send as a notification?")
            notification_con = myCommand()
            toaster = win10toast.ToastNotifier()
            toaster.show_toast((notification_con) , duration=7)


        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "open my os" in query or "open rc os" in query or "open plane os" in query or "plane os" in query or "open cms" in query:
            Popen('OS.bat')

        elif "would you marry me" in query or "will you marry me" in query or "marry me" in query:
            speak("Well before answering this question")
            speak("You have to answer some questions!")
            speak("Are you ready?")
            speak("Let's begin!")
            speak("1. When is my birthday?")

            A_A = myCommand()

            if "8 january" in A_A or "eight january" in A_A or "Eight January" in A_A:
                speak('Wow! great')
                speak("Let's move towards next question!")

            else:
                ("Wrong answer!")
                while(1):
                    break

            speak("1. What is my favourite colour?")

            B_B = myCommand()

            if "red" in B_B or "Red" in B_B:
                speak("Correct answer!")
                speak("Let's move toward\'s next question")
                speak("This one is going to be a bit harder!")

            else:
                speak("Wrong")
                while(1):
                    break

            speak("3. Who made me?")

            C_C = myCommand()

            if "Prasoon rai" in C_C or "prasoon rai" in C_C:
                speak("Great! but")
                speak("Right, now I am wrapping my head around the concept of love")
                speak("So, for now I would like to answer by this song!")
                webbrowser.open('https://www.youtube.com/watch?v=lNmAkWvnWEg')

            else:
                speak('Nah...')
                speak("I, think we need more time to get to know each other!")

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif "make my notes" in query or "make my school notes" in query:
            speak("Let's start making your notes...")
            speak("Enter your notes here -")
            speak("To exit notes just say, exit notes")
            note_content = myCommand()

            if "exit notes" in note_content or "exit note" in note_content:
                while(1):
                    quit
            
        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient or 'MI' in recipient or "mi" in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Mail", 'Passward')
                    server.sendmail('Your_Mail', "Your_Mail", content)
                    speak('Email sent!')
                    server.close()

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif "stop" in query:
            sys.exit

        elif "information Assistant" in query or "more information Assistant" in query:
            speak("Ok")

        elif "Who made you" in query or "who is your master" in query or "who made you" in query:
            ans_m = ("Prasoon rai made me... Thanks to him!")
            speak(ans_m)

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak("Here's what I found on the web.")
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak(results)
        
            except:
                webbrowser.open('https://www.bing.com/')
                speak("Sorry, I am unable to help with that!" + " 🤐")





print('-----------------------------------------------------------------------------------------------------------')

a = PhotoImage(file="mike.png")
btn = Button(
    root,
    image=a,
    command=Open,
    border=0,
)
btn.pack(pady=50)
btn.place(x=225,y=590)
"""
but5=Button(frame,padx=1,pady=5,width=3,bg='white',fg='black',relief=GROOVE,text=a,command=Open,font=('helvetica 15 bold'))
but5.place(x=360,y=590)
"""
root.mainloop()

print('Thanks! for choosing me ' + (User))