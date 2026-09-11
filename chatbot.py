print("Hello")

botName = "Jarvis: "

while True:

    why = input(botName + "Why are you building this?")

    why = why.strip().lower()

    if why == "quit":
        print(botName + "Goodbye...")
        break
    
    if why == "to learn" or why == "learn":
        print(botName + "You're on the right path.")
    elif why == "idk":
        print(botName + "Go figure it out!")
    elif why == "":
        print("say something...i'm giving up on you.\n")
    else:
        print(botName + "awkward...")
