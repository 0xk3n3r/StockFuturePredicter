import unittest
import streamlit_app


class AlienTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("TestCase  start running ")

    def test_1_run(self):
        key = streamlit_app.get_Vantage()
        print(key)
        self.assertEqual(key['Time Series (Daily)']['2023-09-08'], {'1. open': '330.09',
                                                                    '2. high': '336.16',
                                                                    '3. low': '329.46',
                                                                    '4. close': '334.27',
                                                                    '5. adjusted close': '334.27',
                                                                    '6. volume': '19548165',
                                                                    '7. dividend amount': '0.0000',
                                                                    '8. split coefficient': '1.0'})


if __name__ == '__main__':
    print('hello world')
