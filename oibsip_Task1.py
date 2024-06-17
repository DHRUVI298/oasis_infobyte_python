        # DABHI DHRUVI R
        #  VOICE 
        # task 1
            
            
            
            
            
            
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# import email  # Uncomment if needed for the email functionality
recognizer = sr.Recognizer()
# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Using the second voice available

# Function to speak the provided audio
def speack(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet based on the current time
def date():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speack('Good Morning')
    elif hour >= 12 and hour < 18:
        speack('Good Afternoon')
    else:
        speack('Good Evening')
    
    speack('I am your virtual assistant. Please tell me how may I help you')

# Function to take voice command from the user
def command():
    
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    
    try:
        print('Recognizing...')
        text = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {text}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError:
        print("Could not request results from Google Web Speech API.")
        return "None"
    
    return text


if __name__ == "__main__":
    date()
    while True:
        text = command().lower()
        if 'stop' in text or 'exit' in text:
            speack("Goodbye! Have a nice day.")
            exit()
            
        elif 'wikipedia' in text:
            speack('Searching Wikipedia...')
            text = text.replace("wikipedia", "")
            result = wikipedia.summary(text, sentences=2)
            speack("According to Wikipedia")
            print(result)
            speack(result)
            
        elif 'open youtube' in text:
            webbrowser.open("youtube.com")
            
        elif 'open google' in text:
            webbrowser.open("google.com")
            
        elif 'time right now' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speack(f"The time is {strTime}")
            print(f"The time is {strTime}")
        elif 'weather' in text:
            webbrowser.open('https://www.accuweather.com/en/in/india-weather')
        elif 'what is your name' in text:
            name = "Your virtual assistant "
            speack(f'{name}')
            speack
            

        elif text:
            command(text)
            