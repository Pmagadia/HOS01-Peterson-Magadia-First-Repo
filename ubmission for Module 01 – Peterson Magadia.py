class HelloWorld: # A start of a simple class

    def __init__(self): # Constructor that initializes the message
        self.message = "Hello, World" # Setting the message attribute
        
    def display(self): # Method to display the message
        print(self.message) # Print the message

greeting = HelloWorld() # Creating an instance of HelloWorld
greeting.display() # To display the greeting message