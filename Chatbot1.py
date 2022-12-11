import random

# Define a list of greetings that the AI can use
greetings = ["Hello!", "Hi there!", "Greetings!", "Howdy!", "Hola!"]

# Define a list of responses to common questions
responses = ["I'm doing well, thank you.", "I'm just a program, so I don't have feelings.", "I'm a machine learning model, not a human."]

# Define a list of responses to statements
statements = ["That's interesting.", "I see.", "I'm not sure I understand what you mean.", "Could you explain that in more detail?"]

# Define a function that generates a random response to a given input
def generate_response(input_text):
    # If the input is a greeting, choose a random greeting to respond with
    if input_text.lower() in ["hello", "hi", "greetings", "howdy", "hola"]:
        return random.choice(greetings)
    
    # If the input is a question, choose a random response from the list of responses
    elif input_text[-1] == "?":
        return random.choice(responses)
    
    # Otherwise, assume the input is a statement and choose a random response from the list of statements
    else:
        return random.choice(statements)

# Define a main function that runs the conversational AI
def main():
    # Print a greeting to start the conversation
    print(random.choice(greetings))

    # Set a variable to indicate whether the conversation is over
    conversation_over = False

    # Keep looping until the conversation is over
    while not conversation_over:
        # Ask the user for input
        user_input = input("What would you like to say? ")

        # Generate a response
        response = generate_response(user_input)

        # Print the response
        print(response)

        # If the user's input is "goodbye", set the conversation_over variable to True to end the conversation
        if user_input.lower() == "goodbye":
            conversation_over = True

# Call the main function to start the conversation
main()
