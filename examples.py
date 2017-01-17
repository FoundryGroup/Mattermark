################################################################################
# Examples of how to use the mattermark package
#
# Author: Carl Cortright - Foundry Group
# Date: 1/16/2017
#
################################################################################
from mattermark import mattermark
import yaml

# Get the API key from the config file (for more info see 'recommended key storage')
config_file = open(".config.yml")
config_dict = yaml.safe_load(config_file)
config_file.close()
MM_API_KEY = config_dict["MM_API_KEY"]

# Initialize a new mattermark object
mm = mattermark(MM_API_KEY)

# Search for the foundry group
foundry_search = mm.investorSearch("Foundry Group")
