import pyttsx3
import pywhatkit
import datetime
import webbrowser
import os
import pyjokes
import wikipedia

engine = pyttsx3.init()

engine.setProperty('rate',170)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text, output_box=None):

    print("Jarvis:", text)

    if output_box:
        output_box.insert("end","Jarvis: "+text+"\n")
        output_box.see("end")

    engine.say(text)
    engine.runAndWait()


def execute_command(command, output_box=None):

    command = command.lower().strip()


    if "play" in command:

        song = command.replace("play","").strip()

        talk("Playing "+song, output_box)

        pywhatkit.playonyt(song)


    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        talk("The time is "+current_time, output_box)


    elif "date" in command or "today" in command:

        today = datetime.datetime.now().strftime("%d %B %Y")

        talk("Today is "+today, output_box)


    elif "weather" in command:

        city = command.replace("weather","").strip()

        talk("Showing weather for "+city, output_box)

        webbrowser.open("https://www.google.com/search?q=weather+"+city)


    elif "who is" in command:

        person = command.replace("who is","").strip()

        try:

            info = wikipedia.summary(person,1)

            talk(info, output_box)

        except:

            talk("I could not find information", output_box)


    elif "open youtube" in command:

        talk("Opening YouTube", output_box)

        webbrowser.open("https://youtube.com")


    elif "open google" in command:

        talk("Opening Google", output_box)

        webbrowser.open("https://google.com")


    elif "whatsapp" in command:

        talk("Opening WhatsApp", output_box)

        webbrowser.open("https://web.whatsapp.com")


    elif "joke" in command:

        joke = pyjokes.get_joke()

        talk(joke, output_box)


    elif "shutdown" in command:

        talk("Shutting down computer", output_box)

        os.system("shutdown /s /t 5")


    elif "exit" in command or "stop" in command:

        talk("Goodbye boss", output_box)

        os._exit(0)


    else:

        talk("I did not understand that command", output_box)