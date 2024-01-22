from MnistClient.minstClient import MnistClient;
from MnistClient.mnistClientUnitTesting import runClientUnitTesting;
from MnistClient.InputFunctions import getUserInput, processUserInput
from MnistClient.mnistClientInputTests import runClientInputTests
from MnistServer.minstServerStressTest import minstClientStressTest

def main():
    runClientUnitTesting()
    runClientInputTests()
    minstClientStressTest(MnistClient, 'localhost:50051', 'y', 5)   
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
