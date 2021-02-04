import os
from pygame import *
import speech_recognition as sr
import datetime
import webbrowser as web
import wikipedia
import wolframalpha
import smtplib
import random

def wish():
    time=datetime.datetime.now().time()
    hour=time.hour

    if hour>=12 and hour<18:
        print("good afternoon sir")
        os.system('espeak "{}"'.format("good afternoon sir"))
    elif hour>=6 and hour<12:
        print("good morning sir")
        os.system('espeak "{}"'.format("good morning sir"))
    else:
        print("good night sir")
        os.system('espeak "{}"'.format("good night sir"))


def special_command():
    global reply
    recog=sr.Recognizer()
    mic1=sr.Microphone()

    with mic1 as source:
        print("listning....")
        recog.adjust_for_ambient_noise(source,duration=1)
        audio=recog.listen(source)

    try:
        os.system('espeak "{}"'.format("recognizing"))
        print("recognizing...")
        REPLY=recog.recognize_google(audio,language="en-IN")
        reply=REPLY.lower()
        print("you said:",reply)

    except Exception as e:
        return()

def command():
    global text
    rec=sr.Recognizer()
    mic=sr.Microphone()
    
    with mic as source:
        print("listening...")
        rec.adjust_for_ambient_noise(source,duration=1)
        audio=rec.listen(source)

    try:
        print("recognizing....")
        os.system('espeak "{}"'.format("recognizing"))
        TEXT=rec.recognize_google(audio,language="en-IN")
        text=TEXT.lower()
        print("you said:",text)
        

    except Exception as e:
        print("sir please say that again.")
        os.system('espeak "{}"'.format("sir please say that again"))
        return()
        

wish()
os.system('espeak "{}"'.format("i am your jarvis sir,how can i help you"))
while True:
    command()

    if "open youtube" in text:
        text=""
        web.open("https://www.youtube.com")
        os.system('espeak "{}"'.format("opening youtube,sir"))
        os.system('espeak "{}"'.format("next command,sir"))


    elif "search" in text:
        text=""
        call(["espeak","-s140 -ven+18 -z","what i have to search sir"])
        special_command()
        site="https://www.google.com/search?source=hp&ei=0bAJXaG9O4W8rQG1mZxA&q="+reply
        web.open(site)
        reply=""
        os.system('espeak "{}"'.format("here is it,sir"))
        os.system('espeak "{}"'.format("now what my next task,sir"))


    elif "open facebook" in text:
        text=""
        web.open("https://www.facebook.com")
        os.system('espeak "{}"'.format("opening facebook,sir"))
        os.system('espeak "{}"'.format("next command,sir"))


    elif "open whatsapp" in text:
        text=""
        web.open("https://web.whatsapp.com")
        os.system('espeak "{}"'.format("opening whatsapp,sir"))
        os.system('espeak "{}"'.format("next command,sir"))


    elif "wikipedia" in text:
        text=""
        os.system('espeak "{}"'.format("sir please say,what i have to search"))
        special_command()
        os.system('espeak "{}"'.format("searching"))
        wiki=wikipedia.summary(reply,sentences=2)
        print("According to Wikipedia:",wiki)
        os.system('espeak "{}"'.format("ir,wikipedia says that,"))
        os.system('espeak "{}"'.format(wiki))
        reply=""
        os.system('espeak "{}"'.format("next command,sir"))


    elif "tell me" in text:
        os.system('espeak "{}"'.format("yes sir,what i have to search"))
        command()
        client=wolframalpha.Client("JXW3A3-EK792GWGXL")
        res=client.query(text)
        output=next(res.results).text
        print(output)
        os.system('espeak "{}"'.format(output))
        text=""
        os.system('espeak "{}"'.format("next command,sir"))


    elif "email" in text:
        text=""
        while True:
            os.system('espeak "{}"'.format("whom you want to send the mail?sir"))
            special_command()
            if "boss"==reply:
                reply=""
                os.system('espeak "{}"'.format("what should i say"))
                special_command()
                content=reply
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.ehlo()
                server.starttls()
                server.login("kanharajput91@gmail.com","9926495946")
                server.sendmail("kanharajput91@gmail.com","kanharajput91@gmail.com",content)
                server.close()
                reply=""
                os.system('espeak "{}"'.format("mubarak! email sent successfull"))
                os.system('espeak "{}"'.format("next command,sir"))


            elif "no one"==reply:
                os.system('espeak "{}"'.format("what can i do for you sir other then sending a mail"))
                reply=""
                break


            else:
                reply=""
                os.system('espeak "{}"'.format("please type the email adress ,sir"))
                email=str(input("email:")) 

                if email=="exit":
                    os.system('espeak "{}"'.format("what can i do for you sir other then sending a mail"))
                    break

                else:
                    os.system('espeak "{}"'.format("what should i say?sir"))
                    special_command()
                    content=reply
                    server=smtplib.SMTP("smtp.gmail.com",587)
                    server.ehlo()
                    server.starttls()
                    server.login("kanharajput91@gmail.com","9926495946")
                    server.sendmail("kanharajp[ut91@gmail.com",email,content)
                    server.close()
                    os.system('espeak "{}"'.format("mubarak,email sent successfully!"))
                    reply=""



    elif "open gmail" in text:
        text=""
        os.system('espeak "{}"'.format("opening gmail,sir"))
        web.open("https://www.gmail.com")
        os.system('espeak "{}"'.format("next command,sir"))



    elif "play song" in text:
        text=""
        songs=["kanha.wav","pehli.wav","jogi.wav"]
        file=(random.choice(songs))
        mixer.init()
        mixer.music.load(file)
        os.system('espeak "{}"'.format("okay sir,here is your music,enjoy!"))
        mixer.music.play()
        while mixer.music.get_busy:
            time.Clock().tick(10)


    elif  "stop" in text:
        os.system('espeak "{}"'.format("okay sir, as you wish,bye-bye"))
        break


    elif "flow" in text: #to open stackoverflow site
        text=""
        os.system('espeak "{}"'.format("opening the stackoverflow site,sir"))
        web.open("https://stackoverflow.com")
        os.system('espeak "{}"'.format("next command,sir"))





        









         
