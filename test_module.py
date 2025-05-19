import unittest
import pandas as pd
from demographic_data_analyzer import *

class TestDemographicDataAnalyzer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = load_data("E:/My PROJECTSS/census+income/adult.data")

    def test_count_high_earners(self):
        result = count_high_earners(self.df)
        self.assertTrue(isinstance(result, int))
        self.assertGreater(result, 0)

    def test_average_age_by_gender(self):
        male_avg = average_age_by_gender(self.df, 'Male')
        female_avg = average_age_by_gender(self.df, 'Female')
        self.assertTrue(male_avg > 0 and female_avg > 0)

    def test_percentage_bachelors(self):
        result = percentage_bachelors(self.df)
        self.assertTrue(0 < result < 100)

    def test_percentage_high_income_advanced_education(self):
        result = percentage_high_income_advanced_education(self.df)
        self.assertTrue(0 < result < 100)

    def test_percentage_high_income_non_advanced(self):
        result = percentage_high_income_non_advanced(self.df)
        self.assertTrue(0 < result < 100)

    def test_min_work_hours(self):
        self.assertEqual(min_work_hours(self.df), 1)

    def test_percentage_rich_min_hours(self):
        result = percentage_rich_min_hours(self.df)
        self.assertTrue(0 <= result <= 100)

    def test_country_with_highest_rich_percentage(self):
        country, percentage = country_with_highest_rich_percentage(self.df)
        self.assertIsInstance(country, str)
        self.assertTrue(0 <= percentage <= 100)

    def test_most_common_high_income_occupation_india(self):
        result = most_common_high_income_occupation_india(self.df)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
