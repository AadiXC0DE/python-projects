import speech_recognition as sr
#pip install SpeechRecognition


def speech_to_text():
    
    r = sr.Recognizer()

    
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)

    try:
        
        text = r.recognize_google(audio)
        print("You said: " + text)

        # Write the recognized text to a file
        with open("output.txt", "w") as file:
            file.write(text)
        print("Text saved to 'output.txt'.")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
    except sr.RequestError as e:
        print("Sorry, an error occurred. {0}".format(e))

speech_to_text()
