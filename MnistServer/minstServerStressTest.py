import threading
from unittest.mock import patch

def automatedClientRequest(MnistClient, server_address, request_type='y'):
    client = MnistClient(server_address)
    if request_type == 'y':
        numOfSamples = -1
    else:
        numOfSamples = int(request_type)
    
    client.showMnistData(numOfSamples)

def minstClientStressTest(MnistClient, server_address, request_type='y', num_clients=5):
    threads = []
    for _ in range(num_clients):
        thread = threading.Thread(target=automatedClientRequest, args=(MnistClient, server_address, request_type))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
 