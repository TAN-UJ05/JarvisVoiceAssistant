# 🤖 Jarvis - Voice Assistant

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Speech Recognition](https://img.shields.io/badge/Speech_Recognition-FF6B6B?style=for-the-badge&logo=google&logoColor=white)
![Pyttsx3](https://img.shields.io/badge/Pyttsx3-Text_to_Speech-4CAF50?style=for-the-badge)
![Requests](https://img.shields.io/badge/Requests-API-00ADD8?style=for-the-badge)

A **Python-based voice assistant** inspired by JARVIS from Iron Man, built using **speech recognition, text-to-speech, and various APIs**.  
It can perform tasks like opening websites, fetching news/weather, playing YouTube videos, searching Wikipedia, telling jokes, controlling system volume/brightness, and more—all via voice commands.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🌐 Open Websites | Opens popular social media sites (Google, Facebook, YouTube, etc.) |
| ⏰ Current Time | Tells the current time |
| 📰 News Headlines | Fetches top 5 US news headlines using NewsAPI |
| 🌤️ Weather Info | Provides weather details for a specified city using OpenWeatherMap API |
| 🎵 YouTube Playback | Searches and plays videos on YouTube |
| 📖 Wikipedia Search | Summarizes topics from Wikipedia |
| 😂 Jokes | Tells random jokes |
| 💻 System Control | Shutdown, restart, take screenshots |
| 🔊 Volume Control | Increase/decrease system volume |
| 💡 Brightness Control | Adjust screen brightness |
| 🎤 Voice Activation | Activates on "Jarvis" wake word |

---

## 🖥️ Project Structure

```
jarvis.py          -> Main Python script
requirements.txt   -> List of required Python libraries
README.md          -> This file
```

---

## 🛠️ How It Works

### Activation
- Say **"Jarvis"** to wake the assistant.
- It responds with "Yes sir, how may I help you?"
- Then, give a voice command (e.g., "Open Google", "What's the weather in New York").

### Commands Examples
- **Open sites:** "Open Facebook" → Opens Facebook in browser.
- **Time:** "What's the current time?" → Speaks the time.
- **News:** "Tell me the news" → Reads top 5 headlines.
- **Weather:** "Weather in London" → Provides temperature, description, humidity.
- **YouTube:** "Play on YouTube Avengers trailer" → Plays the video.
- **Wikipedia:** "Tell me about Python" → Summarizes from Wikipedia.
- **Joke:** "Tell me a joke" → Shares a random joke.
- **System:** "Shut down" → Shuts down the PC in 5 seconds.
- **Screenshot:** "Take a screenshot" → Saves a screenshot as PNG.
- **Volume/Brightness:** "Increase volume" or "Decrease brightness" → Adjusts accordingly.
- **Exit:** "Exit" or "Stop" → Ends the program.

---

## 🏷️ Code Overview

**Key Functions**

- `speak(text)` → Converts text to speech using pyttsx3.
- `wishMe()` → Greets based on current time (Morning/Afternoon/Evening).
- `processCommand(c)` → Processes the voice command and executes actions.

**APIs Used**
- **NewsAPI:** For fetching news headlines (requires API key).
- **OpenWeatherMap:** For weather data (requires API key).

**Libraries**
- `speech_recognition`: For voice input.
- `pyttsx3`: For text-to-speech.
- `webbrowser`: To open URLs.
- `requests`: For API calls.
- `wikipedia`: For summaries.
- `pywhatkit`: For YouTube playback.
- `pyjokes`: For jokes.
- `os`: For system commands.
- `pyautogui`: For screenshots.
- `screen_brightness_control`: For brightness.
- `pycaw`: For volume control.

---

## 📊 Sample Command Flow

```python
# User says: "Jarvis"
# Assistant: "Yes sir, how may I help you?"

# User says: "Weather in New York"
# Assistant processes: Fetches weather data and speaks: "The current temperature in New York is 22°C with clear sky and Humidity is 65 percent"
```

---

## ⚡ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourGitHubUsername/jarvis-voice-assistant.git
   cd jarvis-voice-assistant
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys:**
   - Get a NewsAPI key from [newsapi.org](https://newsapi.org) and replace `newsapi` variable.
   - Get an OpenWeatherMap key from [openweathermap.org](https://openweathermap.org) and replace `weatherapi` variable.

4. **Run the script:**
   ```bash
   python jarvis.py
   ```

> Ensure your microphone is working. The assistant listens continuously for the wake word "Jarvis".

---

## 🚀 Future Improvements

- Add **natural language processing** for more complex queries.
- Integrate **Google Calendar** or **email** reading.
- Implement **multi-language support**.
- Add **GUI interface** for visual feedback.
- Enhance **error handling** and offline capabilities.
- Support for **custom wake words** or multiple users.

---

## 📫 Contact

- **GitHub:** https://github.com/TAN-UJ05
- **Email:** tanujjoshi669@gmail.com

---

## ⚖️ License
MIT License  
Made with ❤️ using Python and various libraries.
