
from django.test import TestCase
import pandas as pd

class csvFileTestCases(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass
        
    def test_state_wise_csv(self):
        
        df = pd.read_csv('state_wise.csv', header = None)
        self.assertFalse(df.empty)
        self.assertEqual(df[0][0], 'State')
        self.assertEqual(df[1][0], 'Confirmed')
        self.assertEqual(df[2][0], 'Recovered')
        self.assertEqual(df[3][0], 'Deaths')
    
    def test_case_time_series_csv(self):
        
        df = pd.read_csv('case_time_series.csv', header = None)
        self.assertFalse(df.empty)
        self.assertEqual(df[1][0], 'Date_YMD')
        self.assertEqual(df[3][0], 'Total Confirmed')
        self.assertEqual(df[5][0], 'Total Recovered')
        self.assertEqual(df[7][0], 'Total Deceased')
    
