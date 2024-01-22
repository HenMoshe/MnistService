from MnistServer.minstServer import MnistServiceServicer

def serve(waitForTermination=True):
    mnistService = MnistServiceServicer()
    server = mnistService.startServer(waitForTermination)
    return server


if __name__ == '__main__':
    serve()