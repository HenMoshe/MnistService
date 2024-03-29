import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
import grpc
import time
from minstServiceProto_pb2 import DataRequest, Sample
from minstServiceProto_pb2_grpc import MnistServiceStub, add_MnistServiceServicer_to_server, MnistServiceServicer
from concurrent import futures
import tensorflow


class MnistServiceServicer(MnistServiceServicer):
    def __init__(self):
        logging.info("Initializing MNIST Service Servicer")
        (self.train_images, self.train_labels) = self.loadMnistData()

    def startServer(self, waitForTermination=True):
        try:
            server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
            add_MnistServiceServicer_to_server(self, server)
            server.add_insecure_port('[::]:50051')
            server.start()
            if waitForTermination:
                server.wait_for_termination()
            logging.info("MNIST Server started on port 50051")
            return server
        except Exception as e:
            logging.error("there is a problem with server startup", e)    

    def loadMnistData(self):
        try:
            dataProvider = tensorflow.keras.datasets.mnist
            (train_images, train_labels), _ = dataProvider.load_data()
            return train_images, train_labels
        except Exception as e:
            logging.error("there is a problem in loading the dataset", e)

    def GetTrainingSamples(self, request, context):
        dataRequestStartTime = time.time()
        logging.info("Received request for %s samples", request.numOfSamples)
        try:
            numOfSamples = request.numOfSamples if request.numOfSamples and request.numOfSamples > 0 else len(self.train_images)
            for image, label in zip(self.train_images[:numOfSamples], self.train_labels[:numOfSamples]):
                image_bytes = image.tobytes() 
                yield Sample(image=image_bytes, label=label)
                # should we add compression?
                #print(f'sent sample with label: {label}')
        except Exception as e:
            logging.error("Error in GetTrainingSamples: %s", e)
            context.abort(grpc.StatusCode.INTERNAL, 'Internal error occurred')
        finally:
            dataRequestEndTime = time.time()
            logging.info("Request handled in %s seconds", dataRequestEndTime - dataRequestStartTime)            
