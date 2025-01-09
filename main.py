import pyttsx3

if __name__ == '__main__':
    print("Welcome to 'Text To Speech Conversion' (type 'stop' to exit the program)")
    os = pyttsx3.init()
    while True:
        x = input("Enter what you want me to say: ")
        if x.lower() == "stop":
            os.say("Goodbye! talk to you later")
            os.runAndWait()
            break

        os.say(x)
        os.runAndWait()
