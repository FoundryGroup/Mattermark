################################################################################
# Test suite for the Mattermark API
#
# Author: Carl Cortright
# Date: 1/16/2017
#
################################################################################
import unittest
import yaml
from mattermark import mattermark

#
# Extends TestCase to test our mattermark api wrapper
#
class TestMattermark(unittest.TestCase):

    #
    # Override the default init so we have access to a universal mm object
    #
    def __init__(self, *args, **kwargs):
        # Call the super
        super(TestMattermark, self).__init__(*args, **kwargs)
        # Get the API key from the config file (for more info see 'recommended key storage')
        config_file = open(".config.yml")
        config_dict = yaml.safe_load(config_file)
        config_file.close()
        MM_API_KEY = config_dict["MM_API_KEY"]

        # Initialize a new mattermark object
        self.mm = mattermark(MM_API_KEY)

    def test_investor_search(self):
        self.assertEqual(self.mm.investorSearch("Foundry Group")[0]["object_id"], 38)

    def test_investor_portfolio(self):
        portfolio = self.mm.investorPortfolio(38)
        self.assertEqual(len(portfolio), 119)

    def test_investor_details(self):
        foundry_details = self.mm.investorDetails(38)
        self.assertEqual(foundry_details["website"], "foundrygroup.com")

    def test_funding_events(self):
        # Can't think of anything else consistent to test
        self.assertEqual(len(self.mm.fundingEvents()), 50)

    def test_company_news(self):
        # Can't think of anything else consistent to test
        self.assertEqual(len(self.mm.companyNews(146589)), 50)

    def test_company_search(self):
        mattermark_search = self.mm.companySearch("mattermark")
        self.assertEqual(mattermark_search[0]["object_name"], "Mattermark")

    def test_key_people(self):
        key_people = self.mm.companyPersonnel(146589)
        self.assertEqual(key_people[0]["title"], "CEO")

    def test_similar_companies(self):
        mm_similar_companies = self.mm.similarCompanies(146589)
        self.assertEqual(mm_similar_companies[0]["company_name"], "ITjuzi")


#
# Run the test cases
#
if(__name__ == "__main__"):
    unittest.main()
