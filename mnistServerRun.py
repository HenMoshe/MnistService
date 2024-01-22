from MnistServer.minstServer import MnistServiceServicer
from MnistServer.minstServerUnitTesting import runServerUnitTesting

def serve(waitForTermination=True):
    runServerUnitTesting()
    mnistService = MnistServiceServicer()
    server = mnistService.startServer(waitForTermination)
    return server


if __name__ == '__main__':
    serve()