# Import libraries
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
import wikipedia
import pywhatkit
import pyjokes
import os
import pyautogui
import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Creating recognizer object
recognizer = sr.Recognizer()

# Initializing text-to-speech engine
engine = pyttsx3.init()

# API keys for news and weather
newsapi = "8e5b0a4cbef64ed79e88b8549b212dc0"
weatherapi = "706bd931f82fc21879d0a516a572259b"

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function that wishes according to current time 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!") 

# Function for processing the command
def processCommand(c):

    social_media_sites={
    "google": "https://google.com",
    "facebook": "https://facebook.com",
    "youtube": "https://youtube.com",
    "linkedin": "https://linkedin.com",
    "instagram": "https://instagram.com",
    "twitter": "https://twitter.com",
    "reddit": "https://reddit.com"
    }

    # Open social media sites
    for site, url in social_media_sites.items():
        if f"open {site}" in c.lower():
            speak(f"Opening {site.capitalize()}....")
            webbrowser.open(url)
            break
    
    # Tells what is the current time
    if 'the current time' in c.lower():
            current_time = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the current time is {current_time}")
    
    # Provides five news headlines of US
    elif "news" in c.lower():

        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                if not articles:
                    speak("Sorry, I couldn't find any news right now")
                else:
                    speak("Here are the top news headlines")
                    for article in articles[:5]:  # Limit to top 5 headlines
                        speak(article['title'])
            else:
                speak("Failed to fetch news. Please check your API key or internet connection")
        except Exception as e:
            print("Error; {0}".format(e))
            
    # Provides the weather of specific city
    elif "weather in" in c.lower() or "weather at" in c.lower():
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # Extract and sanitize city name
        lower_c = c.lower()
        if "weather in" in lower_c:
            city = lower_c.split("weather in")[-1].strip()
        else:
            city = lower_c.split("weather at")[-1].strip()

        # Add country code if not already specified
        if "," not in city:
            city += ",IN"
        if city:

            try:
                full_url = f"{base_url}appid={weatherapi}&q={city}&units=metric"
                response = requests.get(full_url)
                data = response.json()
                if str(data.get("cod")) == "200":
                    main_data = data["main"]
                    weather_desc = data["weather"][0]["description"]
                    temp = main_data["temp"]
                    humidity = main_data["humidity"]
                    spoken_city = city.split(",")[0].title()
                    speak(f"The current temperature in {spoken_city} is {temp}°C with {weather_desc} and Humidity is {humidity} percent")
                else:
                    spoken_city = city.split(",")[0].title()
                    speak(f"City '{spoken_city}' not found, Please try again")
            except Exception as e:
                print("Error; {0}".format(e))
        else:
            speak("Please specify the city")

    # Searches and plays a YouTube video
    elif "play on youtube" in c.lower() or "search youtube for" in c.lower():
        
        try:
            if "play on youtube" in c.lower():
                topic = c.lower().replace("play on youtube", "").strip()
            else:
                topic = c.lower().replace("search youtube for", "").strip()
            if topic:
                speak(f"Playing {topic} on YouTube")
                pywhatkit.playonyt(topic)
            else:
                speak("Please tell me what to play on YouTube.")
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, I couldn't play the video right now.")

    # Searches topics from wikipedia
    elif "wikipedia" in c.lower() or "search wikipedia for" in c.lower() or "tell me about" in c.lower():
        speak("Searching wikipedia....")

        try:
            # Clean command to extract the topic
            if "search wikipedia for" in c.lower():
                topic = c.lower().replace("search wikipedia for", "").strip()
            elif "tell me about" in c.lower():
                topic = c.lower().replace("tell me about", "").strip()
            else:
                topic = c.lower().replace("wikipedia", "").strip()

            if topic:
                summary = wikipedia.summary(topic, sentences=2)
                speak(f"According to wikipedia: {summary}")
            else:
                speak("Sorry, I didn't catch the topic to search.")
        except Exception as e:
            print("Error; {0}".format(e))

    # Tells a random joke
    elif "tell me a joke" in c.lower() or "joke" in c.lower():
        joke = pyjokes.get_joke()
        speak(joke)

    # Shut down the system
    elif "shut down" in c.lower() or "shutdown" in c.lower():
        speak("Shutting down the system in 5 seconds")
        os.system("shutdown /s /t 5")

    # Restart the system
    elif "restart" in c.lower():
        speak("Restarting the system in 5 seconds")
        os.system("shutdown /r /t 5")

    # Take a screenshot
    elif "take a screenshot" in c.lower():
        speak("Taking a screenshot")
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        speak("Screenshot saved as screenshot.png")

    # Volume control using pycaw
    elif "increase volume" in c.lower():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(min(current + 0.1, 1.0), None)
        speak("Volume increased")

    elif "decrease volume" in c.lower():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(max(current - 0.1, 0.0), None)
        speak("Volume decreased")

    # Brightness control using screen-brightness-control
    elif "increase brightness" in c.lower():
        
        try:
            current_brightness = sbc.get_brightness(display=0)[0]
            new_brightness = min(current_brightness + 10, 100)
            sbc.set_brightness(new_brightness, display=0)
            speak(f"Brightness increased to {new_brightness} percent")
        except Exception as e:
            print("Error; {0}".format(e))

    elif "decrease brightness" in c.lower():

        try:
            current_brightness = sbc.get_brightness(display=0)[0]
            new_brightness = max(current_brightness - 10, 0)
            sbc.set_brightness(new_brightness, display=0)
            speak(f"Brightness decreased to {new_brightness} percent")
        except Exception as e:
            print("Error; {0}".format(e))

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    wishMe()

    while True:
        # Obtain audio from the microphone
        # Listen for the wake word "jarvis"
        r = sr.Recognizer()
        print("Recognizing....")

        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if "exit" in word.lower() or "stop" in word.lower():
                speak("Thank you, exiting now")
                break
            if "jarvis" in word.lower():
                speak("Yes sir, how may i help you")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    if "exit" in command.lower() or "stop" in command.lower():
                        speak("Thank you, exiting now")
                        break
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))