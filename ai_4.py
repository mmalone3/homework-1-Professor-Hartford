import speech_recognition as sr
import sys
import tkinter as tk
import pyttsx3
import pyjokes
import datetime
import wikipedia
import pyaudio 
import pywhatkit as pymus

# Create a recognizer object
recognizer = sr.Recognizer()



# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 for male, 1 for female

# Initialize the greetings and goodbyes
hello = "how can i help you today"
goodbye = "goodbye"
action = ''
def google_api():
    with sr.Microphone() as source:
        print("Listening... (Say 'exit' to quit)")
        audio = recognizer.listen(source)

    try:
        # Perform speech recognition
        text = recognizer.recognize_google(audio)
        text = text.lower()
        print(f"Recognized: {text}")
        return text

    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def quit_app():
    root.destroy()  # Close the window

def interactions():
    text = google_api()
    
    if text is None:  # Add check for None
        return
    
    if "date" in text:
        date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        print(date)
        engine.say(date)
        engine.runAndWait()
        
    elif "joke" in text:
        joke = pyjokes.get_joke()
        print(joke)
        engine.say(joke)
        engine.runAndWait()
    elif"who is" in text:
        person = text.replace("who is", "")
        info = wikipedia.summary(person, 2)
        print(info)
        engine.say(info)
        engine.runAndWait()
    elif "play" in text:
            song = text.replace("play", "")
            print(f"Playing {song}")
            engine.say(f"Playing {song}")
            engine.runAndWait()
            pymus.playonyt(song)
        
    elif "exit" in text:
        print("Goodbye!")
        engine.say("Goodbye!")
        engine.runAndWait()
        sys.exit()
        
    else:
        print("I'm sorry, I did not understand that.")
        engine.say("I'm sorry, I did not understand that.")
        engine.runAndWait()
    
    return text

# Initialize the Tkinter root window
root = tk.Tk()
quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack()

# Start the interactions
engine.say(hello)
engine.runAndWait()
done = interactions()
print(done)

# Start the Tkinter main loop
root.mainloop()

U R L :   h t t p s : / / g i t h u b . c o m / m m a l o n e 3 / h o m e w o r k - 1 - P r o f e s s o r - H a r t f o r d  
 