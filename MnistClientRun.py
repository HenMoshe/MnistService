from MnistClient.minstClient import MnistClient;
from MnistClient.InputFunctions import getUserInput, processUserInput

def main():    
    client = MnistClient('host.docker.internal:50051')
    print("Hello! Welcome to the MNIST Data Client.")
    while True:
        userInput = getUserInput()
        action = processUserInput(client, userInput)
        if action == 'quit':
            print("Exiting MNIST Data Client.")
            break

if __name__ == '__main__':
    main()
