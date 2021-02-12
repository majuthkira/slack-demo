from flask_demo_api import app
import unittest
import json

class FlaskTest(unittest.TestCase):
    def test_response(self):
        tester = app.test_client(self)
        response = tester.get('/io')
        statuscode = response.status_code
        self.assertEqual(statuscode,200)


    def test_content_type(self):
        tester = app.test_client(self)
        response = tester.get('/io')
        print('ssss===================')
        print(response.content_type)
        #self.assertEqual(response.content_type, 'text/plain')
        #self.assertEqual(response.content_type, 'application/octet-stream')
        self.assertEqual(response.content_type, 'application/json')

    def test_content_data(self):
        tester = app.test_client(self)
        response = tester.get('/io')
        self.assertTrue(b'id' in response.data)


    def test_content_length(self):
        tester = app.test_client(self)
        response = tester.get('/io')
        temp = json.loads(response.data)['tasks']
        print(temp)
        self.assertGreater(len(temp),5,msg='Not Populated')

if __name__ == '__main__':
    unittest.main()