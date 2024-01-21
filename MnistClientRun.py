from minstClient import MnistClient;

def getUserInput():
    print("press y for downloading the full dataset, or enter the number of required samples from 1 - 70000, or press q to quit.")
    return input().strip()

def processUserInput(client, userInput):
    if userInput.lower() == 'q':
        return 'quit'
    elif userInput.isdigit():
        numOfSamples = int(userInput)
        if 1 <= numOfSamples <= 70000:
            client.showMnistData(numOfSamples)
        else:
            print("Please enter a number between 1 and 70000.")
    elif userInput.lower() == 'y':
        client.showMnistData(-1)
    else:
        print("Invalid input. Please enter a number from 1-70000, 'y' for all data, or 'q' to quit.")

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
