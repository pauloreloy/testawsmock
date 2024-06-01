import unittest
from unittest.mock import patch, MagicMock
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.classes.AWS import AWS  # Adjust the import to match your module name

class TestAWS(unittest.TestCase):
    @patch('src.classes.AWS.boto3.client')
    def test_get_s3_object(self, mock_boto_client):
        # Create a mock S3 client
        mock_s3_client = MagicMock()

        # Mock the response from get_object
        mock_s3_client.get_object.return_value = {
            'Body': MagicMock(read=MagicMock(return_value=b'Mock Data'))
        }

        # Assign the mock S3 client to the boto3.client call
        mock_boto_client.return_value = mock_s3_client

        # Instantiate the AWS class and call the get_s3_object method
        aws = AWS()
        result = aws.get_s3_object('mock-bucket', 'mock-key')

        # Assertions
        mock_s3_client.get_object.assert_called_once_with(Bucket='mock-bucket', Key='mock-key')
        self.assertEqual(result, b'Mock Data')

if __name__ == '__main__':
    unittest.main()
