import unittest
from unittest.mock import patch
from MnistClientRun import getUserInput, processUserInput
from minstClient import MnistClient

class TestGetUserInput(unittest.TestCase):
    
    @patch('builtins.input', return_value='y')
    def testGetUserInput_y(self, mock_input):
        try:
            result = getUserInput()
            self.assertEqual(result, 'y')
        except Exception as e:
            self.fail(f"Problem in getting user input 'y' for full dataset {e}")

    @patch('builtins.input', return_value='q')
    def testGetUserInputq(self, mock_input):
        try:
            result = getUserInput()
            self.assertEqual(result, 'q')
        except Exception as e:
            self.fail(f"Problem in geting user input for quitting {e}")   

    @patch.object(MnistClient, 'showMnistData')
    def testProcessUserInput_y(self, mock_show_data):
        try:
            client = MnistClient('localhost:50051')
            result = processUserInput(client, 'y')
            mock_show_data.assert_called_once_with(-1)
            self.assertIsNone(result)
        except Exception as e:
            self.fail(f"Problem in processing user input letter {e}")
            
    @patch.object(MnistClient, 'showMnistData')
    def testProcessUserInputNumber(self, mock_show_data):
        try:
            client = MnistClient('localhost:50051')
            result = processUserInput(client, '100')
            mock_show_data.assert_called_once_with(100)
            self.assertIsNone(result)    
        except Exception as e:
            self.fail(f"Problem in processing user input number {e}")

if __name__ == '__main__':
    unittest.main(verbosity=2)        