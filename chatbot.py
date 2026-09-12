print("Hello")

# define variables
botName = "Jarvis"

# build the text that goes before the bot's messages
# \n starts a new line... then add the bot's name and ": "
botPrefix = "\n" + botName + ": "

# start the count outside the loop so it doesn't reset every time the loop repeats
answerCount = 0

# define a function that retrieves the bot's response, with a parameter called userAnswer
# a parameter receives the value passed in when the function is called
def get_bot_reply(userAnswer):
    # take the value passed into userAnswer and compare it with these possible values
    if userAnswer == "to learn" or userAnswer == "learn":
        # if it matches then end the function and send this text back
        # return doesn't print or store it... the code calling the function handles that
        return "You're on the right path."
    elif userAnswer == "idk":
        return "Go figure it out!"
    elif userAnswer == "":
        return "say something...i'm giving up on you."
    else:
        # if none of the conditions above matched... return this reply
        return "awkward..."

# create a list called userAnswerHistory
# a python list is similar to a javascript array... it can hold strings, numbers, etc.
# python's array module is different and stores specific types, mainly numeric values
# create the list outside the loop so we keep adding to the same list
userAnswerHistory = []

# while repeats code as long as its condition is true
# here we give it True directly... so the condition is always true
# something like while answerCount > 0 would check that comparison to determine if its true or false.
# this loop below keeps going until the userAnswer gets a break in the bot's response.
while True:

    # the variable userAnswer calls the input() function...it shows whatever is in the paramter and waits for a response from me...
    # in this case it shows the question and waits for me to respond
    # whatever i type becomes the value that gets returned (sent back) by the input function.
    userAnswer = input(botPrefix + "Why are you building this?\nYou: ")

    # strip() function removes spaces and other whitespace from the beginning and end
    # lower() function makes the text lowercase... then save that cleaned text back into userAnswer
    # ***IMPORTANT: the userAnswer variable did not get redefined its output was just modified...it is still waiting for my response***
    userAnswer = userAnswer.strip().lower()

    # add userAnswer to the end of userAnswerHistory... the list we made outside the loop
    # since this happens before the checks below... blank answers and quit get added too
    # ***IMPORTANT: the userAnswer variable did not get redefined its output was just added to the history list...it is still waiting for my response***
    userAnswerHistory.append(userAnswer)

    # if my answer is quit then the bot's response, goodbye, gets printed and the loop stops
    # break skips the rest of this loop... so the userAnswerHistory isn't printed here
    if userAnswer == "quit":
        print(botPrefix + "Goodbye...")
        break

    # != means "not equal to"... so only count the answer if it isn't an empty string
    if userAnswer != "":
        answerCount = answerCount + 1

    # call get_bot_reply() function and pass my userAnswer into its parameter
    # the parameter inside the function and the variable here have the same name...
    # doesnt have to be but we do it for clarity sake...
    # basically when defining the function the parameter within is just a placeholder...
    # so that we know what is supposed to go in there...
    # whatever the function returns gets stored in botReply
    # userAnswer is what i typed... botReply is the response the function returns (sends back)
    botReply = get_bot_reply(userAnswer)

    # print the bot's name + ": " followed by the text stored in botReply
    print(botPrefix + botReply)

    # print the list of my saved answers
    print(userAnswerHistory)

    # when we reach the end of the loop... go back and check the while condition again
    # the list keeps my previous inputs and gets another input added on the next repetition
    # the bot's replies aren't saved because we only append userAnswer to the list