print("Hello")

botName = "Jarvis"
bot = botName + ": "

while True:

    why = input(bot + "Why are you building this?")

    why = why.strip().lower()

    if why == "quit":
        print(bot + "Goodbye...")
        break
    
    if why == "to learn" or why == "learn":
        print(bot + "You're on the right path.")
    elif why == "idk":
        print(bot + "Go figure it out!")
    elif why == "":
        print("say something...i'm giving up on you.\n")
    else:
        print(bot + "awkward...")
