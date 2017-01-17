################################################################################
# Examples of how to use the mattermark package
#
# Author: Carl Cortright - Foundry Group
# Date: 1/16/2017
#
################################################################################
from mattermark import mattermark
import yaml
import pprint

# Get the API key from the config file (for more info see 'recommended key storage')
config_file = open(".config.yml")
config_dict = yaml.safe_load(config_file)
config_file.close()
MM_API_KEY = config_dict["MM_API_KEY"]

pp = pprint.PrettyPrinter()

# Initialize a new mattermark object
mm = mattermark(MM_API_KEY)

# Search for the FoundryGroup
foundry_search = mm.investorSearch("Foundry Group")
pp.pprint(foundry_search)
foundryID = foundry_search[0]["object_id"]

# Get the Foundry Group portfolio
foundry_portfolio = mm.investorPortfolio(foundryID)
pp.pprint(foundry_portfolio)

# Get details on the Foundry Group
foundry_details = mm.investorDetails(foundryID)
pp.pprint(foundry_details)

# See how many queries we have used
print(mm.queries)

# Get some of the funding events that have happened today
pp.pprint(mm.fundingEvents())

# Get even more funding events
pp.pprint(mm.fundingEvents(Pages=10))

# Search for "mattermark" in the company database
mattermark_search = mm.companySearch("mattermark")
pp.pprint(mattermark_search[0])
mmID = mattermark_search[0]["object_id"]

# Get details on the company
mattermark_details = mm.companyDetails(mmID)
print(mattermark_details["mattermark_score"])

# Get the key personnel
key_people = mm.companyPersonnel(mmID)
pp.pprint(key_people)

# And similar companies
mm_similar_companies = mm.similarCompanies(mmID)
pp.pprint(mm_similar_companies)

# Do a more advanced company search
parameters = {"last_funding_date": "raised in past 9 months", "industries": "Finance"}
company_list_search = mm.companiesList(parameters)
pp.pprint(company_list_search)
