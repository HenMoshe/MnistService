import unittest
import grpc
from minstServiceProto_pb2_grpc import MnistServiceStub
from minstServiceProto_pb2 import DataRequest

class TestMnistServiceIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.channel = grpc.insecure_channel('localhost:50051')
        cls.stub = MnistServiceStub(cls.channel)

    @classmethod
    def tearDownClass(cls):
        cls.channel.close()

    def testSuccessfulDataRetrieval(self):
        request = DataRequest(numOfSamples=10)
        response = self.stub.GetTrainingSamples(request)
        response_list = list(response)
        self.assertEqual(len(response_list), 10)
        # Additional assertions to check data integrity

    # Other test cases...

if __name__ == '__main__':
    unittest.main()