from MnistClient.minstClient import MnistClient;
from MnistClient.mnistClientUnitTesting import runClientUnitTesting;
from MnistClient.InputFunctions import getUserInput, processUserInput
from MnistClient.mnistClientInputTests import runClientInputTests

def main():
    runClientUnitTesting()
    runClientInputTests()
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
