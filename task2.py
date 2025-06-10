def chatbot():  
    print('Chatbot: Hello! Type "bye" to exit.')  # Greet the user  
    while True:  
        user_input = input('You: ').lower().strip()  # Get user input  
        if user_input == 'hello':  
            print('Chatbot: Hi!')  
        elif user_input == 'how are you':  
            print('Chatbot: I\'m fine, thanks!')  
        elif user_input == 'bye':  
            print('Chatbot: Goodbye!')  
            break  # Exit the loop and end the chat  
        else:  
            print('Chatbot: Sorry, I don\'t understand.')  
  
# Start the chatbot  
chatbot()  