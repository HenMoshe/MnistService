import unittest
from unittest.mock import patch
from MnistServer import minstServer
import grpc_testing 
from minstServiceProto_pb2 import Sample, DataRequest

class MnistServiceServicerTest(unittest.TestCase):

    def setUp(self):
        self.service = minstServer.MnistServiceServicer()
        self.responses = list(self.service.GetTrainingSamples(DataRequest(), None))
        
    def testServerLoadingMnistDataAfterStartup(self):
        try:
            (train_images, train_labels) = self.service.loadMnistData()
            self.assertTrue(list(train_images), "Expected non-empty response list from initial data lading.")
        except Exception as e:
            self.fail(f"testServer Didnt load the initial data. {e}")

    def testGetTrainingSamplesResponse(self):
        try:
            responses = self.responses
            self.assertTrue(responses, "The service should return a non-empty response.")
        except Exception as e:
            self.fail(f"GetTrainingSamples_BasicResponse raised an exception: {e}")

    @patch('MnistServer.minstServer.tensorflow')
    def testGetTrainingSamplesFormat(self, mock_tf):
        try: 
            responses = self.responses
            self.assertTrue(responses, "The service should return a non-empty response.")
            for response in responses:
                self.assertIsInstance(
                    response, Sample, 
                    f"Expected response type to be mnistServiceProto_pb2.Sample, got {type(response)} instead."
                    )
        except Exception as e:
            print(f"GetTrainingSamples_CorrectFormat test raised an exception: {e}.")
            self.fail(f"GetTrainingSamples_CorrectFormat test raised an exception: {e}.")         

    def testClientRequests(self):
        try:
            responses = list(self.service.GetTrainingSamples(DataRequest(), None))
            self.assertTrue(responses, "Expected non-empty response list.")
        except Exception as e:
            self.fail(f"testClientRequests raised an exception: {e}")               


    def testTrainingSamplesWithSpecificNumber(self):
        try:
            request = DataRequest(numOfSamples=10)
            responses = list(self.service.GetTrainingSamples(request, None))
            self.assertEqual(len(responses), 10, "Should return exactly 10 samples.")
        except Exception as e:
            self.fail(f"testTrainingSamplesWithSpecificNumber raised an exception: {e}") 

    def testTrainingSamplesWithAllData(self):
        try:
            responses = self.responses #assuming no numofsamples param to return full list
            self.assertEqual(len(responses), len(self.service.train_images), "Should return all samples.")
        except Exception as e:
            self.fail(f"testTrainingSamplesWithAllData raised an exception: {e}")  



if __name__ == '__main__':
    unittest.main(verbosity=2)


    
