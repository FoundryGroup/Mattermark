###############################################################################
# Python wrapper for the Mattermark API.
#
# Author: Carl Cortright
# Date: 10/27/2016
#
################################################################################
import requests

class mattermark:
    # Constants
    COMPANIES_URL = "https://api.mattermark.com/companies"
    INVESTOR_URL = "https://api.mattermark.com/investors"
    SEARCH_URL = "https://api.mattermark.com/search"

    #
    # Initialization function
    #
    def __init__(self, api_key, verbose=False):
        self.api_key = api_key
        self.verbose = verbose
        payload = {"key": self.api_key}
        if(requests.get(self.COMPANIES_URL, payload).status_code == 403):
            raise ValueError("Invalid API key")

    #
    # Searches for a company and returns a dictionary of results
    #
    def companySearch(self, company):
        payload = {"key": self.api_key, "term": company}
        result = requests.get(self.SEARCH_URL, payload)
        return result.json()

    #
    # Returns a dictionary of details about a company
    #
    def companyDetails(self, identifier):
        company_url = self.COMPANIES_URL + "/" + identifier
        payload = {"key": self.api_key}
        result = requests.get(company_url, payload)
        return result.json()


    #
    # Returns a dictionary of news stories about a company
    #
    def companyNews(self, identifier):
        company_url = self.COMPANIES_URL + "/" + str(identifier) + "/stories"
        payload = {"key": self.api_key}
        result = requests.get(company_url, payload)
        return result.json()

    #
    # Returns a list of compeditors
    #
    def companyCompeditors(self, identifier):
        company_url = self.COMPANIES_URL + "/" + identifier + "/similar"
        payload = {"key": self.api_key}
        result = requests.get(company_url, payload)
        return result.json()

    #
    # Returns a dictionary of important people at the company
    #
    def companyPersonnel(self, identifier):
        company_url = self.COMPANIES_URL + "/" + identifier + "/people"
        payload = {"key": self.api_key}
        result = requests.get(company_url, payload)
        return result.json()

    #
    # Return a list of the companies in the investor's portfolio
    #
    def investorPortfolio(self, investorID):
        company_list = []
        url = self.INVESTOR_URL + "/" + str(investorID) + "/portfolio"
        payload = {"key": self.api_key}
        result = requests.get(url, payload)
        results_p1 = result.json()
        # Add each company to the list
        for company in results_p1["companies"]:
            company_list.append(company)
        # Deal with paging
        if(results_p1["meta"]["total_pages"] > 1):
            for i in range(2, results_p1["meta"]["total_pages"]+1):
                payload = {"key": self.api_key, "page": i}
                result = requests.get(url, payload)
                results = result.json()
                for company in results["companies"]:
                    company_list.append(company)
        return company_list
