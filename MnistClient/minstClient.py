import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
from minstServiceProto_pb2_grpc import MnistServiceStub
from minstServiceProto_pb2 import DataRequest
import grpc
import time

class MnistClient:
    def __init__(self, serverAddress):
        self.channel = grpc.insecure_channel(serverAddress)
        self.stub = MnistServiceStub(self.channel)
        
    def getMnistData(self, numOfSamples = 0):
        try:
            dataRequest = DataRequest(numOfSamples=numOfSamples)
            return self.stub.GetTrainingSamples(dataRequest)
        except Exception as e:
            logging.error("Error in getting data from server: %s", e)

    def getMnistDataWithRetry(self, numOfSamples=0, max_retries=3, backoff_factor=2):
        retries = 0
        while retries < max_retries:
            try:
                return self.getMnistData(numOfSamples)
            except grpc.RpcError as e:
                if retries == max_retries - 1:
                    raise e
                time.sleep(backoff_factor ** retries)
                retries += 1

    def showMnistData(self, numOfSamples = 0):
        try:
            mnistData = self.getMnistDataWithRetry(numOfSamples)
            for sample in mnistData:
                print("Received sample with label:", sample.label)
        except Exception as e:
            logging.error("Failed in showing data: %s", e)
