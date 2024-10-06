import speech_recognition as sr 
import webbrowser
import pyttsx3
import pocketsphinx
import subprocess
import musicl
import requests
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
# webbrowser.open

op = webbrowser.get('brave').open
recognizer = sr.Recognizer()

engine=pyttsx3.init()

newsapi="46f7b732c60c4d06921c086da23e8d50"
# 46f7b732c60c4d06921c086da23e8d50 api news
# GET https://newsapi.org/v2/top-headlines?country=us&apiKey=46f7b732c60c4d06921c086da23e8d50

def speak(text):
    
    engine.say(text)
    engine.runAndWait()   
    
def processcommand(c):
    c=c.lower()
    if "open google" in c:
        op("https://google.com")
        
    elif "open spotify" in c:
        subprocess.Popen(["start", "Spotify"], shell=True)
    elif "open whatsapp" in c:
        subprocess.Popen([r"C:\Users\amitg\Desktop\WhatsApp - Shortcut.lnk"], shell=True)  # Replace with the actual path


        
    elif "open youtube" in c:
        op("https://youtube.com")
    elif c.startswith("play"):
        song=c.split(" ")[1]
        link = musicl.music[song]
        op(link)
    # elif "news" in c:
    #     r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
    #     if r.status_code == 200:
    #         data = r.json()
    #         headlines = [article['title'] for article in data['articles']]
    #     for i, headline in enumerate(headlines, 1):
    #         speak(f"{i}. {headline}")
    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")  # Ensure the country code is correct
            if r.status_code == 200:
                data = r.json()
                headlines = [article['title'] for article in data['articles']]
            if headlines:  # Check if there are any headlines
                for i, headline in enumerate(headlines, 1):
                    speak(f"Headline {i}: {headline}")
                else:
                    speak("I found no news headlines.")
            else:
                speak("I couldn't retrieve the news. Please try again later.")
        except Exception as e:
            speak("An error occurred while fetching the news.")
            print(f"Error: {e}")


        
        
if __name__=="__main__":
    
    speak("initializing jarvis.....")
    
    while True:
        
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("listening.....")
         
            try:
                
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                
            except Exception as e:
        # recognize speech using google cloud
                print("recognising")
        
        try:
            
           word= r.recognize_google(audio)
           
           if ((word.lower())=="jarvis"):
               
               speak("what's up")
               print("jarvis active")
               with sr.Microphone() as source:
                    audio = r.listen(source)
                    command= r.recognize_google(audio)
                    
                    processcommand(command)
                   
                
            
                
        except Exception as e:
            
            print(" error; {0}".format(e))