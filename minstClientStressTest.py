from MnistClientRun import main
import threading

def minstClientStressTest():
    main()

testingClientsNumber = 5
threads = [threading.Thread(target = minstClientStressTest) for _ in range(testingClientsNumber)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()