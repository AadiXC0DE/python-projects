import speech_recognition as sr
import time

def speech_to_text():
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Speak something...")
            audio = r.listen(source)

        try:
            print("Recognizing...")
            text = r.recognize_google(audio)
            print("You said: " + text)

            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"output_{timestamp}.txt"
            
            with open(filename, "w") as file:
                file.write(text)
            print(f"Text saved to '{filename}'.")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your speech.")
        except sr.RequestError as e:
            print("Sorry, an error occurred. {0}".format(e))
        
        choice = input("Do you want to continue recording? (y/n): ")
        if choice.lower() != 'y':
            break

speech_to_text()
