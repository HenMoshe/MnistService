import unittest
import minstClient
import minstServiceProto_pb2
import grpc
import io
from unittest.mock import patch
from MnistClientRun import main

class MnistClientTest(unittest.TestCase):
    def setUp(self):
        self.client = minstClient.MnistClient('host.docker.internal:50051')

    def testConnectionToServer(self):
        try:
            client = self.client
            self.assertIsNotNone(client.channel, "Client should have a gRPC channel.")
        except Exception as e:
            print("Client should have a gRPC channel.", e)
            self.fail("Client should have a gRPC channel.")
            
    def testRequestMnistData(self):
        try:
            serverResponse = self.client.getMnistData()
            self.assertIsNotNone(serverResponse, "Response should not be None.")
        except Exception as e:
            self.fail(f"Requesting MNIST data failed: {e}")

    def testSuccessfulAmountDataRetrieval(self):
        try:
            serverResponse = self.client.getMnistData(numOfSamples=10)
            serverResponseListed = list(serverResponse)
            self.assertEqual(len(serverResponseListed), 10)
        except Exception as e:
            self.fail(f"requested 10 samples and received a deffrent number.{e}")    

    def testReceiveDataFormat(self):
        try:
            responses = list(self.client.getMnistData(1))
            for response in responses:
                self.assertIsInstance(response, minstServiceProto_pb2.Sample, "Response should be of type Sample.")
                # Further checks can be added based on the expected data structure
        except Exception as e:
            self.fail(f"Receiving data failed: {e}")

    def testErrorHandling(self):
        client = minstClient.MnistClient('invalid_address')
        try:
            incorrectClientInitResults = list(client.getMnistData())
            self.fail("Error handling test should not succeed with an invalid address.")
        except grpc.RpcError:
            pass 
        except Exception as e:
            self.fail(f"Unexpected exception type: {e}")


if __name__ == '__main__':
    unittest.main(verbosity=2)