import unittest
from unittest.mock import patch
import minstServer 
import grpc_testing
import minstServiceProto_pb2, minstServiceProto_pb2_grpc
from mnistServerRun import serve

class MnistServiceServicerTest(unittest.TestCase):

    def setUp(self):
        self.service = minstServer.MnistServiceServicer()
        self.responses = list(self.service.GetTrainingSamples(minstServiceProto_pb2.DataRequest(), None))
        self.server = grpc_testing.server_from_dictionary(
            {
                minstServiceProto_pb2.DESCRIPTOR.services_by_name['MnistService'] : minstServer.MnistServiceServicer()
            }, 
            grpc_testing.strict_real_time()
        )
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

    @patch('minstServer.tensorflow')
    def testGetTrainingSamplesFormat(self, mock_tf):
        try: 
            responses = self.responses
            self.assertTrue(responses, "The service should return a non-empty response.")
            for response in responses:
                self.assertIsInstance(
                    response, minstServiceProto_pb2.Sample, 
                    f"Expected response type to be mnistServiceProto_pb2.Sample, got {type(response)} instead."
                    )
        except Exception as e:
            print(f"GetTrainingSamples_CorrectFormat test raised an exception: {e}.")
            self.fail(f"GetTrainingSamples_CorrectFormat test raised an exception: {e}.")         

    def testClientRequests(self):
        try:
            # Create a mock request
            mockRequest = minstServiceProto_pb2.DataRequest()

            # Directly call the GetTrainingSamples method of the service
            responses = self.service.GetTrainingSamples(mockRequest, None)

            # Validate the responses
            self.assertTrue(list(responses), "Expected non-empty response list.")
        except Exception as e:
            self.fail(f"testClientRequests raised an exception: {e}")               


    def testTrainingSamplesWithSpecificNumber(self):
        try:
            request = minstServiceProto_pb2.DataRequest(numOfSamples=10)
            responses = list(self.service.GetTrainingSamples(request, None))
            self.assertEqual(len(responses), 10, "Should return exactly 10 samples.")
        except Exception as e:
            self.fail(f"testTrainingSamplesWithSpecificNumber raised an exception: {e}") 

    def testTrainingSamplesWithAllData(self):
        try:
            request = minstServiceProto_pb2.DataRequest(numOfSamples=0)  # Assuming 0 means all data
            responses = list(self.service.GetTrainingSamples(request, None))
            self.assertEqual(len(responses), len(self.service.train_images), "Should return all samples.")
        except Exception as e:
            self.fail(f"testTrainingSamplesWithAllData raised an exception: {e}")     


class ServerStartupTest(unittest.TestCase):
    
    def testServerStartup(self):
        try:
            server = serve(waitForTermination = False)
            self.assertIsNotNone(server, "server failed to start up")
        except Exception as e:
            print(f"testServerStartup failed.{e}")
            self.fail(f"server Startup had a problem")


if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    
    
    
    
