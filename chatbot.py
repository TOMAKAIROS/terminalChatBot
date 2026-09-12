print("Hello")

botName = "Jarvis"
bot = "\n" + botName + ": "
answerCount = 0

def get_response(answer):
    if answer == "to learn" or answer == "learn":
        return "You're on the right path."
    elif answer == "idk":
        return "Go figure it out!"
    elif answer == "":
        return "say something...i'm giving up on you." 
    else:
        return "awkward..."

#  return stops the function and optionally sends a value back, without printing it.

history = []

while True:

    why = input(bot + "Why are you building this?\nYou: ")

    why = why.strip().lower()
    history.append(why)

    if why == "quit":
        print(bot + "Goodbye...")
        break
    
    if why != "":
        answerCount = answerCount + 1

    response = get_response(why)

    print("\n" + str(answerCount))
    print(bot + response)
    print(history)